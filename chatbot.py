import argparse
import json
import re
from pathlib import Path
from typing import Any


class CinemaBookingBot:
    # Simple chatbot with intent recognition, entity extraction and context management.
    #
    # Use case:
    # The chatbot simulates a cinema ticket booking assistant.
    #
    # Implemented concepts:
    # - keyword-based intent recognition
    # - regex-based entity extraction
    # - controlled movie list from JSON configuration
    # - dictionary-based conversation context

    def __init__(self, config_path: str = "chatbot_config.json") -> None:
        # Initialize the chatbot with configuration and an empty context.
        self.config = self._load_config(config_path)
        self.context = self._create_initial_context()

    def _load_config(self, config_path: str) -> dict[str, Any]:
        # Load chatbot configuration from a JSON file.
        #
        # The JSON file contains:
        # - known movies
        # - intents
        # - keywords
        # - default responses
        # - prompts for missing booking information

        path = Path(__file__).with_name(config_path)

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _create_initial_context(self) -> dict[str, Any]:
        # Create the initial conversation context.
        #
        # The context stores:
        # - current conversation state
        # - last recognized intent
        # - collected cinema booking data

        return {
            "state": "start",
            "last_intent": None,
            "booking": {
                "movie": None,
                "date": None,
                "time": None,
                "number_of_tickets": None,
            },
        }

    def reset_context(self) -> None:
        # Reset the conversation context.
        #
        # This is used when the user cancels the current booking process.

        self.context = self._create_initial_context()

    def _normalize_text(self, text: str) -> str:
        # Normalize user input for simple text matching.
        #
        # Example:
        # "Ich möchte MORGEN buchen." -> "ich möchte morgen buchen."

        return text.lower().strip()

    def _contains_keyword(self, text: str, keyword: str) -> bool:
        # Check whether a keyword is present in the user input.
        #
        # Short keywords are matched as complete words to avoid accidental matches.
        # Longer phrases are matched as substrings.

        keyword = keyword.lower()

        if len(keyword) <= 3:
            pattern = rf"\b{re.escape(keyword)}\b"
            return re.search(pattern, text) is not None

        return keyword in text

    def recognize_intent(self, user_input: str) -> str:
        # Recognize the user intent using keyword mappings from the JSON config.
        #
        # If no configured keyword is found but an entity is detected, the method
        # returns "provide_information". This allows the bot to continue collecting
        # missing booking data.

        normalized_input = self._normalize_text(user_input)
        intent_scores: dict[str, int] = {}

        # Check each configured intent and count how many keywords match.
        for intent, intent_data in self.config["intents"].items():
            keywords = intent_data.get("keywords", [])

            score = sum(
                1
                for keyword in keywords
                if self._contains_keyword(normalized_input, keyword)
            )

            if score > 0:
                intent_scores[intent] = score

        # If no keyword-based intent is found, check whether the user provided
        # useful booking information such as movie, date, time or ticket count.
        if not intent_scores:
            extracted_entities = self.extract_entities(user_input)

            if any(extracted_entities.values()):
                return "provide_information"

            if self.context["state"] == "collecting_booking":
                return "provide_information"

            return "fallback"

        # Priority is used when multiple intents match the same input.
        # Example: "nein, abbrechen" should be treated as cancellation.
        priority = [
            "cancel",
            "booking_request",
            "confirm_booking",
            "help",
            "greeting",
        ]

        best_intent = max(
            intent_scores,
            key=lambda intent: (intent_scores[intent], -priority.index(intent)),
        )

        return best_intent

    def extract_entities(self, user_input: str) -> dict[str, str | None]:
        # Extract movie, date, time and number of tickets from user input.
        #
        # This implementation uses:
        # - a controlled movie list from the JSON config
        # - regular expressions for dates, times and ticket numbers
        # - simple word lists for number words such as "zwei" or "drei"

        normalized_input = self._normalize_text(user_input)

        entities: dict[str, str | None] = {
            "movie": None,
            "date": None,
            "time": None,
            "number_of_tickets": None,
        }

        # Movie extraction from a controlled list in the JSON config.
        # This avoids confusing other parts of the sentence with a movie title.
        for movie in self.config.get("known_movies", []):
            if movie.lower() in normalized_input:
                entities["movie"] = movie
                break

        # Date extraction: numeric dates such as 15.07.2026 or 15.07.
        date_match = re.search(r"\b(\d{1,2}\.\d{1,2}\.?\d{0,4})\b", normalized_input)

        if date_match:
            entities["date"] = date_match.group(1)
        else:
            # Date extraction: relative dates and weekdays.
            relative_dates = [
                "heute",
                "morgen",
                "übermorgen",
                "montag",
                "dienstag",
                "mittwoch",
                "donnerstag",
                "freitag",
                "samstag",
                "sonntag",
            ]

            for date_word in relative_dates:
                if date_word in normalized_input:
                    entities["date"] = date_word
                    break

        # Time extraction: formats such as 18:30 or 18.30.
        time_match = re.search(r"\b([01]?\d|2[0-3])[:.]([0-5]\d)\b", normalized_input)

        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2))
            entities["time"] = f"{hour:02d}:{minute:02d}"
        else:
            # Time extraction: formats such as 20 Uhr.
            hour_match = re.search(r"\b([01]?\d|2[0-3])\s*uhr\b", normalized_input)

            if hour_match:
                hour = int(hour_match.group(1))
                entities["time"] = f"{hour:02d}:00"

        # Number of tickets: numeric expressions such as 2 Tickets or 3 Personen.
        ticket_match = re.search(
            r"\b(?:für|mit)?\s*(\d{1,2})\s*"
            r"(tickets|ticket|karten|karte|personen|person|gäste|gaeste|gast|leute)\b",
            normalized_input,
        )

        if ticket_match:
            entities["number_of_tickets"] = ticket_match.group(1)
        else:
            # Number of tickets: word-based expressions such as drei Tickets.
            number_words = {
                "eine": "1",
                "einen": "1",
                "ein": "1",
                "zwei": "2",
                "drei": "3",
                "vier": "4",
                "fünf": "5",
                "fuenf": "5",
                "sechs": "6",
                "sieben": "7",
                "acht": "8",
                "neun": "9",
                "zehn": "10",
            }

            for word, number in number_words.items():
                pattern = (
                    rf"\b{word}\s*"
                    r"(tickets|ticket|karten|karte|personen|person|gäste|gaeste|gast|leute)\b"
                )

                if re.search(pattern, normalized_input):
                    entities["number_of_tickets"] = number
                    break

        return entities

    def update_context(self, intent: str, entities: dict[str, str | None]) -> None:
        # Update the conversation context with the latest intent and entities.

        self.context["last_intent"] = intent

        for entity_name, entity_value in entities.items():
            if entity_value:
                self.context["booking"][entity_name] = entity_value

    def _missing_booking_fields(self) -> list[str]:
        # Return all booking fields that are still missing.

        booking = self.context["booking"]

        return [
            field
            for field, value in booking.items()
            if value is None
        ]

    def _next_question(self) -> str:
        # Ask the next question based on missing booking fields.
        #
        # The order is:
        # 1. movie
        # 2. date
        # 3. time
        # 4. number of tickets

        missing_fields = self._missing_booking_fields()
        prompts = self.config["prompts"]

        if "movie" in missing_fields:
            return prompts["ask_movie"]

        if "date" in missing_fields:
            return prompts["ask_date"]

        if "time" in missing_fields:
            return prompts["ask_time"]

        if "number_of_tickets" in missing_fields:
            return prompts["ask_tickets"]

        return self._booking_summary() + " " + prompts["ask_confirmation"]

    def _booking_summary(self) -> str:
        # Create a short summary of the current booking context.

        booking = self.context["booking"]

        return (
            "Ich habe folgende Buchungsdaten verstanden: "
            f"Film: {booking['movie']}, "
            f"Datum: {booking['date']}, "
            f"Uhrzeit: {booking['time']}, "
            f"Tickets: {booking['number_of_tickets']}."
        )

    def generate_response(self, intent: str) -> str:
        # Generate a chatbot response based on intent and current context.
        #
        # This method connects:
        # - recognized intent
        # - extracted entities
        # - stored conversation context

        if intent == "cancel":
            self.reset_context()
            return self.config["intents"]["cancel"]["response"]

        if intent == "help":
            return self.config["intents"]["help"]["response"]

        if intent == "greeting" and self.context["state"] == "start":
            return self.config["intents"]["greeting"]["response"]

        if intent == "booking_request":
            self.context["state"] = "collecting_booking"
            return self._next_question()

        if intent == "provide_information":
            if self.context["state"] == "start":
                self.context["state"] = "collecting_booking"

            return self._next_question()

        if intent == "confirm_booking":
            if self._missing_booking_fields():
                self.context["state"] = "collecting_booking"
                return (
                    "Es fehlen noch Informationen für die Buchung. "
                    + self._next_question()
                )

            self.context["state"] = "completed"
            return (
                self.config["intents"]["confirm_booking"]["response"]
                + " "
                + self._booking_summary()
            )

        if self.context["state"] == "collecting_booking":
            return self._next_question()

        return self.config["fallback_response"]

    def process_input(self, user_input: str) -> str:
        # Process a user message and return the chatbot response.
        #
        # Processing order:
        # 1. recognize intent
        # 2. extract entities
        # 3. update context
        # 4. generate response

        intent = self.recognize_intent(user_input)
        entities = self.extract_entities(user_input)

        self.update_context(intent, entities)

        return self.generate_response(intent)


def run_demo() -> None:
    # Run a predefined demo conversation.

    bot = CinemaBookingBot()

    demo_messages = [
        "Hallo",
        "Ich möchte Kinotickets buchen.",
        "Für Dune",
        "Morgen",
        "Um 20 Uhr",
        "Für 2 Personen",
        "Ja, das passt.",
    ]

    print("Demo: Cinema Ticket Booking Chatbot")
    print("=" * 50)

    for message in demo_messages:
        response = bot.process_input(message)

        print(f"User: {message}")
        print(f"Bot:  {response}")
        print("-" * 50)


def run_interactive_mode() -> None:
    # Run the chatbot in interactive command-line mode.

    bot = CinemaBookingBot()

    print("Cinema Ticket Booking Chatbot")
    print("Type 'exit' to stop the conversation.")
    print("=" * 50)

    while True:
        user_input = input("User: ")

        if user_input.lower().strip() in {"exit", "quit"}:
            print("Bot: Auf Wiedersehen!")
            break

        response = bot.process_input(user_input)
        print(f"Bot:  {response}")


def run_self_test() -> None:
    # Run simple self-tests for the chatbot.
    #
    # These tests verify that the chatbot can:
    # - detect a booking request
    # - extract movie, date, time and number of tickets
    # - preserve context across multiple turns
    # - generate a final confirmation response

    bot = CinemaBookingBot()

    assert bot.recognize_intent("Hallo") == "greeting"
    assert bot.recognize_intent("Ich möchte Kinotickets buchen.") == "booking_request"

    entities = bot.extract_entities("Dune morgen um 20 Uhr für 2 Personen")
    assert entities["movie"] == "Dune"
    assert entities["date"] == "morgen"
    assert entities["time"] == "20:00"
    assert entities["number_of_tickets"] == "2"

    bot.process_input("Ich möchte Kinotickets buchen.")
    bot.process_input("Für Dune")
    bot.process_input("Morgen")
    bot.process_input("Um 20 Uhr")
    response = bot.process_input("Für 2 Personen")

    assert "Film: Dune" in response
    assert "Datum: morgen" in response
    assert "Uhrzeit: 20:00" in response
    assert "Tickets: 2" in response

    final_response = bot.process_input("Ja, das passt.")
    assert "vorgemerkt" in final_response

    print("All self-tests passed successfully.")


def main() -> None:
    # Parse command-line arguments and start the selected mode.

    parser = argparse.ArgumentParser(
        description="Simple AI-based chatbot with intents, entities and context."
    )

    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run a predefined demo conversation.",
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Start an interactive chatbot session.",
    )

    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run simple self-tests.",
    )

    args = parser.parse_args()

    if args.self_test:
        run_self_test()
    elif args.interactive:
        run_interactive_mode()
    else:
        run_demo()


if __name__ == "__main__":
    main()
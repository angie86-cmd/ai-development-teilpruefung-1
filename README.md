# AI-basierter Chatbot - Teilprüfung 1

Dieses Projekt enthält eine einfache Python-Implementierung eines AI-basierten Chatbots für eine Kinoticket-Buchung.

Der Chatbot ist in der Lage, einfache Konversationen zu führen, Benutzeranfragen anhand von Intents zu erkennen, relevante Entities aus der Eingabe zu extrahieren und den Kontext über mehrere Nachrichten hinweg zu speichern.

## Ziel der Implementierung

Ziel ist die Entwicklung eines einfachen Chatbots, der folgende grundlegende Komponenten enthält:

- Intent Recognition
- Entity-Extraktion
- Kontextverwaltung
- kontextabhängige Antwortgenerierung

Der Chatbot unterstützt eine einfache Kinoticket-Buchung. Dazu sammelt er während der Konversation folgende Informationen:

- Film
- Datum
- Uhrzeit
- Anzahl der Tickets beziehungsweise Personen

Sobald alle Informationen vorhanden sind, fasst der Chatbot die Buchungsdaten zusammen und fragt nach einer Bestätigung.

## Dateien

```text
ai-development-teilpruefung-1/
├── README.md
├── chatbot.py
├── chatbot_config.json
├── beispiel_dialog.txt
├── requirements.txt
├── .gitignore
└── submission/
    └── Angie_Angarita_Soto_Teilprüfung 1.zip
```

---

# a) Grundlegende Architektur des Chatbots

Die Architektur des Chatbots besteht aus mehreren einfachen, klar getrennten Komponenten.

```text
User Input
    ↓
Input Processing
    ↓
Intent Recognition
    ↓
Entity Extraction
    ↓
Context Management
    ↓
Response Generation
    ↓
Bot Response
```

## 1. Input Processing

Die Benutzereingabe wird zunächst vorbereitet. Dazu wird der Text normalisiert:

- Umwandlung in Kleinbuchstaben
- Entfernen überflüssiger Leerzeichen
- Vorbereitung für Schlüsselwortsuche und reguläre Ausdrücke

Beispiel:

```text
"Ich möchte MORGEN um 20 Uhr Dune sehen."
→ "ich möchte morgen um 20 uhr dune sehen."
```

Diese Normalisierung erleichtert die weitere Verarbeitung durch Intent Recognition und Entity-Extraktion.

## 2. Intent Recognition

Die Intent Recognition erkennt die Absicht des Nutzers. Dazu verwendet der Chatbot ein einfaches Mapping von Schlüsselwörtern zu vordefinierten Intents.

Die Intents und Schlüsselwörter werden in der Datei `chatbot_config.json` gepflegt.

Beispiele für Intents:

| Intent | Bedeutung |
|---|---|
| `greeting` | Der Nutzer begrüßt den Chatbot. |
| `booking_request` | Der Nutzer möchte Kinotickets buchen. |
| `provide_information` | Der Nutzer liefert Film, Datum, Uhrzeit oder Ticketanzahl. |
| `confirm_booking` | Der Nutzer bestätigt die gesammelten Buchungsdaten. |
| `cancel` | Der Nutzer bricht den Vorgang ab. |
| `help` | Der Nutzer fragt nach Unterstützung. |
| `fallback` | Die Eingabe wurde nicht verstanden. |

Beispiel:

```text
"Ich möchte Kinotickets buchen."
→ Intent: booking_request
```

## 3. Entity-Extraktion

Die Entity-Extraktion erkennt konkrete Informationen innerhalb der Benutzereingabe.

In dieser Implementierung werden folgende Entities extrahiert:

| Entity | Beispiel |
|---|---|
| `movie` | Dune, Barbie, Inside Out |
| `date` | morgen, freitag, 15.07.2026 |
| `time` | 20 Uhr, 18:30 |
| `number_of_tickets` | 2 Tickets, drei Personen |

Beispiele:

```text
"Für Dune" → movie = Dune
"Morgen" → date = morgen
"Um 20 Uhr" → time = 20:00
"Für 2 Personen" → number_of_tickets = 2
```

Die Extraktion erfolgt mit einfachen regulären Ausdrücken, kontrollierten Wortlisten und einer kleinen Liste bekannter Filme.

## 4. Context Management

Die Kontextverwaltung speichert den aktuellen Zustand der Konversation.

Der Chatbot merkt sich, welche Informationen bereits genannt wurden und welche noch fehlen.

Der Kontext wird in einem Python-Dictionary gespeichert:

```python
{
    "state": "collecting_booking",
    "last_intent": "provide_information",
    "booking": {
        "movie": "Dune",
        "date": "morgen",
        "time": "20:00",
        "number_of_tickets": "2"
    }
}
```

Dadurch kann der Chatbot über mehrere Nachrichten hinweg eine zusammenhängende Konversation führen.

Beispiel:

```text
User: Ich möchte Kinotickets buchen.
Bot: Für welchen Film möchten Sie Tickets buchen?

User: Für Dune
Bot: Für welches Datum möchten Sie buchen?
```

Der Chatbot weiß in diesem Beispiel, dass der Film bereits vorhanden ist und als Nächstes das Datum fehlt.

## 5. Response Generation

Die Antwortgenerierung kombiniert:

- den erkannten Intent
- die extrahierten Entities
- den aktuellen Kontextzustand

Wenn noch Informationen fehlen, stellt der Chatbot eine gezielte Rückfrage.

Wenn alle benötigten Informationen vorhanden sind, erstellt der Chatbot eine Zusammenfassung der Buchung.

Beispiel:

```text
Ich habe folgende Buchungsdaten verstanden: Film: Dune, Datum: morgen, Uhrzeit: 20:00, Tickets: 2. Soll ich die Buchung bestätigen?
```

## Zusammenspiel der Komponenten

Die Komponenten arbeiten wie folgt zusammen:

1. Der Nutzer schreibt eine Nachricht.
2. Die Eingabe wird normalisiert.
3. Die Intent Recognition erkennt die Absicht des Nutzers.
4. Die Entity-Extraktion sucht nach Film, Datum, Uhrzeit und Ticketanzahl.
5. Die Kontextverwaltung speichert neue Informationen.
6. Die Antwortgenerierung entscheidet, ob eine Rückfrage, eine Bestätigung oder eine Fallback-Antwort notwendig ist.
7. Der Bot gibt eine kontextabhängige Antwort aus.

Dadurch entsteht eine einfache, aber kohärente Konversation.

---

# b) Intent-Recognition-Funktion

Die Intent Recognition ist in der Methode `recognize_intent()` in der Datei `chatbot.py` implementiert.

Sie erkennt den Intent eines Benutzereingabetextes anhand eines einfachen Mappings von Schlüsselwörtern zu Intents.

Die Schlüsselwörter werden in der Datei `chatbot_config.json` definiert.

Beispiel aus `chatbot_config.json`:

```json
{
  "booking_request": {
    "keywords": [
      "ticket",
      "tickets",
      "kino",
      "film",
      "buchen",
      "buchung",
      "reservieren"
    ],
    "response": "Gerne. Ich helfe Ihnen bei der Kinoticket-Buchung."
  }
}
```

Wenn die Eingabe eines Nutzers eines dieser Schlüsselwörter enthält, wird der Intent `booking_request` erkannt.

Beispiel:

```text
User: Ich möchte Kinotickets buchen.
Erkannter Intent: booking_request
```

Die Implementierung ist bewusst einfach und transparent gehalten.

Wenn kein Keyword gefunden wird, prüft der Chatbot zusätzlich, ob Entities wie Film, Datum, Uhrzeit oder Ticketanzahl erkannt wurden. In diesem Fall wird der Intent `provide_information` verwendet.

Beispiel:

```text
User: Morgen
Erkannte Entity: date = morgen
Erkannter Intent: provide_information
```

Dadurch kann der Chatbot auch dann sinnvoll weiterarbeiten, wenn die Eingabe kein klassisches Schlüsselwort enthält, aber relevante Informationen liefert.

---

# c) Entity-Extraktionsfunktion

Die Entity-Extraktion ist in der Methode `extract_entities()` in der Datei `chatbot.py` implementiert.

Sie extrahiert spezifische Informationen aus dem Benutzereingabetext.

Extrahiert werden:

- Film
- Datum
- Uhrzeit
- Anzahl der Tickets beziehungsweise Personen

## Film

Der Chatbot erkennt Filme aus einer kontrollierten Liste in `chatbot_config.json`.

Beispiele:

```text
Dune
Barbie
Inside Out
Oppenheimer
Avatar
```

Beispiel:

```text
User: Für Dune
→ movie = Dune
```

## Datum

Der Chatbot erkennt einfache Datumsangaben wie:

```text
15.07.2026
15.07.
morgen
übermorgen
freitag
samstag
```

Beispiele:

```text
User: Morgen
→ date = morgen

User: Ich möchte am 15.07.2026 buchen.
→ date = 15.07.2026
```

## Uhrzeit

Der Chatbot erkennt Uhrzeiten in einfachen Formaten:

```text
20 Uhr
18:30
18.30
```

Beispiele:

```text
User: Um 20 Uhr
→ time = 20:00

User: Um 18:30
→ time = 18:30
```

## Anzahl der Tickets oder Personen

Der Chatbot erkennt numerische und einfache ausgeschriebene Angaben:

```text
2 Tickets
für 3 Personen
zwei Gäste
drei Karten
```

Beispiele:

```text
User: Für 2 Personen
→ number_of_tickets = 2

User: Drei Tickets
→ number_of_tickets = 3
```

Die Entity-Extraktion wird mit regulären Ausdrücken und kontrollierten Wortlisten umgesetzt.

Diese Lösung ist einfach, nachvollziehbar und für den Anwendungsfall einer Kinoticket-Buchung ausreichend.

---

# d) Kontextverwaltungssystem

Das Kontextverwaltungssystem ist im Chatbot über das Attribut `self.context` implementiert.

Der Kontext speichert:

- den aktuellen Zustand der Konversation
- den zuletzt erkannten Intent
- die bereits gesammelten Buchungsdaten

Beispiel für den Anfangszustand:

```python
{
    "state": "start",
    "last_intent": None,
    "booking": {
        "movie": None,
        "date": None,
        "time": None,
        "number_of_tickets": None
    }
}
```

Sobald der Nutzer Informationen liefert, wird der Kontext aktualisiert.

Beispiel nach mehreren Nachrichten:

```python
{
    "state": "collecting_booking",
    "last_intent": "provide_information",
    "booking": {
        "movie": "Dune",
        "date": "morgen",
        "time": "20:00",
        "number_of_tickets": "2"
    }
}
```

## Kontextabhängige Antworten

Der Bot prüft nach jeder Eingabe, welche Informationen noch fehlen.

Wenn der Film fehlt, fragt er:

```text
Für welchen Film möchten Sie Tickets buchen?
```

Wenn das Datum fehlt, fragt er:

```text
Für welches Datum möchten Sie buchen?
```

Wenn die Uhrzeit fehlt, fragt er:

```text
Zu welcher Uhrzeit möchten Sie den Film sehen?
```

Wenn die Anzahl der Tickets fehlt, fragt er:

```text
Für wie viele Personen möchten Sie Tickets buchen?
```

Wenn alle Informationen vorhanden sind, fasst der Bot die Buchung zusammen:

```text
Ich habe folgende Buchungsdaten verstanden: Film: Dune, Datum: morgen, Uhrzeit: 20:00, Tickets: 2. Soll ich die Buchung bestätigen?
```

Die Kontextverwaltung ermöglicht dadurch eine einfache mehrstufige Konversation.

---

# Ausführung

## Demo-Konversation starten

```bash
python chatbot.py --demo
```

## Interaktiven Modus starten

```bash
python chatbot.py --interactive
```

## Selbsttests ausführen

```bash
python chatbot.py --self-test
```

Die Selbsttests prüfen unter anderem:

- Intent Recognition
- Entity Extraction
- Kontextaktualisierung
- finale Bestätigung der Buchung

Erwartete Ausgabe:

```text
All self-tests passed successfully.
```

---

# Beispieldialog

```text
User: Hallo
Bot: Hallo! Ich kann Ihnen bei einer Kinoticket-Buchung helfen.

User: Ich möchte Kinotickets buchen.
Bot: Für welchen Film möchten Sie Tickets buchen?

User: Für Dune
Bot: Für welches Datum möchten Sie buchen?

User: Morgen
Bot: Zu welcher Uhrzeit möchten Sie den Film sehen?

User: Um 20 Uhr
Bot: Für wie viele Personen möchten Sie Tickets buchen?

User: Für 2 Personen
Bot: Ich habe folgende Buchungsdaten verstanden: Film: Dune, Datum: morgen, Uhrzeit: 20:00, Tickets: 2. Soll ich die Buchung bestätigen?

User: Ja, das passt.
Bot: Vielen Dank. Ihre Kinoticket-Buchung wurde vorgemerkt. Ich habe folgende Buchungsdaten verstanden: Film: Dune, Datum: morgen, Uhrzeit: 20:00, Tickets: 2.
```

---

# Grenzen der Implementierung

Diese Implementierung verwendet bewusst eine einfache keyword-basierte Intent Recognition und regex-basierte Entity-Extraktion.

Die Lösung ist für eine transparente und didaktische Demonstration geeignet, aber nicht als produktives Chatbot-System gedacht.

Für produktive Systeme könnten moderne Verfahren ergänzt werden, zum Beispiel:

- semantisches Routing mit Embeddings
- LLM-basierte Intent-Erkennung
- Tool Calling
- RAG für Wissenszugriff
- Guardrails
- Evaluation und Monitoring

Die vorliegende Lösung erfüllt den Zweck, die grundlegenden Komponenten eines AI-basierten Chatbots verständlich und nachvollziehbar zu demonstrieren.
# AI-basierter Chatbot - Teilprüfung 1

## Teilprüfung 1

### Aufgabe

Entwickle einen einfachen AI-basierten Chatbot in Python, der in der Lage ist, einfache Konversationen zu führen und dabei spezifische Benutzeranfragen basierend auf Intents und Entities zu erkennen und zu beantworten. Der Chatbot soll in der Lage sein, Kontext über die Dauer einer Konversation zu speichern und zu verwenden, um relevante Antworten zu generieren.

Folge diesen Schritten:

a) Definiere eine grundlegende Architektur für deinen Chatbot, einschließlich der Komponenten für Intent-Recognition, Entity-Extraktion und Kontextverwaltung. Beschreibe, wie jede Komponente funktioniert und wie sie zusammenarbeiten, um eine kohärente Konversation zu ermöglichen.

b) Implementiere eine einfache Intent-Recognition-Funktion, die aus einer Liste vordefinierter Intents den Intent eines Benutzereingabetextes erkennen kann. Verwende dazu ein einfaches Mapping von Schlüsselwörtern zu Intents.

c) Erstelle eine Entity-Extraktionsfunktion, die spezifische Informationen (z.B. Datum, Zeit, Anzahl der Personen) aus dem Benutzereingabetext extrahieren kann.

d) Implementiere ein einfaches Kontextverwaltungssystem, das in der Lage ist, den aktuellen Zustand einer Konversation zu speichern und zu aktualisieren, um kontextabhängige Antworten zu generieren.

---

# Lösung

## Einleitung

Im Rahmen dieser Arbeit wurde ein einfacher AI-basierter Chatbot in Python entwickelt. Der Chatbot demonstriert grundlegende Konzepte der Chatbot-Entwicklung, insbesondere Intent Recognition, Entity-Extraktion und Kontextverwaltung.

Als Anwendungsfall wurde bewusst eine Kinoticket-Buchung gewählt. Der Chatbot unterstützt den Nutzer dabei, eine einfache Buchungsanfrage vorzubereiten. Dafür sammelt er über mehrere Nachrichten hinweg die relevanten Informationen: Film, Datum, Uhrzeit und Anzahl der Tickets beziehungsweise Personen.

Der Anwendungsfall wurde gewählt, weil er einfach genug ist, um die grundlegenden Chatbot-Komponenten transparent zu zeigen, aber gleichzeitig mehrere typische Anforderungen an dialogbasierte Systeme enthält. Eine Kinoticket-Buchung erfordert die Erkennung einer Nutzerabsicht, die Extraktion konkreter Informationen und die Speicherung des Gesprächskontexts über mehrere Nachrichten hinweg.

Die Projektdateien wurden in einem separaten GitHub-Repository erstellt und versioniert:

```text
https://github.com/angie86-cmd/ai-development-teilpruefung-1
```

Das Repository dient der strukturierten Dokumentation der Umsetzung. Durch die Nutzung von Git und GitHub ist nachvollziehbar, welche Dateien erstellt wurden und wie sich die Implementierung entwickelt hat. Dadurch wird die Lösung reproduzierbar, wartbar und transparent dokumentiert.

Die eigentliche Abgabe erfolgt zusätzlich als ZIP-Archiv gemäß den Vorgaben. Das ZIP-Archiv befindet sich im Ordner `submission/` und enthält ausschließlich erlaubte Dateitypen wie `.md`, `.py`, `.json` und `.txt`.

Die Umsetzung trennt bewusst Dokumentation, Programmlogik, Konfiguration und Beispieldialog:

- `README.md` dokumentiert Aufgabe, Architektur, Vorgehensweise und Umsetzung.
- `chatbot.py` enthält die Python-Implementierung des Chatbots.
- `chatbot_config.json` enthält Intents, Schlüsselwörter, Standardantworten und Prompts.
- `beispiel_dialog.txt` zeigt eine beispielhafte Konversation.
- `requirements.txt` dokumentiert die technischen Voraussetzungen.

Diese Struktur wurde gewählt, um die Lösung übersichtlich und nachvollziehbar zu halten. Gleichzeitig zeigt sie eine saubere Trennung zwischen Konfiguration und Programmlogik, was die Wartbarkeit des Chatbots verbessert.

## Projektstruktur und Versionierung

Für die Umsetzung wurde eine übersichtliche Projektstruktur erstellt, die die verschiedenen Bestandteile der Lösung voneinander trennt. Dadurch bleibt nachvollziehbar, welche Dateien für die Implementierung, die Konfiguration, den Beispieldialog und die finale Abgabe verwendet wurden.

Die verwendete Projektstruktur lautet:

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

**Tabelle 1: Dateien und Zweck im Projekt**

| Datei | Zweck |
|---|---|
| `README.md` | Dokumentation der Aufgabe, Architektur, Komponenten und Umsetzungsschritte |
| `chatbot.py` | Python-Implementierung des Chatbots |
| `chatbot_config.json` | Konfiguration der Intents, Schlüsselwörter, Antworten, Filme und Prompts |
| `beispiel_dialog.txt` | Beispielhafte Konversation zur Demonstration der Kontextverwaltung |
| `requirements.txt` | Technische Voraussetzungen |
| `.gitignore` | Ausschluss technischer Hilfsdateien aus der Versionskontrolle |
| `submission/Angie_Angarita_Soto_Teilprüfung 1.zip` | ZIP-Datei für die Abgabe |

Die lokale Projektstruktur wurde mit Git versioniert und anschließend in ein GitHub-Repository übertragen. Dadurch sind sämtliche Änderungen nachvollziehbar dokumentiert und können bei Bedarf reproduziert werden.

Die Verwendung von Git und GitHub unterstützt einen reproduzierbaren und transparenten Arbeitsablauf. Änderungen an Code, Konfiguration und Dokumentation können versioniert, überprüft und bei Bedarf nachvollzogen werden. Gleichzeitig entspricht dieser Ansatz modernen Praktiken aus den Bereichen DevOps und AI-Assisted Software Engineering.

---

# a) Grundlegende Architektur des Chatbots

## a.1 Ziel der Architektur

Die grundlegende Architektur des Chatbots wurde so entworfen, dass die zentralen Bestandteile eines einfachen dialogbasierten KI-Systems klar abgebildet werden:

- Intent Recognition
- Entity-Extraktion
- Kontextverwaltung
- kontextabhängige Antwortgenerierung

Der Chatbot soll nicht nur einzelne Eingaben isoliert beantworten, sondern eine einfache mehrstufige Konversation führen. Dafür muss er erkennen, was der Nutzer möchte, relevante Informationen aus der Eingabe extrahieren und sich bereits genannte Informationen merken.

Der gewählte Anwendungsfall einer Kinoticket-Buchung eignet sich gut für diese Architektur, weil eine vollständige Buchung typischerweise aus mehreren Informationen besteht:

- Film
- Datum
- Uhrzeit
- Anzahl der Tickets beziehungsweise Personen

Diese Informationen werden nicht zwingend in einer einzigen Nachricht genannt. Deshalb benötigt der Chatbot ein Kontextverwaltungssystem, das den aktuellen Zustand der Konversation speichert und fehlende Informationen gezielt nachfragt.

## a.2 Architekturüberblick

Die Architektur des Chatbots besteht aus mehreren klar getrennten Komponenten.

**Abbildung 1: Gesamtarchitektur des Chatbots**

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

Der Chatbot folgt damit einer einfachen Input-Processing-Output-Pipeline. Die Nutzereingabe wird zuerst vorbereitet, anschließend hinsichtlich Absicht und relevanter Informationen analysiert. Danach wird der Konversationskontext aktualisiert und eine passende Antwort erzeugt.

## a.3 Begründung der gewählten Architektur

Die Architektur wurde so gewählt, dass der Chatbot die Anforderungen eines einfachen Kinoticket-Buchungsassistenten transparent, wartbar und nachvollziehbar erfüllt.

Der Chatbot benötigt keine komplexe externe Infrastruktur, keine Datenbank und keine API-Anbindung, weil der Fokus auf der Demonstration der Grundkomponenten liegt. Die verfügbaren Ressourcen des Systems sind bewusst einfach gehalten:

- eine kleine Liste bekannter Filme
- vordefinierte Intents
- Schlüsselwörter zur Intent-Erkennung
- reguläre Ausdrücke zur Entity-Extraktion
- ein Python-Dictionary zur Speicherung des Konversationszustands
- vordefinierte Rückfragen und Antworten

Für einen Kinoticket-Buchungsassistenten ist diese Architektur ausreichend, weil der Dialog einem klaren Ablauf folgt: Der Nutzer möchte Tickets buchen, nennt einen Film, ein Datum, eine Uhrzeit und die Anzahl der Tickets. Der Bot sammelt diese Informationen schrittweise und fasst sie am Ende zusammen.

Die Architektur wurde außerdem gewählt, weil sie eine klare Trennung zwischen Absicht, Informationen und Gesprächszustand ermöglicht. Die Intent Recognition beantwortet die Frage, was der Nutzer tun möchte. Die Entity-Extraktion beantwortet die Frage, welche konkreten Informationen der Nutzer genannt hat. Die Kontextverwaltung beantwortet die Frage, welche Informationen bereits im Gespräch gespeichert wurden und welche noch fehlen.

Dadurch entsteht eine nachvollziehbare Verarbeitungskette:

```text
Absicht erkennen
→ Informationen extrahieren
→ Kontext aktualisieren
→ passende Antwort generieren
```

Diese Trennung ist wichtig, weil ein Chatbot sonst schnell unübersichtlich wird. Wenn alle Regeln, Antworten und Zustände direkt in einer einzigen Funktion vermischt würden, wäre die Lösung schwerer zu verstehen, zu testen und zu erweitern.

**Tabelle 2: Komponenten der Chatbot-Architektur**

| Komponente | Aufgabe | Umsetzung im Projekt |
|---|---|---|
| Input Processing | Vorbereitung der Nutzereingabe | Normalisierung in Kleinbuchstaben und Entfernen überflüssiger Leerzeichen |
| Intent Recognition | Erkennung der Nutzerabsicht | Keyword-Mapping aus `chatbot_config.json` |
| Entity Extraction | Extraktion relevanter Informationen | Reguläre Ausdrücke, Wortlisten und bekannte Filmtitel |
| Context Management | Speicherung des Konversationszustands | Python-Dictionary `self.context` |
| Response Generation | Erzeugung passender Antworten | Kombination aus Intent, Entities und Kontext |

Die technische Basis ist bewusst schlank gehalten. Der Chatbot nutzt ausschließlich Python-Standardbibliotheken wie `json`, `re`, `argparse`, `pathlib` und `typing`. Dadurch kann er ohne zusätzliche externe Pakete ausgeführt werden. Das ist für einen einfachen Prototyp sinnvoll, weil die Lösung reproduzierbar bleibt und keine komplexe Installationsumgebung benötigt.

## a.4 Zusammenspiel der Komponenten

Die Komponenten arbeiten nicht isoliert, sondern bauen aufeinander auf.

**Abbildung 2: Datenfluss innerhalb des Chatbots**

```text
Beispielhafte Eingabe:
"Ich möchte morgen um 20 Uhr Dune für 2 Personen sehen."

1. Input Processing
   → "ich möchte morgen um 20 uhr dune für 2 personen sehen."

2. Intent Recognition
   → booking_request oder provide_information

3. Entity Extraction
   → movie = Dune
   → date = morgen
   → time = 20:00
   → number_of_tickets = 2

4. Context Management
   → speichert die extrahierten Informationen im Kontext

5. Response Generation
   → erzeugt eine Zusammenfassung oder fragt nach fehlenden Informationen
```

Dadurch kann der Chatbot eine mehrstufige Konversation führen. Wenn der Nutzer nicht alle Informationen in einer Nachricht liefert, fragt der Chatbot gezielt nach den fehlenden Angaben.

Beispiel:

```text
User: Ich möchte Kinotickets buchen.
Bot: Für welchen Film möchten Sie Tickets buchen?

User: Für Dune
Bot: Für welches Datum möchten Sie buchen?
```

Der Chatbot erkennt in diesem Beispiel, dass bereits eine Buchungsabsicht vorliegt und dass der Film inzwischen bekannt ist. Deshalb fragt er als Nächstes nach dem Datum.

## a.5 Input Processing

Die Benutzereingabe wird zunächst vorbereitet. Dazu wird der Text normalisiert.

Die Normalisierung umfasst:

- Umwandlung in Kleinbuchstaben
- Entfernen überflüssiger Leerzeichen
- Vorbereitung für Schlüsselwortsuche und reguläre Ausdrücke

Beispiel:

```text
"Ich möchte MORGEN um 20 Uhr Dune sehen."
→ "ich möchte morgen um 20 uhr dune sehen."
```

Diese Normalisierung erleichtert die weitere Verarbeitung durch Intent Recognition und Entity-Extraktion, weil unterschiedliche Schreibweisen einfacher verglichen werden können.

## a.6 Intent Recognition

Die Intent Recognition erkennt die Absicht des Nutzers. Dazu verwendet der Chatbot ein einfaches Mapping von Schlüsselwörtern zu vordefinierten Intents.

Die Intents und Schlüsselwörter werden in der Datei `chatbot_config.json` gepflegt.

**Tabelle 3: Implementierte Intents**

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

Die Intent Recognition bildet damit den ersten Schritt zur Interpretation der Nutzerabsicht. Sie entscheidet, ob der Nutzer eine Buchung starten, Informationen liefern, eine Buchung bestätigen, abbrechen oder Hilfe erhalten möchte.

## a.7 Entity-Extraktion

Die Entity-Extraktion erkennt konkrete Informationen innerhalb der Benutzereingabe.

In dieser Implementierung werden folgende Entities extrahiert:

**Tabelle 4: Implementierte Entities**

| Entity | Beispiel | Bedeutung im Buchungsprozess |
|---|---|---|
| `movie` | Dune, Barbie, Inside Out | Gewünschter Film |
| `date` | morgen, freitag, 15.07.2026 | Gewünschtes Datum |
| `time` | 20 Uhr, 18:30 | Gewünschte Uhrzeit |
| `number_of_tickets` | 2 Tickets, drei Personen | Anzahl der Tickets beziehungsweise Personen |

Beispiele:

```text
"Für Dune" → movie = Dune
"Morgen" → date = morgen
"Um 20 Uhr" → time = 20:00
"Für 2 Personen" → number_of_tickets = 2
```

Die Extraktion erfolgt mit einfachen regulären Ausdrücken, kontrollierten Wortlisten und einer kleinen Liste bekannter Filme.

## a.8 Context Management

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

Ohne Kontextverwaltung müsste der Nutzer alle Informationen in jeder Nachricht wiederholen. Mit Kontextverwaltung kann der Chatbot dagegen bereits genannte Informationen speichern und nur noch fehlende Angaben nachfragen.

## a.9 Response Generation

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

Die Antwortgenerierung ist damit die Komponente, die aus Analyse und Kontext eine für den Nutzer verständliche Antwort erzeugt.

## a.10 Verwendung einer JSON-Konfigurationsdatei

Die Datei `chatbot_config.json` wurde verwendet, um Konfiguration und Programmlogik voneinander zu trennen.

Diese Entscheidung wurde bewusst getroffen, weil ein Chatbot nicht nur aus Programmcode besteht, sondern auch aus konfigurierbaren Elementen wie Intents, Schlüsselwörtern, Standardantworten, Rückfragen und kontrollierten Listen.

In dieser Implementierung enthält die JSON-Datei:

- bekannte Filme
- Intents
- Schlüsselwörter
- Standardantworten
- Prompts für fehlende Informationen
- Fallback-Antwort

**Tabelle 5: Zweck der JSON-Konfiguration**

| Bereich in `chatbot_config.json` | Zweck |
|---|---|
| `known_movies` | Liste bekannter Filme für die Entity-Extraktion |
| `intents` | Definition der Intents, Schlüsselwörter und Standardantworten |
| `prompts` | Rückfragen für fehlende Buchungsinformationen |
| `fallback_response` | Standardantwort bei nicht verstandener Eingabe |

Beispiel:

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

Die Nutzung einer separaten JSON-Datei bietet mehrere Vorteile:

1. Die Intents, Schlüsselwörter und Standardantworten können angepasst werden, ohne den Python-Code zu verändern.
2. Die Programmlogik in `chatbot.py` bleibt übersichtlicher.
3. Die Konfiguration ist leichter nachvollziehbar und wartbar.
4. Neue Schlüsselwörter oder Filme können ergänzt werden, ohne die Kernlogik des Chatbots umzuschreiben.
5. Die Lösung zeigt eine klare Trennung zwischen Daten, Konfiguration und Verarbeitung.

Die JSON-Datei ist damit kein zwingend notwendiger Bestandteil für einen sehr kleinen Chatbot, verbessert aber die Struktur, Wartbarkeit und Erweiterbarkeit der Lösung deutlich. Aus diesem Grund wurde sie in dieser Implementierung verwendet.

---

# b) Intent-Recognition-Funktion

## b.1 Funktion der Intent Recognition

Die Intent Recognition ist in der Methode `recognize_intent()` in der Datei `chatbot.py` implementiert.

Die Aufgabe dieser Funktion ist es, aus einer Benutzereingabe den wahrscheinlich passenden Intent zu bestimmen. Der Intent beschreibt die Absicht des Nutzers, also zum Beispiel, ob der Nutzer eine Kinoticket-Buchung starten, Informationen liefern, die Buchung bestätigen, den Vorgang abbrechen oder Hilfe erhalten möchte.

Die Intent Recognition ist damit eine zentrale Komponente des Chatbots. Ohne sie könnte das System nicht unterscheiden, ob eine Eingabe wie „Hallo“, „Ich möchte Tickets buchen“, „Ja, das passt“ oder „Abbrechen“ unterschiedliche Bedeutungen hat.

## b.2 Input und Output der Funktion

Die Funktion `recognize_intent()` erhält als Input einen String mit der Benutzereingabe.

Beispiel-Input:

```python
"Ich möchte Kinotickets buchen."
```

Die Funktion gibt als Output einen String mit dem erkannten Intent zurück.

Beispiel-Output:

```python
"booking_request"
```

**Tabelle 6: Input und Output der Intent-Recognition-Funktion**

| Element | Beschreibung | Beispiel |
|---|---|---|
| Input | Benutzereingabetext als String | `"Ich möchte Kinotickets buchen."` |
| Verarbeitung | Keyword-Vergleich mit vordefinierten Intents | `"tickets"` → `booking_request` |
| Output | Erkannter Intent als String | `"booking_request"` |

## b.3 Auswahl der Schlüsselwörter

Die Schlüsselwörter wurden so ausgewählt, dass sie typische Formulierungen in einer Kinoticket-Buchung abdecken.

Für den Intent `booking_request` wurden Wörter gewählt, die häufig auftreten, wenn ein Nutzer eine Kinobuchung starten möchte:

- `ticket`
- `tickets`
- `kino`
- `film`
- `buchen`
- `buchung`
- `reservieren`
- `karte`
- `karten`

Diese Wörter decken verschiedene mögliche Ausdrucksweisen ab. Ein Nutzer kann zum Beispiel sagen:

```text
Ich möchte Kinotickets buchen.
Ich möchte Karten reservieren.
Ich will einen Film sehen.
Ich möchte ins Kino.
```

Alle diese Formulierungen deuten auf denselben Intent hin: Der Nutzer möchte eine Kinoticket-Buchung starten.

**Tabelle 7: Beispielhafte Schlüsselwörter und erkannte Intents**

| Nutzereingabe | Erkanntes Schlüsselwort | Erkannter Intent |
|---|---|---|
| `Ich möchte Kinotickets buchen.` | `tickets`, `buchen` | `booking_request` |
| `Ich möchte Karten reservieren.` | `karten`, `reservieren` | `booking_request` |
| `Hallo` | `hallo` | `greeting` |
| `Ja, das passt.` | `ja`, `passt` | `confirm_booking` |
| `Abbrechen bitte.` | `abbrechen` | `cancel` |

Die Schlüsselwörter sind bewusst einfach gewählt. Ziel ist nicht eine vollständige natürliche Sprachverarbeitung, sondern eine transparente und nachvollziehbare Intent-Erkennung.

## b.4 Konfiguration der Intents in JSON

Die Intents und Schlüsselwörter werden in `chatbot_config.json` definiert.

Ausschnitt aus `chatbot_config.json`:

```json
{
  "booking_request": {
    "_description": "Detects that the user wants to book cinema tickets.",
    "keywords": [
      "ticket",
      "tickets",
      "kino",
      "film",
      "buchen",
      "buchung",
      "reservieren",
      "karte",
      "karten"
    ],
    "response": "Gerne. Ich helfe Ihnen bei der Kinoticket-Buchung."
  }
}
```

Durch diese Struktur kann die Keyword-Liste erweitert werden, ohne die Python-Logik zu ändern. Wenn später weitere Formulierungen unterstützt werden sollen, können sie direkt in der JSON-Datei ergänzt werden.

## b.5 Python-Code der Intent Recognition

Die folgende Methode implementiert die Intent Recognition:

```python
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
```

## b.6 Erklärung des Codes

Der Code verarbeitet die Benutzereingabe in mehreren Schritten.

Zuerst wird der Text normalisiert:

```python
normalized_input = self._normalize_text(user_input)
```

Dadurch wird die Eingabe in Kleinbuchstaben umgewandelt. Das erleichtert den Vergleich mit den Schlüsselwörtern aus der JSON-Datei.

Danach wird ein leeres Dictionary `intent_scores` angelegt:

```python
intent_scores: dict[str, int] = {}
```

Dieses Dictionary speichert, wie viele Schlüsselwörter pro Intent gefunden wurden.

Anschließend werden alle Intents aus der JSON-Konfiguration durchlaufen:

```python
for intent, intent_data in self.config["intents"].items():
```

Für jeden Intent werden die dazugehörigen Keywords gelesen:

```python
keywords = intent_data.get("keywords", [])
```

Dann wird gezählt, wie viele dieser Keywords in der Nutzereingabe vorkommen:

```python
score = sum(
    1
    for keyword in keywords
    if self._contains_keyword(normalized_input, keyword)
)
```

Wenn mindestens ein Keyword gefunden wurde, wird der entsprechende Intent mit seinem Score gespeichert:

```python
if score > 0:
    intent_scores[intent] = score
```

Wenn kein Intent erkannt wird, prüft der Chatbot, ob die Eingabe trotzdem relevante Entities enthält:

```python
if not intent_scores:
    extracted_entities = self.extract_entities(user_input)

    if any(extracted_entities.values()):
        return "provide_information"
```

Das ist wichtig für kurze Antworten wie:

```text
Morgen
Um 20 Uhr
Für 2 Personen
```

Diese Eingaben enthalten keine typischen Intent-Schlüsselwörter, liefern aber wichtige Informationen für die Buchung. Deshalb werden sie als `provide_information` behandelt.

Wenn weder Keywords noch Entities gefunden werden, gibt die Funktion `fallback` zurück:

```python
return "fallback"
```

Wenn mehrere Intents gleichzeitig passen, wird eine Prioritätsliste verwendet:

```python
priority = [
    "cancel",
    "booking_request",
    "confirm_booking",
    "help",
    "greeting",
]
```

Diese Priorisierung verhindert Mehrdeutigkeiten. Wenn ein Nutzer zum Beispiel „Nein, abbrechen“ schreibt, soll der Chatbot den Vorgang abbrechen und nicht versehentlich eine andere Antwort generieren.

Am Ende wird der beste Intent zurückgegeben:

```python
return best_intent
```

## b.7 Rolle der Hilfsfunktion `_contains_keyword()`

Die Intent Recognition verwendet zusätzlich die Hilfsfunktion `_contains_keyword()`.

```python
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
```

Diese Funktion prüft, ob ein Keyword in der Nutzereingabe vorkommt. Kurze Keywords werden als vollständige Wörter geprüft, damit es nicht zu zufälligen Treffern innerhalb längerer Wörter kommt. Längere Begriffe werden als Teilstring gesucht.

Diese einfache Logik reicht für den gewählten Prototyp aus und bleibt transparent nachvollziehbar.

---

# c) Entity-Extraktionsfunktion

## c.1 Funktion der Entity-Extraktion

Die Entity-Extraktion ist in der Methode `extract_entities()` in der Datei `chatbot.py` implementiert.

Die Aufgabe dieser Funktion ist es, aus einem Benutzereingabetext konkrete Informationen zu extrahieren, die für die Kinoticket-Buchung relevant sind. Während die Intent Recognition erkennt, was der Nutzer tun möchte, erkennt die Entity-Extraktion die Details, die für die Ausführung dieser Absicht benötigt werden.

Für den gewählten Kinoticket-Buchungsassistenten sind folgende Informationen notwendig:

- Film
- Datum
- Uhrzeit
- Anzahl der Tickets beziehungsweise Personen

Beispiel:

```text
User: Ich möchte morgen um 20 Uhr Dune für 2 Personen sehen.
```

Aus dieser Eingabe sollen folgende Entities extrahiert werden:

```text
movie = Dune
date = morgen
time = 20:00
number_of_tickets = 2
```

## c.2 Input und Output der Funktion

Die Funktion `extract_entities()` erhält als Input einen String mit der Benutzereingabe.

Beispiel-Input:

```python
"Dune morgen um 20 Uhr für 2 Personen"
```

Die Funktion gibt als Output ein Dictionary zurück. Dieses Dictionary enthält die erkannten Entities. Wenn eine Entity nicht gefunden wurde, bleibt ihr Wert `None`.

Beispiel-Output:

```python
{
    "movie": "Dune",
    "date": "morgen",
    "time": "20:00",
    "number_of_tickets": "2"
}
```

**Tabelle 8: Input und Output der Entity-Extraktionsfunktion**

| Element | Beschreibung | Beispiel |
|---|---|---|
| Input | Benutzereingabetext als String | `"Dune morgen um 20 Uhr für 2 Personen"` |
| Verarbeitung | Suche nach Film, Datum, Uhrzeit und Ticketanzahl | Regex, Wortlisten, bekannte Filme |
| Output | Dictionary mit extrahierten Entities | `{"movie": "Dune", "date": "morgen", "time": "20:00", "number_of_tickets": "2"}` |

## c.3 Auswahl der Entities

Die Entities wurden so ausgewählt, dass sie den Mindestinformationen für eine einfache Kinoticket-Buchung entsprechen.

**Tabelle 9: Begründung der ausgewählten Entities**

| Entity | Grund für die Auswahl |
|---|---|
| `movie` | Ohne Film kann keine konkrete Kinobuchung vorbereitet werden. |
| `date` | Das Datum ist notwendig, um die gewünschte Vorstellung einzugrenzen. |
| `time` | Die Uhrzeit ist notwendig, um eine konkrete Vorstellung zu bestimmen. |
| `number_of_tickets` | Die Ticketanzahl ist notwendig, um die Buchungsanfrage abzuschließen. |

Diese Entities bilden zusammen den Kern des Buchungsprozesses. Sobald alle vier Informationen vorhanden sind, kann der Chatbot eine vollständige Zusammenfassung der Buchung erzeugen und den Nutzer um Bestätigung bitten.

## c.4 Python-Code der Entity-Extraktion

Die folgende Methode implementiert die Entity-Extraktion:

```python
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
```

## c.5 Erklärung des Codes

Die Funktion beginnt mit der Normalisierung der Nutzereingabe:

```python
normalized_input = self._normalize_text(user_input)
```

Dadurch wird der Eingabetext in Kleinbuchstaben umgewandelt und für die weitere Verarbeitung vorbereitet.

Anschließend wird ein Dictionary mit allen erwarteten Entities angelegt:

```python
entities: dict[str, str | None] = {
    "movie": None,
    "date": None,
    "time": None,
    "number_of_tickets": None,
}
```

Dieses Dictionary ist die zentrale Rückgabe der Funktion. Zu Beginn sind alle Werte `None`, weil noch keine Information extrahiert wurde.

## c.6 Extraktion des Films

Der Film wird mithilfe einer kontrollierten Liste bekannter Filme aus `chatbot_config.json` erkannt:

```python
for movie in self.config.get("known_movies", []):
    if movie.lower() in normalized_input:
        entities["movie"] = movie
        break
```

Die kontrollierte Liste verhindert, dass beliebige Wörter fälschlicherweise als Filmtitel interpretiert werden. Für diesen einfachen Prototyp ist das ausreichend, weil nur eine kleine Auswahl bekannter Filme unterstützt wird.

Beispiel:

```text
User: Für Dune
→ movie = Dune
```

## c.7 Extraktion des Datums

Für numerische Datumsangaben wird ein regulärer Ausdruck verwendet:

```python
date_match = re.search(r"\b(\d{1,2}\.\d{1,2}\.?\d{0,4})\b", normalized_input)
```

Dieser Ausdruck erkennt einfache Datumsformate wie:

```text
15.07.
15.07.2026
```

Wenn ein numerisches Datum gefunden wird, wird es gespeichert:

```python
if date_match:
    entities["date"] = date_match.group(1)
```

Wenn kein numerisches Datum gefunden wird, prüft der Chatbot relative Datumsangaben und Wochentage:

```python
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
```

Beispiel:

```text
User: Morgen
→ date = morgen
```

## c.8 Extraktion der Uhrzeit

Für Uhrzeiten mit Minuten wird ein regulärer Ausdruck verwendet:

```python
time_match = re.search(r"\b([01]?\d|2[0-3])[:.]([0-5]\d)\b", normalized_input)
```

Dieser Ausdruck erkennt zum Beispiel:

```text
18:30
18.30
```

Wenn eine solche Uhrzeit gefunden wird, wird sie in ein einheitliches Format gebracht:

```python
entities["time"] = f"{hour:02d}:{minute:02d}"
```

Wenn keine Uhrzeit mit Minuten gefunden wird, sucht der Chatbot nach Formulierungen wie `20 Uhr`:

```python
hour_match = re.search(r"\b([01]?\d|2[0-3])\s*uhr\b", normalized_input)
```

Beispiel:

```text
User: Um 20 Uhr
→ time = 20:00
```

Dadurch werden verschiedene einfache Schreibweisen unterstützt und in ein konsistentes Zeitformat überführt.

## c.9 Extraktion der Ticketanzahl

Für numerische Angaben wird ein regulärer Ausdruck verwendet:

```python
ticket_match = re.search(
    r"\b(?:für|mit)?\s*(\d{1,2})\s*"
    r"(tickets|ticket|karten|karte|personen|person|gäste|gaeste|gast|leute)\b",
    normalized_input,
)
```

Dieser Ausdruck erkennt Formulierungen wie:

```text
2 Tickets
für 2 Personen
mit 3 Gästen
```

Wenn eine Zahl gefunden wird, wird sie als `number_of_tickets` gespeichert:

```python
entities["number_of_tickets"] = ticket_match.group(1)
```

Zusätzlich unterstützt der Chatbot ausgeschriebene Zahlen:

```python
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
```

Beispiel:

```text
User: Drei Tickets
→ number_of_tickets = 3
```

## c.10 Rückgabe der extrahierten Entities

Am Ende gibt die Funktion das vollständige Entity-Dictionary zurück:

```python
return entities
```

Beispiel:

```python
{
    "movie": "Dune",
    "date": "morgen",
    "time": "20:00",
    "number_of_tickets": "2"
}
```

Wenn einzelne Informationen fehlen, bleiben sie auf `None`.

Beispiel:

```python
{
    "movie": "Dune",
    "date": None,
    "time": None,
    "number_of_tickets": None
}
```

Diese Struktur ist wichtig für die Kontextverwaltung. Der Chatbot kann dadurch erkennen, welche Informationen bereits vorhanden sind und welche noch abgefragt werden müssen.

## c.11 Bedeutung der Entity-Extraktion für den Buchungsdialog

Die Entity-Extraktion ermöglicht es dem Chatbot, kurze und natürliche Nutzereingaben sinnvoll zu interpretieren.

Beispielhafte Eingaben:

```text
Morgen
Um 20 Uhr
Für 2 Personen
Dune
```

Diese Nachrichten enthalten nicht immer vollständige Sätze oder klare Intents. Trotzdem liefern sie wichtige Informationen für die Buchung. Durch die Entity-Extraktion kann der Chatbot diese Informationen erkennen, im Kontext speichern und den Dialog fortsetzen.

Dadurch wird aus mehreren kurzen Einzeleingaben eine zusammenhängende Konversation.

---

# d) Kontextverwaltungssystem

## d.1 Funktion der Kontextverwaltung

Das Kontextverwaltungssystem ist im Chatbot über das Attribut `self.context` implementiert.

Die Aufgabe der Kontextverwaltung ist es, den aktuellen Zustand der Konversation zu speichern und bei jeder neuen Benutzereingabe zu aktualisieren. Dadurch kann der Chatbot bereits genannte Informationen wiederverwenden und gezielt nach fehlenden Angaben fragen.

Für den Kinoticket-Buchungsassistenten ist diese Komponente besonders wichtig, weil der Nutzer die benötigten Informationen häufig über mehrere Nachrichten verteilt nennt.

Beispiel:

```text
User: Ich möchte Kinotickets buchen.
Bot: Für welchen Film möchten Sie Tickets buchen?

User: Für Dune
Bot: Für welches Datum möchten Sie buchen?

User: Morgen
Bot: Zu welcher Uhrzeit möchten Sie den Film sehen?
```

Der Chatbot muss sich in diesem Beispiel merken, dass bereits eine Buchung gestartet wurde und dass der Film `Dune` genannt wurde. Ohne Kontextverwaltung müsste der Nutzer alle Informationen erneut eingeben.

## d.2 Gespeicherte Kontextinformationen

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

**Tabelle 10: Elemente des Kontext-Dictionaries**

| Kontextfeld | Bedeutung |
|---|---|
| `state` | Aktueller Gesprächszustand, z. B. `start`, `collecting_booking` oder `completed` |
| `last_intent` | Zuletzt erkannter Intent |
| `booking.movie` | Gespeicherter Film |
| `booking.date` | Gespeichertes Datum |
| `booking.time` | Gespeicherte Uhrzeit |
| `booking.number_of_tickets` | Gespeicherte Ticketanzahl |

## d.3 Input und Output der Kontextverwaltung

Die Kontextverwaltung arbeitet nicht als einzelne isolierte Funktion, sondern als Zusammenspiel mehrerer Methoden.

**Tabelle 11: Input und Output der Kontextverwaltung**

| Methode | Input | Output / Wirkung |
|---|---|---|
| `_create_initial_context()` | Kein externer Input | Erstellt den Anfangskontext |
| `update_context(intent, entities)` | Erkannter Intent und extrahierte Entities | Aktualisiert `self.context` |
| `_missing_booking_fields()` | Aktueller Kontext | Liste der fehlenden Buchungsfelder |
| `_next_question()` | Aktueller Kontext | Passende Rückfrage oder Zusammenfassung |
| `_booking_summary()` | Aktueller Kontext | Zusammenfassung der Buchungsdaten |
| `generate_response(intent)` | Erkannter Intent und gespeicherter Kontext | Kontextabhängige Antwort |

Der Input für die Kontextaktualisierung besteht aus zwei Informationen:

```python
intent
entities
```

Beispiel:

```python
intent = "provide_information"

entities = {
    "movie": "Dune",
    "date": None,
    "time": None,
    "number_of_tickets": None
}
```

Die Wirkung ist, dass der Kontext aktualisiert wird:

```python
self.context["booking"]["movie"] = "Dune"
```

## d.4 Python-Code: Erstellung des Anfangskontexts

Die Methode `_create_initial_context()` erstellt den Anfangszustand des Chatbots.

```python
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
```

Diese Methode wird beim Start des Chatbots im Konstruktor aufgerufen:

```python
self.context = self._create_initial_context()
```

Dadurch beginnt jede neue Chatbot-Sitzung mit einem leeren Kontext. Alle Buchungsinformationen sind zunächst `None`.

## d.5 Python-Code: Aktualisierung des Kontexts

Die Methode `update_context()` aktualisiert den Kontext nach jeder Benutzereingabe.

```python
def update_context(self, intent: str, entities: dict[str, str | None]) -> None:
    # Update the conversation context with the latest intent and entities.

    self.context["last_intent"] = intent

    for entity_name, entity_value in entities.items():
        if entity_value:
            self.context["booking"][entity_name] = entity_value
```

Die Methode erhält zwei Inputs:

```python
intent
entities
```

Der erkannte Intent wird gespeichert:

```python
self.context["last_intent"] = intent
```

Danach werden alle extrahierten Entities geprüft. Wenn eine Entity einen Wert enthält, wird sie in `self.context["booking"]` gespeichert:

```python
if entity_value:
    self.context["booking"][entity_name] = entity_value
```

Beispiel:

```python
entities = {
    "movie": "Dune",
    "date": None,
    "time": None,
    "number_of_tickets": None
}
```

führt zu:

```python
self.context["booking"]["movie"] = "Dune"
```

Werte, die `None` sind, überschreiben den bestehenden Kontext nicht. Dadurch gehen bereits gespeicherte Informationen nicht verloren.

## d.6 Python-Code: Ermittlung fehlender Buchungsfelder

Die Methode `_missing_booking_fields()` prüft, welche Informationen noch fehlen.

```python
def _missing_booking_fields(self) -> list[str]:
    # Return all booking fields that are still missing.

    booking = self.context["booking"]

    return [
        field
        for field, value in booking.items()
        if value is None
    ]
```

Diese Methode liest den aktuellen Buchungskontext und gibt eine Liste der Felder zurück, deren Wert noch `None` ist.

Beispiel:

```python
{
    "movie": "Dune",
    "date": "morgen",
    "time": None,
    "number_of_tickets": None
}
```

führt zu:

```python
["time", "number_of_tickets"]
```

Diese Liste wird anschließend verwendet, um die nächste passende Rückfrage zu erzeugen.

## d.7 Python-Code: Auswahl der nächsten Rückfrage

Die Methode `_next_question()` entscheidet anhand des Kontexts, welche Frage als Nächstes gestellt werden soll.

```python
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
```

Die Methode fragt die fehlenden Informationen in einer festen Reihenfolge ab:

1. Film
2. Datum
3. Uhrzeit
4. Anzahl der Tickets

Wenn alle Informationen vorhanden sind, wird keine weitere Detailfrage gestellt. Stattdessen wird eine Zusammenfassung erzeugt und der Nutzer wird um Bestätigung gebeten.

Beispiel:

```text
Ich habe folgende Buchungsdaten verstanden: Film: Dune, Datum: morgen, Uhrzeit: 20:00, Tickets: 2. Soll ich die Buchung bestätigen?
```

## d.8 Python-Code: Zusammenfassung der Buchung

Die Methode `_booking_summary()` erstellt eine kompakte Zusammenfassung der gespeicherten Buchungsdaten.

```python
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
```

Diese Methode liest die gespeicherten Werte aus dem Kontext und erzeugt daraus eine verständliche Antwort.

Beispielausgabe:

```text
Ich habe folgende Buchungsdaten verstanden: Film: Dune, Datum: morgen, Uhrzeit: 20:00, Tickets: 2.
```

## d.9 Python-Code: Kontextabhängige Antwortgenerierung

Die Methode `generate_response()` verbindet Intent, Kontext und Antwortlogik.

```python
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
```

Diese Methode entscheidet, welche Antwort der Chatbot erzeugt.

Wenn der Nutzer abbrechen möchte, wird der Kontext zurückgesetzt:

```python
if intent == "cancel":
    self.reset_context()
```

Wenn der Nutzer eine Buchung startet, wird der Gesprächszustand auf `collecting_booking` gesetzt:

```python
if intent == "booking_request":
    self.context["state"] = "collecting_booking"
    return self._next_question()
```

Wenn der Nutzer Informationen liefert, bleibt der Bot im Buchungsprozess und stellt die nächste passende Frage:

```python
if intent == "provide_information":
    if self.context["state"] == "start":
        self.context["state"] = "collecting_booking"

    return self._next_question()
```

Wenn der Nutzer die Buchung bestätigt, prüft der Bot zuerst, ob noch Informationen fehlen:

```python
if self._missing_booking_fields():
```

Falls Informationen fehlen, fragt der Bot weiter nach. Falls alle Informationen vorhanden sind, wird der Zustand auf `completed` gesetzt und die Buchung wird zusammengefasst.

## d.10 Verarbeitungskette im Code

Die zentrale Methode `process_input()` verbindet alle Komponenten.

```python
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
```

Diese Methode zeigt die komplette Verarbeitungskette:

1. Intent erkennen
2. Entities extrahieren
3. Kontext aktualisieren
4. Antwort generieren

Damit wird sichtbar, wie die einzelnen Komponenten zusammenarbeiten.

## d.11 Beispiel für kontextabhängige Verarbeitung

Beispielhafte Konversation:

```text
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
```

Nach jeder Nutzereingabe wird der Kontext erweitert. Der Chatbot erkennt, welche Informationen bereits vorhanden sind, und fragt nur nach den noch fehlenden Angaben. Dadurch entsteht eine kohärente, mehrstufige Konversation.

---

# Ausführung

## Zweck der drei Ausführungsmodi

Der Chatbot kann auf drei Arten ausgeführt werden:

1. Demo-Modus
2. Interaktiver Modus
3. Selbsttest-Modus

Diese drei Modi wurden implementiert, um unterschiedliche Prüf- und Nutzungssituationen abzudecken.

**Tabelle 12: Ausführungsmodi des Chatbots**

| Modus | Befehl | Zweck |
|---|---|---|
| Demo-Modus | `python chatbot.py --demo` | Führt eine vorbereitete Beispielkonversation aus |
| Interaktiver Modus | `python chatbot.py --interactive` | Ermöglicht eine eigene manuelle Unterhaltung mit dem Chatbot |
| Selbsttest-Modus | `python chatbot.py --self-test` | Prüft automatisch zentrale Funktionen des Chatbots |

Der Demo-Modus zeigt schnell, wie der Chatbot grundsätzlich funktioniert. Der interaktive Modus ermöglicht eigene Eingaben und damit eine manuelle Prüfung der Dialogfähigkeit. Der Selbsttest-Modus prüft automatisch, ob Intent Recognition, Entity Extraction, Kontextaktualisierung und finale Bestätigung funktionieren.

## Demo-Konversation starten

Der Demo-Modus führt eine fest definierte Beispielkonversation aus.

```bash
python chatbot.py --demo
```

Dieser Modus ist nützlich, um den Ablauf des Chatbots schnell zu demonstrieren, ohne selbst Eingaben machen zu müssen.

## Interaktiven Modus starten

Der interaktive Modus erlaubt es, direkt mit dem Chatbot zu schreiben.

```bash
python chatbot.py --interactive
```

Nach dem Start erscheint eine Eingabeaufforderung:

```text
User:
```

Dort können eigene Nachrichten eingegeben werden.

Beispiel für eine vollständige Testkonversation:

```text
Hallo
Ich möchte Kinotickets buchen
Für Dune
Morgen
Um 20 Uhr
Für 2 Personen
Ja, das passt
```

Der Chatbot antwortet nach jeder Eingabe und speichert den Kontext während der laufenden Unterhaltung.

Um den interaktiven Modus zu beenden, muss folgendes eingegeben werden:

```text
exit
```

Alternativ kann auch verwendet werden:

```text
quit
```

Danach beendet der Chatbot die Unterhaltung mit:

```text
Bot: Auf Wiedersehen!
```

## Selbsttests ausführen

Der Selbsttest-Modus prüft automatisch zentrale Funktionen der Implementierung.

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

Der Selbsttest-Modus ist hilfreich, um nach Änderungen am Code schnell zu prüfen, ob die wichtigsten Funktionen weiterhin korrekt arbeiten.

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

# Hinweis zur Abgabe

Die Abgabe erfolgt als ZIP-Archiv mit dem Namen:

```text
Angie_Angarita_Soto_Teilprüfung 1.zip
```

Das Archiv befindet sich im Ordner `submission/`.

Es enthält die folgenden Dateien:

```text
README.md
chatbot.py
chatbot_config.json
beispiel_dialog.txt
requirements.txt
```

Die enthaltenen Dateitypen entsprechen den Vorgaben: `.md`, `.py`, `.json` und `.txt`.

---

# Reflexion und Fazit

Die Umsetzung des AI-basierten Chatbots zeigt, wie die Grundbausteine eines einfachen dialogbasierten Systems in Python nachvollziehbar implementiert werden können. Besonders deutlich wurde dabei, dass ein Chatbot nicht nur aus einzelnen Antworten besteht, sondern aus mehreren zusammenwirkenden Komponenten: Intent Recognition, Entity-Extraktion, Kontextverwaltung und Antwortgenerierung.

Der gewählte Anwendungsfall der Kinoticket-Buchung war für diese Umsetzung gut geeignet, weil er einen klaren, mehrstufigen Dialogablauf besitzt. Der Nutzer muss mehrere Informationen angeben, zum Beispiel Film, Datum, Uhrzeit und Anzahl der Tickets. Dadurch konnte gezeigt werden, warum Kontextverwaltung wichtig ist. Ohne gespeicherten Kontext müsste der Nutzer alle Informationen in jeder Nachricht erneut angeben. Mit Kontextverwaltung kann der Chatbot bereits genannte Informationen behalten und gezielt nach fehlenden Angaben fragen.

Die einfache keyword-basierte Intent Recognition erfüllt in diesem Projekt den Zweck, grundlegende Absichten des Nutzers transparent zu erkennen. Gleichzeitig wurde deutlich, dass dieser Ansatz Grenzen hat. Er funktioniert gut, solange Nutzereingaben vorhersehbar sind und die relevanten Schlüsselwörter enthalten. Bei freieren Formulierungen, Tippfehlern oder komplexeren Anfragen wäre eine rein keyword-basierte Lösung jedoch eingeschränkt.

Auch die Entity-Extraktion wurde bewusst einfach umgesetzt. Reguläre Ausdrücke und kontrollierte Wortlisten eignen sich gut, um klar erkennbare Angaben wie `20 Uhr`, `morgen` oder `2 Personen` zu extrahieren. Für komplexere Sprache, unbekannte Filmtitel oder mehrdeutige Aussagen wäre eine robustere Sprachverarbeitung erforderlich.

Die Trennung von Programmlogik und Konfiguration über `chatbot_config.json` hat sich als sinnvoll erwiesen. Intents, Schlüsselwörter, Prompts und bekannte Filme können dadurch angepasst werden, ohne den Python-Code selbst zu verändern. Diese Struktur verbessert die Wartbarkeit und macht die Lösung übersichtlicher.

Aus heutiger Sicht zeigt diese Implementierung eine klassische und didaktisch gut nachvollziehbare Chatbot-Architektur. Für produktive Systeme würden jedoch moderne Verfahren ergänzt werden, zum Beispiel:

- semantisches Routing mit Embeddings
- LLM-basierte Intent-Erkennung
- Tool Calling
- Retrieval-Augmented Generation für Wissenszugriff
- Guardrails
- Evaluation und Monitoring

Zusammenfassend zeigt die Teilprüfung, dass klassische Chatbot-Konzepte weiterhin eine wichtige Grundlage für das Verständnis dialogbasierter KI-Systeme bilden. Auch moderne LLM- und Agentensysteme benötigen weiterhin Konzepte wie Absichtserkennung, Kontext, strukturierte Eingaben, Antwortlogik und Qualitätskontrolle. Die praktische Umsetzung mit Python, JSON, Git und GitHub verdeutlicht außerdem, wie solche KI-Artefakte strukturiert, versioniert und reproduzierbar dokumentiert werden können.
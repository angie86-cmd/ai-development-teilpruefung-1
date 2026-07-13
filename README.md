# AI-basierter Chatbot - Teilprüfung 1

Dieses Projekt enthält eine einfache Python-Implementierung eines AI-basierten Chatbots für eine Kinoticket-Buchung.

Der Chatbot ist in der Lage, einfache Konversationen zu führen, Benutzeranfragen anhand von Intents zu erkennen, relevante Entities aus der Eingabe zu extrahieren und den Kontext über mehrere Nachrichten hinweg zu speichern.

## Einleitung

Im Rahmen dieser Teilprüfung wurde ein einfacher AI-basierter Chatbot in Python entwickelt. Der Chatbot demonstriert grundlegende Konzepte der Chatbot-Entwicklung, insbesondere Intent Recognition, Entity-Extraktion und Kontextverwaltung.

Als Anwendungsfall wurde bewusst eine Kinoticket-Buchung gewählt. Der Chatbot unterstützt den Nutzer dabei, eine einfache Buchungsanfrage vorzubereiten. Dafür sammelt er über mehrere Nachrichten hinweg die relevanten Informationen: Film, Datum, Uhrzeit und Anzahl der Tickets beziehungsweise Personen.

Die Projektdateien wurden in einem separaten GitHub-Repository erstellt und versioniert:

```text
https://github.com/angie86-cmd/ai-development-teilpruefung-1
```

Das Repository dient der strukturierten Dokumentation der Umsetzung. Durch die Nutzung von Git und GitHub ist nachvollziehbar, welche Dateien erstellt wurden und wie sich die Implementierung entwickelt hat. Dadurch wird die Lösung reproduzierbar, wartbar und transparent dokumentiert.

Die eigentliche Abgabe für die Teilprüfung erfolgt zusätzlich als ZIP-Archiv gemäß den Vorgaben der Aufgabenstellung. Das ZIP-Archiv befindet sich im Ordner `submission/` und enthält ausschließlich erlaubte Dateitypen wie `.md`, `.py`, `.json` und `.txt`.

Die Umsetzung trennt bewusst Dokumentation, Programmlogik, Konfiguration und Beispieldialog:

- `README.md` dokumentiert Architektur, Vorgehensweise und Umsetzung.
- `chatbot.py` enthält die Python-Implementierung des Chatbots.
- `chatbot_config.json` enthält Intents, Schlüsselwörter, Standardantworten und Prompts.
- `beispiel_dialog.txt` zeigt eine beispielhafte Konversation.
- `requirements.txt` dokumentiert die technischen Voraussetzungen.

Diese Struktur wurde gewählt, um die Lösung übersichtlich und nachvollziehbar zu halten. Gleichzeitig zeigt sie eine saubere Trennung zwischen Konfiguration und Programmlogik, was die Wartbarkeit des Chatbots verbessert.

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

## Dateien und Repository-Struktur

Die Projektdateien sind im GitHub-Repository `ai-development-teilpruefung-1` versioniert.

**Tabelle 1: Dateien und Zweck im Projekt**

| Datei | Zweck |
|---|---|
| `README.md` | Dokumentation der Architektur, Komponenten und Umsetzungsschritte |
| `chatbot.py` | Python-Implementierung des Chatbots |
| `chatbot_config.json` | Konfiguration der Intents, Schlüsselwörter, Antworten und Prompts |
| `beispiel_dialog.txt` | Beispielhafte Konversation zur Demonstration der Kontextverwaltung |
| `requirements.txt` | Technische Voraussetzungen |
| `.gitignore` | Ausschluss technischer Hilfsdateien aus der Versionskontrolle |
| `submission/Angie_Angarita_Soto_Teilprüfung 1.zip` | ZIP-Datei für die Abgabe |

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

Die Versionskontrolle über GitHub wurde verwendet, um die Entwicklung nachvollziehbar zu dokumentieren. Dadurch kann der aktuelle Stand der Implementierung jederzeit überprüft, geteilt und bei Bedarf weiterentwickelt werden.

---

# a) Grundlegende Architektur des Chatbots

## a.1 Architekturüberblick

Die Architektur des Chatbots besteht aus mehreren klar getrennten Komponenten. Ziel dieser Struktur ist es, die Verarbeitungsschritte nachvollziehbar und wartbar zu gestalten.

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

## a.2 Begründung der gewählten Architektur

Diese Architektur wurde gewählt, weil sie die zentralen Anforderungen der Teilprüfung direkt abbildet:

1. Der Chatbot soll Benutzeranfragen anhand von Intents erkennen.
2. Der Chatbot soll relevante Entities aus dem Text extrahieren.
3. Der Chatbot soll Kontext über mehrere Nachrichten hinweg speichern.
4. Der Chatbot soll kontextabhängige Antworten generieren.

Die Architektur ist bewusst modular aufgebaut. Dadurch kann jede Komponente separat erklärt, getestet und bei Bedarf erweitert werden.

Ein weiterer Grund für diese Architektur ist die Transparenz. Da es sich um eine Teilprüfung handelt, soll nachvollziehbar sein, wie eine Eingabe verarbeitet wird und warum der Chatbot eine bestimmte Antwort gibt. Eine einfache, komponentenbasierte Struktur eignet sich dafür besser als eine schwer nachvollziehbare Black-Box-Lösung.

**Tabelle 2: Komponenten der Chatbot-Architektur**

| Komponente | Aufgabe | Umsetzung im Projekt |
|---|---|---|
| Input Processing | Vorbereitung der Nutzereingabe | Normalisierung in Kleinbuchstaben und Entfernen überflüssiger Leerzeichen |
| Intent Recognition | Erkennung der Nutzerabsicht | Keyword-Mapping aus `chatbot_config.json` |
| Entity Extraction | Extraktion relevanter Informationen | Reguläre Ausdrücke, Wortlisten und bekannte Filmtitel |
| Context Management | Speicherung des Konversationszustands | Python-Dictionary `self.context` |
| Response Generation | Erzeugung passender Antworten | Kombination aus Intent, Entities und Kontext |

## a.3 Zusammenspiel der Komponenten

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

## a.4 Input Processing

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

## a.5 Intent Recognition

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

## a.6 Entity-Extraktion

Die Entity-Extraktion erkennt konkrete Informationen innerhalb der Benutzereingabe.

In dieser Implementierung werden folgende Entities extrahiert:

**Tabelle 4: Implementierte Entities**

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

## a.7 Context Management

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

## a.8 Response Generation

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

## a.9 Verwendung einer JSON-Konfigurationsdatei

Die Datei `chatbot_config.json` wurde verwendet, um Konfiguration und Programmlogik voneinander zu trennen.

Diese Entscheidung hat mehrere Vorteile:

1. Die Intents, Schlüsselwörter und Standardantworten können angepasst werden, ohne den Python-Code zu verändern.
2. Die Programmlogik in `chatbot.py` bleibt übersichtlicher.
3. Die Konfiguration ist leichter nachvollziehbar und wartbar.
4. Neue Schlüsselwörter oder Filme können ergänzt werden, ohne die Kernlogik des Chatbots umzuschreiben.
5. Die Lösung zeigt eine klare Trennung zwischen Daten, Konfiguration und Verarbeitung.

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

Die JSON-Datei ist damit kein zwingend notwendiger Bestandteil für einen sehr kleinen Chatbot, verbessert aber die Struktur und Wartbarkeit der Lösung deutlich. Aus diesem Grund wurde sie in dieser Implementierung verwendet.

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

Die Implementierung ist bewusst einfach und transparent gehalten. Sie erfüllt damit die Anforderung, eine einfache Intent-Recognition-Funktion auf Basis vordefinierter Intents und eines Schlüsselwort-Mappings zu verwenden.

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

Die Kontextverwaltung ermöglicht dadurch eine einfache mehrstufige Konversation. Der Chatbot behandelt die Nachrichten nicht isoliert, sondern nutzt die bereits gespeicherten Informationen, um sinnvolle Rückfragen und Antworten zu generieren.

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

Die enthaltenen Dateitypen entsprechen den Vorgaben der Teilprüfung: `.md`, `.py`, `.json` und `.txt`.

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
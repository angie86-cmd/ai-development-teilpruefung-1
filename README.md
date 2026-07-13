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

Im Rahmen dieser Teilprüfung wurde ein einfacher AI-basierter Chatbot in Python entwickelt. Der Chatbot demonstriert grundlegende Konzepte der Chatbot-Entwicklung, insbesondere Intent Recognition, Entity-Extraktion und Kontextverwaltung.

Als Anwendungsfall wurde bewusst eine Kinoticket-Buchung gewählt. Der Chatbot unterstützt den Nutzer dabei, eine einfache Buchungsanfrage vorzubereiten. Dafür sammelt er über mehrere Nachrichten hinweg die relevanten Informationen: Film, Datum, Uhrzeit und Anzahl der Tickets beziehungsweise Personen.

Der Anwendungsfall wurde gewählt, weil er einfach genug ist, um die geforderten Grundkonzepte transparent zu zeigen, aber gleichzeitig mehrere typische Chatbot-Komponenten benötigt. Eine Kinoticket-Buchung erfordert die Erkennung einer Nutzerabsicht, die Extraktion konkreter Informationen und die Speicherung des Gesprächskontexts über mehrere Nachrichten hinweg.

Die Projektdateien wurden in einem separaten GitHub-Repository erstellt und versioniert:

```text
https://github.com/angie86-cmd/ai-development-teilpruefung-1
```

Das Repository dient der strukturierten Dokumentation der Umsetzung. Durch die Nutzung von Git und GitHub ist nachvollziehbar, welche Dateien erstellt wurden und wie sich die Implementierung entwickelt hat. Dadurch wird die Lösung reproduzierbar, wartbar und transparent dokumentiert.

Die eigentliche Abgabe für die Teilprüfung erfolgt zusätzlich als ZIP-Archiv gemäß den Vorgaben der Aufgabenstellung. Das ZIP-Archiv befindet sich im Ordner `submission/` und enthält ausschließlich erlaubte Dateitypen wie `.md`, `.py`, `.json` und `.txt`.

Die Umsetzung trennt bewusst Dokumentation, Programmlogik, Konfiguration und Beispieldialog:

- `README.md` dokumentiert Aufgabe, Architektur, Vorgehensweise und Umsetzung.
- `chatbot.py` enthält die Python-Implementierung des Chatbots.
- `chatbot_config.json` enthält Intents, Schlüsselwörter, Standardantworten und Prompts.
- `beispiel_dialog.txt` zeigt eine beispielhafte Konversation.
- `requirements.txt` dokumentiert die technischen Voraussetzungen.

Diese Struktur wurde gewählt, um die Lösung übersichtlich und nachvollziehbar zu halten. Gleichzeitig zeigt sie eine saubere Trennung zwischen Konfiguration und Programmlogik, was die Wartbarkeit des Chatbots verbessert.

## Projektstruktur und Versionierung

Für die Umsetzung wurde eine übersichtliche Projektstruktur erstellt, die die verschiedenen Bestandteile der Teilprüfung voneinander trennt. Dadurch bleibt nachvollziehbar, welche Dateien für die Implementierung, die Konfiguration, den Beispieldialog und die finale Abgabe verwendet wurden.

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

Die grundlegende Architektur des Chatbots wurde so entworfen, dass die geforderten Bestandteile der Teilprüfung klar abgebildet werden:

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

Diese Architektur wurde gewählt, weil sie die Anforderungen der Teilprüfung direkt und nachvollziehbar erfüllt.

Erstens ermöglicht die Trennung zwischen Intent Recognition und Entity-Extraktion eine klare Unterscheidung zwischen der Absicht des Nutzers und den konkreten Informationen innerhalb der Eingabe. Der Intent beschreibt, was der Nutzer erreichen möchte, während die Entities die dazugehörigen Details enthalten.

Zweitens erleichtert die Kontextverwaltung eine kohärente Konversation über mehrere Nachrichten hinweg. Ohne Kontext müsste der Chatbot jede Nachricht isoliert behandeln. Mit Kontext kann er bereits gesammelte Informationen speichern und gezielt nach fehlenden Angaben fragen.

Drittens ist die Architektur modular aufgebaut. Jede Komponente kann separat erklärt, getestet und erweitert werden. Dies verbessert die Wartbarkeit und macht die Lösung für eine Teilprüfung gut nachvollziehbar.

Viertens ist die Implementierung bewusst transparent gehalten. Für diese Teilprüfung ist es wichtiger, die grundlegenden Komponenten eines Chatbots verständlich zu demonstrieren, als eine komplexe Black-Box-Lösung zu verwenden.

**Tabelle 2: Komponenten der Chatbot-Architektur**

| Komponente | Aufgabe | Umsetzung im Projekt |
|---|---|---|
| Input Processing | Vorbereitung der Nutzereingabe | Normalisierung in Kleinbuchstaben und Entfernen überflüssiger Leerzeichen |
| Intent Recognition | Erkennung der Nutzerabsicht | Keyword-Mapping aus `chatbot_config.json` |
| Entity Extraction | Extraktion relevanter Informationen | Reguläre Ausdrücke, Wortlisten und bekannte Filmtitel |
| Context Management | Speicherung des Konversationszustands | Python-Dictionary `self.context` |
| Response Generation | Erzeugung passender Antworten | Kombination aus Intent, Entities und Kontext |

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
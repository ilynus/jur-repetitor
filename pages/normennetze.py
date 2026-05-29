"""Normennetze — Strukturierte Übersichten examensrelevanter Normen und ihrer Zusammenhänge."""
from __future__ import annotations
import streamlit as st

from src.theme import apply_theme, section_header, gold_divider, page_header
from src.llm import chat_stream

apply_theme()

# ── FARB-SCHEMA nach Norm-Typ ─────────────────────────────────────────────────

TYP_FARBEN: dict[str, dict[str, str]] = {
    "Grundnorm":    {"bg": "#1a2744", "text": "#f5e4a8", "border": "#c9a84c", "label": "Grundnorm"},
    "Rechtsfolge":  {"bg": "#92400e", "text": "#fef3c7", "border": "#d97706", "label": "Rechtsfolge"},
    "Verfahren":    {"bg": "#14532d", "text": "#dcfce7", "border": "#16a34a", "label": "Verfahren"},
    "Einschränkung":{"bg": "#7f1d1d", "text": "#fee2e2", "border": "#dc2626", "label": "Einschränkung"},
    "Ergänzung":    {"bg": "#1e3a5f", "text": "#dbeafe", "border": "#3b82f6", "label": "Ergänzung"},
}

# ── NORMENNETZE-DATEN ─────────────────────────────────────────────────────────

NORMENNETZE: dict[str, dict] = {

    # ─────────────────────────────────────────────────────────────────────────
    "Anfechtung": {
        "beschreibung": (
            "Systematische Übersicht der Anfechtungstatbestände (§§ 119–124 BGB) "
            "und ihrer Rechtsfolgen (§§ 142–144 BGB). Examensrelevant für die "
            "Frage der Wirksamkeit von Willenserklärungen."
        ),
        "rechtsgebiet": "Zivilrecht",
        "icon": "📜",
        "normen": [
            {
                "norm": "§ 119 BGB",
                "titel": "Anfechtbarkeit wegen Irrtums",
                "inhalt": "Inhalts-/Erklärungsirrtum (Abs. 1); Eigenschaftsirrtum (Abs. 2). Abs. 2 nur bei verkehrswesentlichen Eigenschaften.",
                "verbindungen": ["§ 121 BGB", "§ 142 BGB", "§ 122 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__119.html",
            },
            {
                "norm": "§ 120 BGB",
                "titel": "Anfechtbarkeit wegen falscher Übermittlung",
                "inhalt": "Übermittlungsfehler durch Boten oder Einrichtungen (Telegramm etc.) – Gleichstellung mit Erklärungsirrtum.",
                "verbindungen": ["§ 119 BGB", "§ 121 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__120.html",
            },
            {
                "norm": "§ 121 BGB",
                "titel": "Anfechtungsfrist bei §§ 119, 120 BGB",
                "inhalt": "Unverzügliche Anfechtung (ohne schuldhaftes Zögern), spätestens 10 Jahre nach WE-Abgabe.",
                "verbindungen": ["§ 119 BGB", "§ 120 BGB", "§ 143 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__121.html",
            },
            {
                "norm": "§ 123 BGB",
                "titel": "Arglistige Täuschung / Drohung",
                "inhalt": "Täuschung (vorsätzlich, kausal) oder widerrechtliche Drohung. Bei Täuschung durch Dritten nur bei Kenntnis/Kennenmüssen des Erklärungsempfängers.",
                "verbindungen": ["§ 124 BGB", "§ 142 BGB", "§ 826 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__123.html",
            },
            {
                "norm": "§ 124 BGB",
                "titel": "Anfechtungsfrist bei § 123 BGB",
                "inhalt": "Jahresfrist ab Kenntnis von Täuschung/Wegfall der Zwangslage, max. 10 Jahre.",
                "verbindungen": ["§ 123 BGB", "§ 143 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__124.html",
            },
            {
                "norm": "§ 142 BGB",
                "titel": "Wirkung der Anfechtung",
                "inhalt": "Ex-tunc-Nichtigkeit des angefochtenen Rechtsgeschäfts (Abs. 1). Wer die Anfechtbarkeit kannte, wird wie ein Wissender behandelt (Abs. 2).",
                "verbindungen": ["§ 119 BGB", "§ 123 BGB", "§ 812 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__142.html",
            },
            {
                "norm": "§ 143 BGB",
                "titel": "Anfechtungserklärung",
                "inhalt": "Gegenüber Anfechtungsgegner; empfangsbedürftige WE; Anfechtungswille muss erkennbar sein (kein Formerfordernis).",
                "verbindungen": ["§ 121 BGB", "§ 124 BGB", "§ 142 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__143.html",
            },
            {
                "norm": "§ 144 BGB",
                "titel": "Bestätigung des anfechtbaren Rechtsgeschäfts",
                "inhalt": "Bestätigung schließt Anfechtungsrecht aus. Formfrei, aber Kenntnis der Anfechtbarkeit erforderlich.",
                "verbindungen": ["§ 142 BGB", "§ 143 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__144.html",
            },
            {
                "norm": "§ 122 BGB",
                "titel": "Schadensersatzpflicht des Anfechtenden",
                "inhalt": "Vertrauensschaden (negatives Interesse) gegenüber gutgläubigem Empfänger. Kein Ersatz wenn Empfänger Irrtum kannte/kennen musste.",
                "verbindungen": ["§ 119 BGB", "§ 142 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__122.html",
            },
        ],
        "schema": [
            "1. Anfechtungsgrund",
            "   a) § 119 I BGB: Inhalts- oder Erklärungsirrtum",
            "   b) § 119 II BGB: Eigenschaftsirrtum (verkehrswesentliche Eigenschaft)",
            "   c) § 120 BGB: Falscher Übermittlung",
            "   d) § 123 BGB: Arglistige Täuschung oder widerrechtliche Drohung",
            "2. Anfechtungserklärung (§ 143 BGB) — gegenüber Anfechtungsgegner",
            "3. Anfechtungsfrist",
            "   a) §§ 119, 120: unverzüglich (§ 121 BGB), max. 10 Jahre",
            "   b) § 123: 1 Jahr ab Kenntnis (§ 124 BGB), max. 10 Jahre",
            "4. Kein Ausschluss durch Bestätigung (§ 144 BGB)",
            "5. Rechtsfolge: ex-tunc-Nichtigkeit (§ 142 I BGB)",
            "   → Bereicherungsanspruch (§ 812 I 1 Alt. 1 BGB)",
            "6. Schadensersatz des Anfechtenden (§ 122 BGB) — negatives Interesse",
        ],
        "klausurfallen": [
            "Irrtum muss kausal für Abgabe der WE sein",
            "§ 119 II: nur objektiv verkehrswesentliche Eigenschaften, nicht subjektive Wertvorstellungen",
            "Bei Täuschung durch Dritten (§ 123 II): nur bei Kenntnis/Kennenmüssen des Empfängers anfechtbar",
            "Anfechtung und § 313 BGB (Wegfall der Geschäftsgrundlage): Abgrenzung im Motivirrtum",
            "§ 122 BGB: nur negatives Interesse (Vertrauensschaden), kein Erfüllungsinteresse",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Rücktritt": {
        "beschreibung": (
            "Überblick über das gesetzliche Rücktrittsrecht bei Leistungsstörungen "
            "(§§ 323–326 BGB) und die Rückgewährpflichten (§§ 346–354 BGB). "
            "Zentral im Schuldrecht AT."
        ),
        "rechtsgebiet": "Zivilrecht",
        "icon": "↩️",
        "normen": [
            {
                "norm": "§ 323 BGB",
                "titel": "Rücktritt wegen nicht oder nicht vertragsgemäß erbrachter Leistung",
                "inhalt": "Nicht-/Schlechtleistung, Fristsetzung als Grundvoraussetzung (Abs. 1). Ausnahmen von Fristsetzung in Abs. 2. Ausschluss bei beiderseitiger Unmöglichkeit (Abs. 6).",
                "verbindungen": ["§ 281 BGB", "§ 346 BGB", "§ 440 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__323.html",
            },
            {
                "norm": "§ 324 BGB",
                "titel": "Rücktritt wegen Verletzung einer Pflicht nach § 241 II BGB",
                "inhalt": "Rücktritt bei Verletzung von Rücksichtnahmepflichten wenn Festhalten am Vertrag unzumutbar.",
                "verbindungen": ["§ 241 BGB", "§ 282 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__324.html",
            },
            {
                "norm": "§ 325 BGB",
                "titel": "Schadensersatz und Rücktritt",
                "inhalt": "Nebeneinander von Rücktritt und Schadensersatz (statt der Leistung) möglich — wichtige Klarstellung.",
                "verbindungen": ["§ 280 BGB", "§ 281 BGB", "§ 346 BGB"],
                "typ": "Ergänzung",
                "link": "https://www.gesetze-im-internet.de/bgb/__325.html",
            },
            {
                "norm": "§ 326 BGB",
                "titel": "Befreiung von der Gegenleistung / Rücktritt bei Unmöglichkeit",
                "inhalt": "Bei Unmöglichkeit: Befreiung von Gegenleistung (Abs. 1); Rücktrittsrecht (Abs. 5) ohne Fristsetzung.",
                "verbindungen": ["§ 275 BGB", "§ 323 BGB", "§ 346 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__326.html",
            },
            {
                "norm": "§ 346 BGB",
                "titel": "Wirkungen des Rücktritts",
                "inhalt": "Rückgewähr empfangener Leistungen (Abs. 1). Bei Unmöglichkeit der Rückgewähr: Wertersatz (Abs. 2). Ausnahmen in Abs. 3.",
                "verbindungen": ["§ 347 BGB", "§ 348 BGB", "§ 323 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__346.html",
            },
            {
                "norm": "§ 347 BGB",
                "titel": "Nutzungen und Verwendungen nach Rücktritt",
                "inhalt": "Herausgabe/Ersatz gezogener Nutzungen. Ersatz notwendiger Verwendungen. Günstigere Regelung für Schuldner vor Rücktritt.",
                "verbindungen": ["§ 346 BGB", "§ 994 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__347.html",
            },
            {
                "norm": "§ 348 BGB",
                "titel": "Aufrechnung bei Rücktritt",
                "inhalt": "Zug-um-Zug-Rückabwicklung: Rücktrittsberechtigter kann nur Zug-um-Zug leisten.",
                "verbindungen": ["§ 346 BGB", "§ 387 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__348.html",
            },
            {
                "norm": "§ 349 BGB",
                "titel": "Rücktrittserklärung",
                "inhalt": "Empfangsbedürftige WE gegenüber dem anderen Teil; formfrei; Bedingungsfeindlichkeit beachten.",
                "verbindungen": ["§ 346 BGB", "§ 350 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__349.html",
            },
            {
                "norm": "§ 350 BGB",
                "titel": "Erlöschen des Rücktrittsrechts",
                "inhalt": "Untergang/wesentliche Verschlechterung der empfangenen Sache führt nicht mehr zum Ausschluss (seit 2002).",
                "verbindungen": ["§ 346 BGB", "§ 323 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__350.html",
            },
            {
                "norm": "§ 354 BGB",
                "titel": "Wegfall des Rücktrittsrechts (überholte Norm)",
                "inhalt": "Veraltete Regelung; heute §§ 346 III, 350 BGB maßgeblich.",
                "verbindungen": ["§ 346 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__354.html",
            },
        ],
        "schema": [
            "1. Rücktrittsrecht",
            "   a) Vertragliches Rücktrittsrecht (§ 346 I Var. 1 BGB)",
            "   b) Gesetzliches Rücktrittsrecht bei Nicht-/Schlechtleistung (§ 323 BGB)",
            "      — Fristsetzung erforderlich (Grundsatz), Ausnahmen § 323 II BGB",
            "   c) Verletzung von Schutzpflichten (§ 324 BGB)",
            "   d) Unmöglichkeit (§ 326 V BGB) — keine Fristsetzung nötig",
            "2. Rücktrittserklärung (§ 349 BGB) — empfangsbedürftige WE",
            "3. Kein Ausschluss (§§ 350, 323 VI BGB)",
            "4. Rechtsfolge: Rückgewährschuldverhältnis (§ 346 I BGB)",
            "   a) Rückgabe empfangener Leistungen",
            "   b) Herausgabe gezogener Nutzungen (§ 347 I BGB)",
            "   c) Bei Unmöglichkeit der Rückgewähr: Wertersatz (§ 346 II BGB)",
            "5. Nebeneinander mit Schadensersatz (§ 325 BGB) möglich",
        ],
        "klausurfallen": [
            "§ 323 VI BGB: Rücktritt ausgeschlossen wenn Gläubiger allein/überwiegend verantwortlich",
            "Fristsetzung: angemessene Frist — keine Nachfrist bei § 326 V BGB nötig",
            "§ 346 II: Wertersatz bei unmöglicher Rückgewähr, aber Ausnahmen in § 346 III BGB beachten",
            "§ 325 BGB: Rücktritt und Schadensersatz statt der Leistung schließen sich NICHT aus",
            "Abgrenzung: Minderung (§ 441 BGB) vs. Rücktritt beim Kaufrecht",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Schadensersatz statt Leistung": {
        "beschreibung": (
            "Die §§ 280–285 BGB regeln den Schadensersatz wegen Pflichtverletzung. "
            "§ 280 I BGB ist die Grundnorm; §§ 281–283 fügen jeweils eine weitere "
            "Voraussetzung hinzu. Examensklassiker: das Dreistufenmodell."
        ),
        "rechtsgebiet": "Zivilrecht",
        "icon": "💶",
        "normen": [
            {
                "norm": "§ 280 BGB",
                "titel": "Schadensersatz wegen Pflichtverletzung (Grundnorm)",
                "inhalt": "Abs. 1: Pflichtverletzung + Vertretenmüssen = SE. Abs. 2: Verzug nur mit § 286 BGB. Abs. 3: SE statt Leistung nur mit §§ 281, 282, 283 BGB.",
                "verbindungen": ["§ 241 BGB", "§ 281 BGB", "§ 282 BGB", "§ 283 BGB", "§ 276 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__280.html",
            },
            {
                "norm": "§ 281 BGB",
                "titel": "SE statt Leistung wegen Nicht-/Schlechtleistung",
                "inhalt": "Fristsetzung als Voraussetzung. Ausnahmen (Abs. 2). Erheblichkeitsschwelle bei Schlechtleistung (Abs. 1 S. 3).",
                "verbindungen": ["§ 280 BGB", "§ 323 BGB", "§ 286 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__281.html",
            },
            {
                "norm": "§ 282 BGB",
                "titel": "SE statt Leistung wegen Verletzung einer Schutzpflicht",
                "inhalt": "Verletzung von § 241 II BGB macht Leistung unzumutbar — SE statt Leistung ohne Fristsetzung.",
                "verbindungen": ["§ 280 BGB", "§ 241 BGB", "§ 324 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__282.html",
            },
            {
                "norm": "§ 283 BGB",
                "titel": "SE statt Leistung bei Unmöglichkeit",
                "inhalt": "Bei § 275 BGB (Unmöglichkeit): SE statt Leistung ohne Fristsetzung.",
                "verbindungen": ["§ 275 BGB", "§ 280 BGB", "§ 326 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__283.html",
            },
            {
                "norm": "§ 284 BGB",
                "titel": "Ersatz vergeblicher Aufwendungen",
                "inhalt": "Statt SE statt Leistung kann Gläubiger vergebliche Aufwendungen ersetzt verlangen (Wahlrecht).",
                "verbindungen": ["§ 281 BGB", "§ 249 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__284.html",
            },
            {
                "norm": "§ 285 BGB",
                "titel": "Herausgabe des Ersatzes (commodum ex negotiatione)",
                "inhalt": "Schuldner muss das erlangte Surrogat herausgeben wenn er wegen Unmöglichkeit befreit ist.",
                "verbindungen": ["§ 275 BGB", "§ 283 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__285.html",
            },
            {
                "norm": "§ 276 BGB",
                "titel": "Verantwortlichkeit des Schuldners",
                "inhalt": "Vorsatz + Fahrlässigkeit (objektiver Maßstab, § 276 II). Mildere Haftung durch Parteivereinbarung oder gesetzliche Anordnung möglich.",
                "verbindungen": ["§ 280 BGB", "§ 277 BGB", "§ 278 BGB"],
                "typ": "Ergänzung",
                "link": "https://www.gesetze-im-internet.de/bgb/__276.html",
            },
            {
                "norm": "§ 249 BGB",
                "titel": "Art und Umfang des Schadensersatzes",
                "inhalt": "Naturalrestitution als Grundsatz (Abs. 1). Geldersatz bei Körperverletzung/Sachbeschädigung (Abs. 2). Differenzhypothese.",
                "verbindungen": ["§ 250 BGB", "§ 251 BGB", "§ 254 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__249.html",
            },
            {
                "norm": "§ 254 BGB",
                "titel": "Mitverschulden",
                "inhalt": "Anspruchsminderung bei eigenem Verschulden des Gläubigers. Obliegenheit zur Schadensminderung.",
                "verbindungen": ["§ 249 BGB", "§ 280 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__254.html",
            },
        ],
        "schema": [
            "1. Schuldverhältnis (§ 241 I oder II BGB)",
            "2. Pflichtverletzung (§ 280 I 1 BGB)",
            "   → Nichtleistung, Schlechtleistung, Schutzpflichtverletzung",
            "3. Vertretenmüssen (§§ 276–278 BGB) — Verschuldensvermutung",
            "4. Zusatzvoraussetzungen für SE statt Leistung:",
            "   a) § 281 BGB: Fristsetzung + Ablauf (bei Nicht-/Schlechtleistung)",
            "   b) § 282 BGB: Unzumutbarkeit (bei Schutzpflichtverletzung)",
            "   c) § 283 BGB: Unmöglichkeit (§ 275 BGB) — kein Fristsetzung nötig",
            "5. Schaden (§§ 249 ff. BGB) — Differenzhypothese",
            "6. Mitverschulden (§ 254 BGB) prüfen",
        ],
        "klausurfallen": [
            "§ 280 I allein gibt nur SE neben der Leistung — für SE statt Leistung §§ 281–283 erforderlich",
            "Fristsetzung bei § 281: Angemessenheit und Entbehrlichkeit (§ 281 II) prüfen",
            "§ 281 I 3: bei Schlechtleistung Erheblichkeitsschwelle — unerhebliche Mängel genügen nicht",
            "§ 276 I: keine Haftung für leichte Fahrlässigkeit bei bestimmten Vertragstypen",
            "§ 254 II: Schadensminderungsobliegenheit — z.B. Hinweis auf drohende Schäden",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Kaufrechtliche Mängelhaftung": {
        "beschreibung": (
            "Das kaufrechtliche Gewährleistungsrecht (§§ 434–445 BGB) ergänzt das "
            "allgemeine Schuldrecht. §§ 434 f. BGB definieren den Mangel; "
            "§§ 437 ff. BGB die Rechte des Käufers. § 475 BGB ist Verbraucherschutznorm."
        ),
        "rechtsgebiet": "Zivilrecht",
        "icon": "🛒",
        "normen": [
            {
                "norm": "§ 434 BGB",
                "titel": "Sachmangel",
                "inhalt": "Dreistufig: (1) vereinbarte Beschaffenheit, (2) vertraglich vorausgesetzte Verwendung, (3) gewöhnliche Verwendung und übliche Beschaffenheit. Montagemangel (Abs. 4). WKRL-Umsetzung 2022.",
                "verbindungen": ["§ 435 BGB", "§ 437 BGB", "§ 476 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__434.html",
            },
            {
                "norm": "§ 435 BGB",
                "titel": "Rechtsmangel",
                "inhalt": "Dritte können Rechte geltend machen, die der Käufer nicht übernehmen musste. Öffentliche Lasten im Grundstücksrecht.",
                "verbindungen": ["§ 434 BGB", "§ 437 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__435.html",
            },
            {
                "norm": "§ 437 BGB",
                "titel": "Rechte des Käufers bei Mängeln",
                "inhalt": "Katalog: (1) Nacherfüllung (§ 439), (2) Rücktritt (§§ 440, 323, 326 V) oder Minderung (§ 441), (3) SE (§§ 440, 280, 281, 283, 311a) oder Aufwendungsersatz (§ 284).",
                "verbindungen": ["§ 434 BGB", "§ 439 BGB", "§ 440 BGB", "§ 441 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__437.html",
            },
            {
                "norm": "§ 438 BGB",
                "titel": "Verjährung der Mängelansprüche",
                "inhalt": "2 Jahre ab Übergabe (Abs. 1 Nr. 3). 5 Jahre bei Bauwerken/eingebauten Sachen (Nr. 2). 30 Jahre bei arglistigem Verschweigen (Abs. 3).",
                "verbindungen": ["§ 437 BGB", "§ 195 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__438.html",
            },
            {
                "norm": "§ 439 BGB",
                "titel": "Nacherfüllung",
                "inhalt": "Käuferwahl: Nachbesserung oder Nachlieferung. Verkäufer kann wegen Unverhältnismäßigkeit verweigern (Abs. 4). Kosten trägt Verkäufer (Abs. 2).",
                "verbindungen": ["§ 437 BGB", "§ 440 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__439.html",
            },
            {
                "norm": "§ 440 BGB",
                "titel": "Besondere Bestimmungen für Rücktritt und Schadensersatz",
                "inhalt": "Fristsetzung entbehrlich bei: Unmöglichkeit der Nacherfüllung, Verweigerung, Fehlschlagen (2 Versuche), Unzumutbarkeit.",
                "verbindungen": ["§ 437 BGB", "§ 323 BGB", "§ 281 BGB"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/bgb/__440.html",
            },
            {
                "norm": "§ 441 BGB",
                "titel": "Minderung",
                "inhalt": "Herabsetzung des Kaufpreises im Verhältnis mangelfreier zu mangelhaftem Wert. Kein Verschulden erforderlich.",
                "verbindungen": ["§ 437 BGB", "§ 323 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__441.html",
            },
            {
                "norm": "§ 442 BGB",
                "titel": "Kenntnis des Käufers",
                "inhalt": "Kenntnis bei Vertragsschluss schließt Mängelrechte aus. Grob fahrlässige Unkenntnis schadet nur bei arglistigem Verschweigen.",
                "verbindungen": ["§ 437 BGB", "§ 123 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__442.html",
            },
            {
                "norm": "§ 475 BGB",
                "titel": "Anwendbare Vorschriften beim Verbrauchsgüterkauf",
                "inhalt": "Verbrauchsgüterkauf: zwingendes Recht zugunsten des Verbrauchers. Abweichungen zum Nachteil des Verbrauchers unwirksam.",
                "verbindungen": ["§ 13 BGB", "§ 14 BGB", "§ 474 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__475.html",
            },
        ],
        "schema": [
            "1. Kaufvertrag (§ 433 BGB)",
            "2. Mangel bei Gefahrübergang (§ 434 oder 435 BGB)",
            "   a) Vereinbarte Beschaffenheit (§ 434 I Nr. 1)",
            "   b) Vertraglich vorausgesetzte Verwendung (§ 434 I Nr. 2)",
            "   c) Gewöhnliche Verwendung + übliche Beschaffenheit (§ 434 III)",
            "3. Vorrang der Nacherfüllung (§ 439 BGB)",
            "   → Fristsetzung grds. erforderlich, Ausnahmen § 440 BGB",
            "4. Sekundäre Rechte nach erfolgloser Nacherfüllung:",
            "   a) Rücktritt (§§ 437 Nr. 2, 440, 323 BGB)",
            "   b) Minderung (§§ 437 Nr. 2, 441 BGB)",
            "   c) SE statt Leistung (§§ 437 Nr. 3, 440, 281, 280 BGB)",
            "5. Verjährung prüfen (§ 438 BGB) — 2 Jahre ab Übergabe",
            "6. Kenntnis des Käufers (§ 442 BGB) prüfen",
            "7. Ggf. Verbrauchsgüterkauf (§§ 474 ff. BGB) beachten",
        ],
        "klausurfallen": [
            "Mangel muss bei Gefahrübergang (§ 446 BGB) vorliegen — Beweislastumkehr § 477 BGB bei Verbrauchsgüterkauf",
            "§ 440: 'Fehlschlagen' der Nacherfüllung nach 2 Versuchen nur Regelbeispiel — Einzelfallprüfung",
            "Minderung erfordert kein Verschulden des Verkäufers",
            "§ 442: grob fahrlässige Unkenntnis nur bei arglistigem Verschweigen unschädlich",
            "Verbrauchsgüterkauf (§ 475): einjährige Verkürzung nur möglich bei gebrauchten Sachen",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Deliktsrecht": {
        "beschreibung": (
            "Das Deliktsrecht (§§ 823–826 BGB) begründet außervertragliche Schadensersatzansprüche. "
            "§§ 249–254 BGB regeln Umfang und Grenzen des Ersatzes. "
            "Prüfungsschwerpunkte: Haftungsgrund, Rechtswidrigkeit, Verschulden."
        ),
        "rechtsgebiet": "Zivilrecht",
        "icon": "⚠️",
        "normen": [
            {
                "norm": "§ 823 I BGB",
                "titel": "Schadensersatzpflicht — Rechtsgutsverletzung",
                "inhalt": "Verletzung von Leben, Körper, Gesundheit, Freiheit, Eigentum, sonstigen Rechten (absoluter Rechtsgüterkatalog). Vorsatz oder Fahrlässigkeit.",
                "verbindungen": ["§ 823 II BGB", "§ 249 BGB", "§ 276 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__823.html",
            },
            {
                "norm": "§ 823 II BGB",
                "titel": "Schutzgesetzverletzung",
                "inhalt": "Verstoß gegen Schutzgesetz (Norm die zumindest auch Individualschutz bezweckt). Verschulden bzgl. des Verstoßes, nicht zwingend bzgl. des Schadens.",
                "verbindungen": ["§ 823 I BGB", "§ 826 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__823.html",
            },
            {
                "norm": "§ 824 BGB",
                "titel": "Kreditgefährdung",
                "inhalt": "Verbreitung unwahre Tatsachen die geeignet sind Kredit zu gefährden oder sonstigen Nachteil zuzufügen.",
                "verbindungen": ["§ 823 BGB", "§ 1004 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__824.html",
            },
            {
                "norm": "§ 826 BGB",
                "titel": "Sittenwidrige vorsätzliche Schädigung",
                "inhalt": "Vorsätzliche Schädigung in einer gegen die guten Sitten verstoßenden Weise. Generalklausel; erfasst auch reine Vermögensschäden.",
                "verbindungen": ["§ 823 BGB", "§ 138 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/bgb/__826.html",
            },
            {
                "norm": "§ 831 BGB",
                "titel": "Haftung für den Verrichtungsgehilfen",
                "inhalt": "Geschäftsherr haftet für Verrichtungsgehilfen; Exkulpation durch sorgfältige Auswahl/Überwachung möglich (Abs. 1 S. 2).",
                "verbindungen": ["§ 823 BGB", "§ 276 BGB"],
                "typ": "Ergänzung",
                "link": "https://www.gesetze-im-internet.de/bgb/__831.html",
            },
            {
                "norm": "§ 249 BGB",
                "titel": "Art und Umfang des Schadensersatzes",
                "inhalt": "Naturalrestitution als Grundsatz. Geldersatz bei Körperverletzung und Sachschäden. Differenzhypothese zur Schadensberechnung.",
                "verbindungen": ["§ 250 BGB", "§ 251 BGB", "§ 253 BGB", "§ 254 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__249.html",
            },
            {
                "norm": "§ 253 BGB",
                "titel": "Immaterieller Schaden (Schmerzensgeld)",
                "inhalt": "Geldentschädigung für immaterielle Schäden nur bei gesetzlicher Anordnung. § 253 II: Schmerzensgeld bei Körper-/Gesundheits-/Freiheitsverletzung.",
                "verbindungen": ["§ 823 BGB", "§ 249 BGB"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/bgb/__253.html",
            },
            {
                "norm": "§ 254 BGB",
                "titel": "Mitverschulden",
                "inhalt": "Eigenes Verschulden des Geschädigten mindert Anspruch (Abs. 1). Obliegenheit zur Schadensminderung (Abs. 2). Berücksichtigung im Verhältnis der Verursachungsbeiträge.",
                "verbindungen": ["§ 249 BGB", "§ 823 BGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/bgb/__254.html",
            },
        ],
        "schema": [
            "1. Haftungsbegründender Tatbestand",
            "   a) § 823 I BGB: Verletzung eines absoluten Rechtsguts",
            "      — Leben, Körper, Gesundheit, Freiheit, Eigentum, sonstiges Recht",
            "   b) § 823 II BGB: Verstoß gegen Schutzgesetz",
            "      — Schutzgesetzcharakter (Individualschutz?)",
            "   c) § 826 BGB: Vorsätzliche sittenwidrige Schädigung",
            "2. Rechtswidrigkeit (Indizwirkung; Rechtfertigungsgründe?)",
            "3. Verschulden (§ 276 BGB): Vorsatz oder Fahrlässigkeit",
            "4. Haftungsausfüllender Tatbestand: Schaden (§§ 249 ff. BGB)",
            "   a) Naturalrestitution (§ 249 I)",
            "   b) Geldersatz (§§ 249 II, 251 BGB)",
            "   c) Immaterieller Schaden: Schmerzensgeld (§ 253 II BGB)",
            "5. Mitverschulden (§ 254 BGB)",
            "6. Verjährung (§§ 195, 199 BGB): 3 Jahre ab Kenntnis",
        ],
        "klausurfallen": [
            "§ 823 I: 'Sonstiges Recht' — nur absolut geschützte Rechtspositionen (nicht bloße Vermögensinteressen!)",
            "§ 823 II: Schutzgesetzeigenschaft prüfen — nicht jede öffentlich-rechtliche Norm ist Schutzgesetz",
            "§ 831: Exkulpation durch ordentliche Auswahl, Ausrüstung, Anweisung, Überwachung möglich",
            "§ 253: Schmerzensgeld auch bei § 823 II und § 826 BGB, wenn Körper/Gesundheit/Freiheit verletzt",
            "Kausalität: haftungsbegründend (conditio sine qua non) UND haftungsausfüllend (Adäquanz) prüfen",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Strafrecht AT – Verbrechensaufbau": {
        "beschreibung": (
            "Die zentralen StGB-Normen für den dreistufigen Verbrechensaufbau: "
            "Tatbestand, Rechtswidrigkeit, Schuld. Examensrelevant: Irrtumslehre, "
            "Vorsatz/Fahrlässigkeit, Schuldfähigkeit, Versuch."
        ),
        "rechtsgebiet": "Strafrecht",
        "icon": "⚖️",
        "normen": [
            {
                "norm": "§ 15 StGB",
                "titel": "Vorsätzliches und fahrlässiges Handeln",
                "inhalt": "Strafbar nur bei Vorsatz, soweit nicht ausdrücklich Fahrlässigkeit mit Strafe bedroht. Grundnorm für Vorsatzerfordernis.",
                "verbindungen": ["§ 16 StGB", "§ 17 StGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/stgb/__15.html",
            },
            {
                "norm": "§ 16 StGB",
                "titel": "Irrtum über Tatumstände (Tatbestandsirrtum)",
                "inhalt": "Unkenntnis eines zum Tatbestand gehörenden Umstandes schließt Vorsatz aus (Abs. 1 S. 1). Fahrlässigkeitsstrafbarkeit bleibt möglich (Abs. 1 S. 2). Abs. 2: Putativnorm.",
                "verbindungen": ["§ 15 StGB", "§ 17 StGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/stgb/__16.html",
            },
            {
                "norm": "§ 17 StGB",
                "titel": "Verbotsirrtum",
                "inhalt": "Fehlt dem Täter bei der Tat die Unrechtseinsicht schuldlos (unvermeidbar): kein Schuldvorwurf. Vermeidbar: Strafmilderung möglich.",
                "verbindungen": ["§ 16 StGB", "§ 49 StGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/stgb/__17.html",
            },
            {
                "norm": "§ 20 StGB",
                "titel": "Schuldunfähigkeit wegen seelischer Störungen",
                "inhalt": "Schuldunfähigkeit bei: krankhafter seelischer Störung, tiefgreifender Bewusstseinsstörung, Schwachsinn, schwerer anderer seelischer Abartigkeit — wenn dadurch Unrechtseinsicht/Steuerungsfähigkeit fehlt.",
                "verbindungen": ["§ 21 StGB", "§ 63 StGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/stgb/__20.html",
            },
            {
                "norm": "§ 21 StGB",
                "titel": "Verminderte Schuldfähigkeit",
                "inhalt": "Erheblich verminderte Unrechtseinsicht oder Steuerungsfähigkeit: Strafmilderung nach § 49 I StGB möglich (fakultativ).",
                "verbindungen": ["§ 20 StGB", "§ 49 StGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/stgb/__21.html",
            },
            {
                "norm": "§ 22 StGB",
                "titel": "Begriffsbestimmung des Versuchs",
                "inhalt": "Versuch: unmittelbares Ansetzen zur Tatbestandsverwirklichung nach dem Tatplan. Subjektive Theorie für das Ansetzen.",
                "verbindungen": ["§ 23 StGB", "§ 24 StGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/stgb/__22.html",
            },
            {
                "norm": "§ 23 StGB",
                "titel": "Strafbarkeit des Versuchs",
                "inhalt": "Versuch eines Verbrechens stets strafbar (Abs. 1). Vergehen: nur wenn ausdrücklich angeordnet. Untauglicher Versuch strafbar (Abs. 3: grob unverständig → fakultative Strafmilderung/-befreiung).",
                "verbindungen": ["§ 22 StGB", "§ 24 StGB", "§ 12 StGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/stgb/__23.html",
            },
            {
                "norm": "§ 24 StGB",
                "titel": "Rücktritt vom Versuch",
                "inhalt": "Freiwilliger Rücktritt: unbeendeter Versuch (Aufgabe), beendeter Versuch (Verhinderung). Persönlicher Strafaufhebungsgrund.",
                "verbindungen": ["§ 22 StGB", "§ 23 StGB"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/stgb/__24.html",
            },
        ],
        "schema": [
            "I. Tatbestand",
            "   1. Objektiver Tatbestand: Tathandlung, Erfolg, Kausalität, obj. Zurechnung",
            "   2. Subjektiver Tatbestand: Vorsatz (§ 15 StGB)",
            "      → Tatbestandsirrtum (§ 16 I StGB): entfällt Vorsatz?",
            "II. Rechtswidrigkeit",
            "   → Rechtfertigungsgründe (§§ 32, 34 StGB; § 127 StPO etc.)?",
            "III. Schuld",
            "   1. Schuldfähigkeit (§§ 19, 20 StGB) — Altersgrenzen, seelische Störungen",
            "   2. Verminderte Schuldfähigkeit (§ 21 StGB)",
            "   3. Unrechtsbewusstsein / Verbotsirrtum (§ 17 StGB)",
            "   4. Entschuldigungsgründe (§§ 33, 35 StGB)",
            "IV. Versuch (wenn Vollendung nicht gegeben)",
            "   1. Vorprüfung: Verbrechenstatbestand oder Vergehen mit Versuchsstrafbarkeit",
            "   2. Tatentschluss + unmittelbares Ansetzen (§ 22 StGB)",
            "   3. Kein strafbefreiender Rücktritt (§ 24 StGB)",
        ],
        "klausurfallen": [
            "§ 16 vs. § 17: TB-Irrtum (Wissenselement des Vorsatzes) vs. Verbotsirrtum (Unrechtsbewusstsein)",
            "Dolus eventualis: billigendes In-Kauf-Nehmen — Abgrenzung zur bewussten Fahrlässigkeit",
            "§ 20: zweistufig — biologisch-psychologische Störung UND normativ-rechtliche Folge prüfen",
            "§ 22 'unmittelbares Ansetzen': subjektiver Tatplan + objektive Schwelle — kein Rückschritt mehr möglich",
            "§ 24: Rücktritt muss freiwillig sein — eigenverantwortliche Entscheidung, nicht durch äußere Hindernisse erzwungen",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Grundrechtsprüfung": {
        "beschreibung": (
            "Übersicht der examensrelevanten Grundrechte (Art. 1–3, 5, 8, 14 GG) "
            "und ihrer Schranken. Prüfungsaufbau: Schutzbereich → Eingriff → "
            "Verfassungsrechtliche Rechtfertigung."
        ),
        "rechtsgebiet": "Öffentliches Recht",
        "icon": "🏛️",
        "normen": [
            {
                "norm": "Art. 1 GG",
                "titel": "Menschenwürde",
                "inhalt": "Abs. 1: Unantastbar; keine Abwägung möglich. Abs. 2: Bekenntnis zu Menschenrechten. Abs. 3: Grundrechte als unmittelbar geltendes Recht — Bindung aller Staatsgewalt.",
                "verbindungen": ["Art. 2 GG", "Art. 19 GG"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/gg/art_1.html",
            },
            {
                "norm": "Art. 2 GG",
                "titel": "Allgemeine Handlungsfreiheit / Körperliche Unversehrtheit",
                "inhalt": "Abs. 1: Allgemeine Handlungsfreiheit (Auffanggrundrecht). Abs. 2: Recht auf Leben und körperliche Unversehrtheit; Freiheit der Person.",
                "verbindungen": ["Art. 1 GG", "Art. 104 GG"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/gg/art_2.html",
            },
            {
                "norm": "Art. 3 GG",
                "titel": "Gleichheitssatz",
                "inhalt": "Abs. 1: Allgemeiner Gleichheitssatz — keine willkürliche Ungleichbehandlung. Abs. 2, 3: besondere Gleichheitssätze (Geschlecht, Abstammung, Rasse etc.).",
                "verbindungen": ["Art. 1 GG", "Art. 33 GG"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/gg/art_3.html",
            },
            {
                "norm": "Art. 5 GG",
                "titel": "Meinungs-, Presse-, Rundfunk- und Kunstfreiheit",
                "inhalt": "Abs. 1: Meinungsfreiheit (Werturteile), Pressefreiheit, Rundfunkfreiheit. Abs. 3: Kunst- und Wissenschaftsfreiheit (vorbehaltlos). Schranken Abs. 2: allgemeine Gesetze, Jugendschutz, Ehrenschutz.",
                "verbindungen": ["Art. 1 GG", "§ 823 BGB"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/gg/art_5.html",
            },
            {
                "norm": "Art. 8 GG",
                "titel": "Versammlungsfreiheit",
                "inhalt": "Abs. 1: Recht auf friedliche Versammlungen ohne Waffen ohne Anmeldung. Abs. 2: Beschränkungen nur für Versammlungen unter freiem Himmel (Gesetzesvorbehalt).",
                "verbindungen": ["Art. 5 GG", "Art. 9 GG"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/gg/art_8.html",
            },
            {
                "norm": "Art. 14 GG",
                "titel": "Eigentumsgarantie",
                "inhalt": "Abs. 1: Eigentum und Erbrecht gewährleistet; Inhalt und Schranken durch Gesetz. Abs. 2: Sozialpflichtigkeit. Abs. 3: Enteignung nur zum Wohl der Allgemeinheit gegen Entschädigung.",
                "verbindungen": ["Art. 12 GG", "Art. 15 GG"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/gg/art_14.html",
            },
            {
                "norm": "Art. 19 GG",
                "titel": "Einschränkung von Grundrechten",
                "inhalt": "Abs. 1: Gesetzesvorbehalt (Zitiergebot). Abs. 2: Wesensgehaltsgarantie. Abs. 3: Grundrechte gelten auch für inländische juristischen Personen. Abs. 4: Rechtswegsgarantie.",
                "verbindungen": ["Art. 1 GG", "Art. 20 GG"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/gg/art_19.html",
            },
            {
                "norm": "Art. 20 GG",
                "titel": "Staatsstrukturprinzipien / Widerstandsrecht",
                "inhalt": "Demokratie-, Sozial-, Rechtsstaatsprinzip, Bundesstaatsprinzip (Abs. 1–3). Verhältnismäßigkeitsprinzip als Bestandteil des Rechtsstaatsprinzips.",
                "verbindungen": ["Art. 19 GG", "Art. 79 GG"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/gg/art_20.html",
            },
        ],
        "schema": [
            "I. Schutzbereich",
            "   1. Persönlicher Schutzbereich: Wer ist Grundrechtsträger?",
            "   2. Sachlicher Schutzbereich: Was wird geschützt?",
            "II. Eingriff",
            "   1. Klassischer Eingriff: final, unmittelbar, imperativ, rechtsförmig",
            "   2. Moderner Eingriffsbegriff: auch mittelbare/faktische Beeinträchtigungen",
            "III. Verfassungsrechtliche Rechtfertigung",
            "   1. Schranken: Gesetzesvorbehalt (einfacher/qualifizierter) oder vorbehaltlose Grundrechte",
            "   2. Schranken-Schranken:",
            "      a) Formelle Anforderungen (Kompetenz, Verfahren, Form)",
            "      b) Zitiergebot (Art. 19 I 2 GG) bei qualifiziertem Vorbehalt",
            "      c) Verhältnismäßigkeitsgrundsatz:",
            "         — Legitimer Zweck",
            "         — Geeignetheit",
            "         — Erforderlichkeit",
            "         — Angemessenheit (Verhältnismäßigkeit i.e.S.)",
            "      d) Wesensgehaltsgarantie (Art. 19 II GG)",
        ],
        "klausurfallen": [
            "Vorbehaltlose Grundrechte (Art. 4, 5 III, 8 I) können nur durch kollidierende Verfassungsgüter eingeschränkt werden",
            "Art. 3 I: Neue Formel des BVerfG — je stärker Ungleichbehandlung die Ausübung von Freiheitsrechten betrifft, desto strengere Prüfung",
            "Art. 14: Inhalts-/Schrankenbestimmung (keine Entschädigung) vs. Enteignung (Entschädigung!) — Abgrenzung wichtig",
            "Mittelbare Drittwirkung: Grundrechte entfalten Wirkung im Privatrecht über Generalklauseln",
            "Art. 19 III: Grundrechte für juristische Personen nur soweit 'wesensgemäß anwendbar'",
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    "Verwaltungsakt": {
        "beschreibung": (
            "Das Recht des Verwaltungsakts nach §§ 35–53 VwVfG und die verwaltungsgerichtliche "
            "Kontrolle (§ 113 VwGO). Kernstück des allgemeinen Verwaltungsrechts "
            "und Ausgangspunkt für Anfechtungs- und Verpflichtungsklagen."
        ),
        "rechtsgebiet": "Öffentliches Recht",
        "icon": "📋",
        "normen": [
            {
                "norm": "§ 35 VwVfG",
                "titel": "Begriff des Verwaltungsakts",
                "inhalt": "VA: hoheitliche Maßnahme einer Behörde auf öffentl.-rechtl. Gebiet zur Regelung eines Einzelfalls mit Außenwirkung. Allgemeinverfügung (S. 2).",
                "verbindungen": ["§ 36 VwVfG", "§ 40 VwGO", "§ 42 VwGO"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__35.html",
            },
            {
                "norm": "§ 36 VwVfG",
                "titel": "Nebenbestimmungen zum Verwaltungsakt",
                "inhalt": "Bedingung, Befristung, Auflage, Widerrufsvorbehalt, Auflagenvorbehalt. Zulässigkeit: bei gebundenen VA nur wenn gesetzlich vorgesehen.",
                "verbindungen": ["§ 35 VwVfG", "§ 113 VwGO"],
                "typ": "Ergänzung",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__36.html",
            },
            {
                "norm": "§ 37 VwVfG",
                "titel": "Bestimmtheit und Form des Verwaltungsakts",
                "inhalt": "Hinreichende Bestimmtheit (Abs. 1). Schriftform bei Rechtsgrundlagenverweis (Abs. 2). Begründungspflicht nach § 39 VwVfG.",
                "verbindungen": ["§ 39 VwVfG", "§ 44 VwVfG"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__37.html",
            },
            {
                "norm": "§ 39 VwVfG",
                "titel": "Begründung des Verwaltungsakts",
                "inhalt": "Schriftlicher VA ist grds. schriftlich zu begründen. Ausnahmen (Abs. 2). Nachholung der Begründung (§ 45 VwVfG). Heilung möglich.",
                "verbindungen": ["§ 37 VwVfG", "§ 44 VwVfG", "§ 45 VwVfG"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__39.html",
            },
            {
                "norm": "§ 43 VwVfG",
                "titel": "Wirksamkeit des Verwaltungsakts",
                "inhalt": "Bekanntgabe als Wirksamkeitsvoraussetzung (Abs. 1). Wirksamkeit trotz Rechtswidrigkeit bis zu Aufhebung (Abs. 2). Ausnahme: Nichtigkeit.",
                "verbindungen": ["§ 44 VwVfG", "§ 45 VwVfG", "§ 41 VwVfG"],
                "typ": "Grundnorm",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__43.html",
            },
            {
                "norm": "§ 44 VwVfG",
                "titel": "Nichtigkeit des Verwaltungsakts",
                "inhalt": "VA ist nichtig bei besonders schwerwiegendem und offenkundigem Fehler (Abs. 1). Abs. 2: Regelbeispiele. Abs. 3: Ausnahmen von Nichtigkeit.",
                "verbindungen": ["§ 43 VwVfG", "§ 113 VwGO"],
                "typ": "Einschränkung",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__44.html",
            },
            {
                "norm": "§ 45 VwVfG",
                "titel": "Heilung von Verfahrens- und Formfehlern",
                "inhalt": "Formfehler heilbar: fehlende Begründung (Nr. 2), fehlende Anhörung (Nr. 3) etc. — bis zur letzten Tatsacheninstanz im verwaltungsgerichtlichen Verfahren.",
                "verbindungen": ["§ 44 VwVfG", "§ 46 VwVfG"],
                "typ": "Ergänzung",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__45.html",
            },
            {
                "norm": "§ 48 VwVfG",
                "titel": "Rücknahme eines rechtswidrigen VA",
                "inhalt": "Rechtswidrige VA können mit Wirkung für die Zukunft oder Vergangenheit zurückgenommen werden. Bei begünstigenden VA: Vertrauensschutz beachten (Abs. 2).",
                "verbindungen": ["§ 49 VwVfG", "§ 44 VwVfG"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__48.html",
            },
            {
                "norm": "§ 49 VwVfG",
                "titel": "Widerruf eines rechtmäßigen VA",
                "inhalt": "Widerruf nur unter engen Voraussetzungen (Abs. 2 Nr. 1–5). Entschädigungspflicht nach Abs. 6.",
                "verbindungen": ["§ 48 VwVfG", "§ 49a VwVfG"],
                "typ": "Verfahren",
                "link": "https://www.gesetze-im-internet.de/vwvfg/__49.html",
            },
            {
                "norm": "§ 113 VwGO",
                "titel": "Urteilsinhalt bei Anfechtungs- und Verpflichtungsklage",
                "inhalt": "Abs. 1: Anfechtungsklage — Aufhebung rechtswidriger belastender VA bei Rechtsverletzung. Abs. 5: Verpflichtungsklage — Erlass oder Neubescheidung.",
                "verbindungen": ["§ 42 VwGO", "§ 44 VwVfG", "§ 48 VwVfG"],
                "typ": "Rechtsfolge",
                "link": "https://www.gesetze-im-internet.de/vwgo/__113.html",
            },
        ],
        "schema": [
            "I. Zulässigkeit der Anfechtungsklage (§ 42 I Var. 1 VwGO)",
            "   1. Verwaltungsrechtsweg (§ 40 VwGO)",
            "   2. Statthafte Klageart: VA i.S.d. § 35 VwVfG",
            "   3. Klagebefugnis (§ 42 II VwGO): Mögliche Verletzung subjektiver Rechte",
            "   4. Vorverfahren / Widerspruchsverfahren (§§ 68 ff. VwGO)",
            "   5. Klagefrist (§ 74 VwGO): 1 Monat ab Zustellung des Widerspruchsbescheids",
            "   6. Beteiligungsfähigkeit, Prozessfähigkeit",
            "II. Begründetheit (§ 113 I 1 VwGO)",
            "   1. Rechtswidrigkeit des VA",
            "      a) Formelle Rechtmäßigkeit: Zuständigkeit, Verfahren (§§ 24, 28 VwVfG), Form",
            "         → Heilung nach § 45 VwVfG? Unbeachtlichkeit nach § 46 VwVfG?",
            "      b) Materielle Rechtmäßigkeit: Ermächtigungsgrundlage, TB, Rechtsfolge",
            "         → Ermessen (§ 40 VwVfG): Ermessensausfall, -missbrauch, -überschreitung",
            "   2. Verletzung subjektiver Rechte des Klägers",
        ],
        "klausurfallen": [
            "§ 35 VwVfG: 'Regelung' — nur Rechtsfolgen setzende Maßnahmen, keine bloßen Hinweise/Auskünfte",
            "§ 44 VwVfG Nichtigkeit: Doppelvoraussetzung — schwerwiegend UND offenkundig",
            "§ 45 vs. § 46 VwVfG: Heilung (noch möglich) vs. Unbeachtlichkeit (Aufhebung trotzdem verhindert)",
            "§ 48 II VwVfG: Vertrauensschutz bei begünstigenden VA — Abwägung mit öffentlichem Interesse",
            "§ 113 I 1: 'soweit' — Teilaufhebung bei teilbaren VA möglich",
        ],
    },
}

# ── SEITEN-HEADER ─────────────────────────────────────────────────────────────

page_header(
    "Normennetze",
    "Strukturierte Übersichten examensrelevanter Normen und ihrer Zusammenhänge",
    "🕸️",
)

gold_divider()

# ── THEMA-AUSWAHL ─────────────────────────────────────────────────────────────

themen = list(NORMENNETZE.keys())

# Ggf. Selektion aus Session-State übernehmen
default_idx = 0
if "nn_thema" in st.session_state and st.session_state["nn_thema"] in themen:
    default_idx = themen.index(st.session_state["nn_thema"])

col_sel, col_info = st.columns([2, 3])

with col_sel:
    section_header("📖", "Thema wählen")
    thema = st.selectbox(
        "Thema",
        themen,
        index=default_idx,
        key="nn_thema",
        format_func=lambda t: f"{NORMENNETZE[t]['icon']} {t}",
        label_visibility="collapsed",
    )

netz = NORMENNETZE[thema]

with col_info:
    rechtsgebiet = netz.get("rechtsgebiet", "")
    rg_badge_col = {"Zivilrecht": "#1d4ed8", "Strafrecht": "#dc2626", "Öffentliches Recht": "#15803d"}.get(rechtsgebiet, "#57534e")
    st.markdown(
        f'<div style="background:rgba(26,39,68,.04);border:1px solid #edeae0;border-radius:10px;'
        f'padding:.75rem 1rem;margin-top:1.6rem">'
        f'<span style="background:{rg_badge_col};color:#fff;font-size:.7rem;font-weight:700;'
        f'padding:.2rem .6rem;border-radius:99px;margin-right:.6rem">{rechtsgebiet}</span>'
        f'<span style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.84rem;color:#44403c">'
        f'{netz["beschreibung"]}</span></div>',
        unsafe_allow_html=True,
    )

gold_divider()

# ── TABS ──────────────────────────────────────────────────────────────────────

tab_netz, tab_schema = st.tabs(["📊 Normennetz", "📋 Prüfungsschema"])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — NORMENNETZ
# ─────────────────────────────────────────────────────────────────────────────
with tab_netz:
    normen = netz["normen"]

    # Statistik-Zeile
    typ_counts: dict[str, int] = {}
    for n in normen:
        t = n.get("typ", "Grundnorm")
        typ_counts[t] = typ_counts.get(t, 0) + 1

    badges_html = "".join(
        f'<span style="background:{TYP_FARBEN[t]["bg"]};color:{TYP_FARBEN[t]["text"]};'
        f'border:1px solid {TYP_FARBEN[t]["border"]};font-size:.7rem;font-weight:700;'
        f'padding:.2rem .55rem;border-radius:99px;margin-right:.35rem">'
        f'{c}× {t}</span>'
        for t, c in typ_counts.items()
        if t in TYP_FARBEN
    )
    st.markdown(
        f'<div style="margin:.4rem 0 .85rem;display:flex;flex-wrap:wrap;gap:.25rem;align-items:center">'
        f'<span style="font-size:.72rem;color:#57534e;margin-right:.35rem">Typen:</span>'
        f'{badges_html}</div>',
        unsafe_allow_html=True,
    )

    # Legende
    legende_html = "".join(
        f'<div style="display:flex;align-items:center;gap:.4rem;margin-right:.75rem">'
        f'<div style="width:12px;height:12px;border-radius:3px;background:{v["bg"]};'
        f'border:1px solid {v["border"]}"></div>'
        f'<span style="font-size:.7rem;color:#57534e">{v["label"]}</span></div>'
        for v in TYP_FARBEN.values()
    )
    st.markdown(
        f'<div style="display:flex;flex-wrap:wrap;margin-bottom:1rem">{legende_html}</div>',
        unsafe_allow_html=True,
    )

    # Grid der Norm-Cards — 3 Spalten
    cols = st.columns(3)
    for idx, norm_data in enumerate(normen):
        typ = norm_data.get("typ", "Grundnorm")
        farbe = TYP_FARBEN.get(typ, TYP_FARBEN["Grundnorm"])

        verbindungen = norm_data.get("verbindungen", [])
        verb_html = ""
        if verbindungen:
            verb_items = "".join(
                f'<span style="display:inline-block;background:rgba(255,255,255,.15);'
                f'border:1px solid rgba(255,255,255,.3);border-radius:4px;'
                f'font-family:\'IBM Plex Mono\',monospace;font-size:.65rem;'
                f'padding:.1rem .35rem;margin:.1rem .15rem .1rem 0;white-space:nowrap">'
                f'→ {v}</span>'
                for v in verbindungen
            )
            verb_html = (
                f'<div style="margin-top:.6rem;border-top:1px solid rgba(255,255,255,.15);'
                f'padding-top:.45rem;font-size:.65rem;color:rgba(255,255,255,.65);'
                f'margin-bottom:.1rem">Verbindungen:</div>'
                f'<div>{verb_items}</div>'
            )

        typ_badge = (
            f'<span style="background:rgba(255,255,255,.18);color:{farbe["text"]};'
            f'font-size:.62rem;font-weight:700;padding:.1rem .4rem;border-radius:99px;'
            f'border:1px solid rgba(255,255,255,.25)">{typ}</span>'
        )

        link = norm_data.get("link", "")
        link_btn = ""
        if link:
            link_btn = (
                f'<div style="margin-top:.65rem">'
                f'<a href="{link}" target="_blank" rel="noopener noreferrer" '
                f'style="display:inline-block;background:rgba(255,255,255,.13);'
                f'border:1px solid rgba(255,255,255,.3);border-radius:5px;'
                f'font-family:\'IBM Plex Sans\',sans-serif;font-size:.7rem;'
                f'font-weight:600;color:{farbe["text"]};padding:.25rem .65rem;'
                f'text-decoration:none">📖 Gesetz öffnen</a></div>'
            )

        card_html = (
            f'<div style="background:{farbe["bg"]};border:1px solid {farbe["border"]};'
            f'border-radius:10px;padding:.85rem 1rem;margin-bottom:.65rem;'
            f'box-shadow:0 2px 8px rgba(0,0,0,.15)">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;'
            f'margin-bottom:.35rem">'
            f'<span style="font-family:\'IBM Plex Mono\',monospace;font-size:.95rem;'
            f'font-weight:700;color:{farbe["text"]}">{norm_data["norm"]}</span>'
            f'{typ_badge}</div>'
            f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.82rem;'
            f'font-weight:600;color:{farbe["text"]};margin-bottom:.3rem;line-height:1.35">'
            f'{norm_data["titel"]}</div>'
            f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.76rem;'
            f'color:rgba(255,255,255,.8);line-height:1.55">{norm_data["inhalt"]}</div>'
            f'{verb_html}'
            f'{link_btn}'
            f'</div>'
        )

        with cols[idx % 3]:
            st.markdown(card_html, unsafe_allow_html=True)

    # Klausurfallen
    if netz.get("klausurfallen"):
        gold_divider()
        section_header("⚠️", "Häufige Klausurfallen")
        fallen_items = "".join(
            f'<li style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.83rem;'
            f'color:#44403c;margin-bottom:.4rem;line-height:1.5">{f}</li>'
            for f in netz["klausurfallen"]
        )
        st.markdown(
            f'<ul style="background:rgba(220,38,38,.04);border:1px solid rgba(220,38,38,.15);'
            f'border-left:3px solid #dc2626;border-radius:8px;padding:.75rem 1rem .75rem 2rem;'
            f'margin:0">{fallen_items}</ul>',
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — PRÜFUNGSSCHEMA
# ─────────────────────────────────────────────────────────────────────────────
with tab_schema:
    schema = netz.get("schema", [])

    if not schema:
        st.info("Kein Prüfungsschema für dieses Thema hinterlegt.")
    else:
        section_header("📋", f"Prüfungsschema — {thema}")

        st.markdown(
            f'<div style="background:white;border:1px solid #edeae0;border-radius:10px;'
            f'padding:1.25rem 1.5rem;box-shadow:0 1px 4px rgba(26,39,68,.07)">',
            unsafe_allow_html=True,
        )

        for schritt in schema:
            # Einrückungstiefe bestimmen
            stripped = schritt.lstrip()
            indent = len(schritt) - len(stripped)

            if stripped.startswith(("I.", "II.", "III.", "IV.")):
                # Hauptstufe
                st.markdown(
                    f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.9rem;'
                    f'font-weight:700;color:#1a2744;padding:.45rem 0 .15rem;'
                    f'border-bottom:1px solid #edeae0;margin-bottom:.3rem">{stripped}</div>',
                    unsafe_allow_html=True,
                )
            elif stripped[0].isdigit() and "." in stripped[:3]:
                # Nummerierte Ebene
                st.markdown(
                    f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.85rem;'
                    f'font-weight:600;color:#243460;padding:.3rem 0 .1rem;'
                    f'margin-left:{indent * 4}px">{stripped}</div>',
                    unsafe_allow_html=True,
                )
            elif stripped.startswith(("a)", "b)", "c)", "d)", "e)")):
                # Buchstabenebene
                st.markdown(
                    f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.82rem;'
                    f'color:#44403c;padding:.2rem 0;margin-left:{max(indent, 3) * 5}px">{stripped}</div>',
                    unsafe_allow_html=True,
                )
            elif stripped.startswith("→"):
                # Pfeil-Hinweis
                st.markdown(
                    f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.8rem;'
                    f'color:#92400e;padding:.2rem 0;margin-left:{max(indent, 6) * 4}px;'
                    f'font-style:italic">{stripped}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.82rem;'
                    f'color:#57534e;padding:.18rem 0;margin-left:{indent * 4}px">{stripped}</div>',
                    unsafe_allow_html=True,
                )

        st.markdown("</div>", unsafe_allow_html=True)

    # Verbindungsübersicht
    gold_divider()
    section_header("🔗", "Verbindungen auf einen Blick")

    all_connections: list[tuple[str, str]] = []
    for n in netz["normen"]:
        for v in n.get("verbindungen", []):
            all_connections.append((n["norm"], v))

    if all_connections:
        conn_cols = st.columns(2)
        for i, (src, dst) in enumerate(all_connections):
            with conn_cols[i % 2]:
                st.markdown(
                    f'<div style="display:flex;align-items:center;gap:.5rem;'
                    f'background:white;border:1px solid #edeae0;border-radius:6px;'
                    f'padding:.35rem .7rem;margin-bottom:.3rem;font-size:.78rem">'
                    f'<span style="font-family:\'IBM Plex Mono\',monospace;font-weight:600;'
                    f'color:#1a2744">{src}</span>'
                    f'<span style="color:#c9a84c;font-size:1rem">→</span>'
                    f'<span style="font-family:\'IBM Plex Mono\',monospace;font-weight:600;'
                    f'color:#243460">{dst}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
    else:
        st.caption("Keine Verbindungen hinterlegt.")

# ─────────────────────────────────────────────────────────────────────────────
# KI-ANALYSE
# ─────────────────────────────────────────────────────────────────────────────

gold_divider()
section_header("🤖", "KI-Analyse")

st.markdown(
    '<p style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.84rem;color:#57534e;'
    'margin-bottom:.75rem">Lass dir das Normennetz von Claude erklären: Zusammenhänge, '
    'Prüfungsreihenfolge und typische Klausurfallen.</p>',
    unsafe_allow_html=True,
)

analyse_cache_key = f"nn_analyse_{thema}"

if st.button("🤖 KI-Analyse starten", type="primary", key="nn_ki_btn"):
    # Normenliste für Prompt aufbereiten
    normen_liste = "\n".join(
        f"- {n['norm']}: {n['titel']} — {n['inhalt'][:120]}..."
        for n in netz["normen"]
    )
    schema_liste = "\n".join(netz.get("schema", []))

    system_prompt = (
        "Du bist ein erfahrener Jurist und Examenscoach. Du erklärst Normennetze klar, "
        "strukturiert und examensrelevant. Du gehst auf Zusammenhänge zwischen den Normen, "
        "den richtigen Prüfungsaufbau und typische Fehler in Klausuren ein. "
        "Verwende Markdown-Formatierung. Halte dich an max. 600 Wörter."
    )
    user_msg = (
        f"Erkläre das Normennetz zum Thema **{thema}** ({netz.get('rechtsgebiet', '')}).\n\n"
        f"Normen:\n{normen_liste}\n\n"
        f"Prüfungsschema:\n{schema_liste}\n\n"
        "Erkläre:\n"
        "1. Wie hängen die Normen systematisch zusammen?\n"
        "2. Wo liegt die praktische Prüfungsreihenfolge?\n"
        "3. Welche Normen werden in Klausuren am häufigsten falsch angewendet?\n"
        "4. Merksatz/Eselsbrücke für das Normennetz."
    )

    with st.spinner("Claude analysiert das Normennetz …"):
        result_chunks = []
        result_placeholder = st.empty()
        full_text = ""
        for chunk in chat_stream(
            messages=[{"role": "user", "content": user_msg}],
            system_prompt=system_prompt,
        ):
            full_text += chunk
            result_placeholder.markdown(full_text)
        st.session_state[analyse_cache_key] = full_text

elif analyse_cache_key in st.session_state:
    st.markdown(st.session_state[analyse_cache_key])
    st.caption(f"Gespeicherte Analyse für **{thema}** (aus Cache)")

gold_divider()

st.markdown(
    '<p style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.73rem;'
    'color:#78716c;text-align:center">'
    'Normennetze basieren auf dem aktuellen Stand des BGB, StGB, VwVfG und GG. '
    'Normtexte: <strong>gesetze-im-internet.de</strong></p>',
    unsafe_allow_html=True,
)

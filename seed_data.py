# seed_data.py – Vorausgefüllte juristische Lernmaterialien für den Jura-Repetitor
# Jeder Eintrag enthält examensrelevante Lerntexte zu zentralen Rechtsgebieten.

SEED_MATERIALS = [
    # ─────────────────────────────────────────────────────────────
    # GESETZGEBUNG – Normen erklären
    # ─────────────────────────────────────────────────────────────
    {
        "name": "BGB AT – Willenserklärung §§ 116-144",
        "topic": "Bürgerliches Recht – Allgemeiner Teil",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "Die Willenserklärung ist die zentrale Grundlage jedes Rechtsgeschäfts. "
            "Sie besteht aus einem subjektiven und einem objektiven Tatbestand. "
            "Objektiv muss eine Erklärung nach außen vorliegen, die auf den Eintritt einer Rechtsfolge gerichtet ist. "
            "Subjektiv sind Handlungswille, Erklärungsbewusstsein und Geschäftswille zu unterscheiden.\n\n"
            "Das Erklärungsbewusstsein (Rechtsbindungswille) ist str. diskutiert: "
            "Nach h.M. genügt das potentielle Erklärungsbewusstsein – wer bei Anwendung der im Verkehr erforderlichen Sorgfalt hätte erkennen können und müssen, "
            "dass seine Äußerung als Willenserklärung aufgefasst werden würde, ist daran gebunden.\n\n"
            "Auslegung (§§ 133, 157 BGB): Empfangsbedürftige Willenserklärungen sind so auszulegen, "
            "wie der Empfänger sie nach Treu und Glauben und mit Rücksicht auf die Verkehrssitte verstehen durfte. "
            "Maßgeblich ist der objektivierte Empfängerhorizont, nicht der subjektive Wille des Erklärenden. "
            "Bei nicht empfangsbedürftigen Erklärungen gilt der wirkliche Wille (§ 133 BGB).\n\n"
            "Geheimvorbehalt (§ 116 BGB): Behält sich der Erklärende insgeheim vor, das Erklärte nicht zu wollen, "
            "ist die Erklärung grundsätzlich wirksam; der Vorbehalt ist unbeachtlich. "
            "Ausnahme: War der Vorbehalt dem Empfänger bekannt, ist die Erklärung nichtig.\n\n"
            "Scheingeschäft (§ 117 BGB): Sind sich beide Parteien einig, dass die Erklärung nur zum Schein abgegeben wird, "
            "ist das Scheingeschäft nichtig. Ein durch das Scheingeschäft verdecktes Rechtsgeschäft ist nach § 117 II BGB zu beurteilen "
            "und kann wirksam sein.\n\n"
            "Scherzerklärung (§ 118 BGB): Eine im Bewusstsein der Nichtigkeit abgegebene Erklärung ist nichtig. "
            "Schadensersatz nach § 122 BGB ist aber möglich.\n\n"
            "Anfechtung (§§ 119–124 BGB): Die Willenserklärung kann angefochten werden bei:\n"
            "- Inhaltsirrtum (§ 119 I Alt. 1): Erklärender irrt über den Sinn der Erklärung.\n"
            "- Erklärungsirrtum (§ 119 I Alt. 2): Versprechen, Verschreiben, Vergreifen.\n"
            "- Eigenschaftsirrtum (§ 119 II): Irrtum über verkehrswesentliche Eigenschaft.\n"
            "- Täuschung/Drohung (§ 123): kein Ersatz nach § 122, aber Schadensersatz nach §§ 280, 311 II, 241 II BGB möglich.\n\n"
            "Rechtsfolge der Anfechtung: ex-tunc-Nichtigkeit (§ 142 I BGB), Schadensersatz aus § 122 BGB "
            "(negatives Interesse, begrenzt auf das Erfüllungsinteresse). "
            "Anfechtungsfrist: § 121 (unverzüglich) bzw. § 124 (1 Jahr/10 Jahre).\n\n"
            "Zugang (§ 130 BGB): Die Erklärung wird wirksam mit Zugang, d.h. wenn sie so in den Machtbereich des Empfängers "
            "gelangt ist, dass dieser unter normalen Umständen Kenntnis nehmen kann. Bei Briefen: Einwurf in Briefkasten zu einer Zeit, "
            "zu der mit Leerung zu rechnen ist. Elektronische Erklärungen gehen zu, wenn sie in der Mailbox des Empfängers abrufbar sind.\n\n"
            "Examenstipp: Im Gutachten stets prüfen: (1) objektiver Tatbestand – Auslegung nach §§ 133, 157 BGB; "
            "(2) subjektiver Tatbestand – fehlender Handlungswille oder Erklärungsbewusstsein?; "
            "(3) Wirksamwerden – Zugang nach § 130 BGB; (4) Anfechtbarkeit §§ 119 ff. BGB."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 116-144 BGB",
    },
    {
        "name": "BGB AT – Stellvertretung §§ 164-181",
        "topic": "Bürgerliches Recht – Allgemeiner Teil",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "Die Stellvertretung ermöglicht es, dass eine Person (Vertreter) für eine andere (Vertretener) Rechtsgeschäfte vornimmt, "
            "die unmittelbar für und gegen den Vertretenen wirken (§ 164 I BGB).\n\n"
            "Voraussetzungen der wirksamen Stellvertretung:\n"
            "1. Eigene Willenserklärung des Vertreters (keine Botenschaft)\n"
            "2. Im Namen des Vertretenen (Offenkundigkeitsprinzip, § 164 I BGB). "
            "   Handeln ohne erkennbaren Fremdbezug ist Eigengeschäft (Ausnahme: Geschäft für den, den es angeht).\n"
            "3. Mit Vertretungsmacht: durch Vollmacht (rechtsgeschäftlich), Gesetz oder Organ-/Amtsstellung.\n\n"
            "Vollmacht (§§ 166-176 BGB): Die Vollmacht ist eine einseitige, empfangsbedürftige Willenserklärung. "
            "Sie kann gegenüber dem Vertreter (Innenvollmacht) oder dem Dritten (Außenvollmacht, § 167 I Alt. 2 BGB) erteilt werden. "
            "Grundsatz: Vollmacht ist formfrei, auch wenn das Grundgeschäft formbedürftig ist (§ 167 II BGB). "
            "Ausnahmen durch Rspr. (z.B. Grundstücksgeschäfte).\n\n"
            "Arten der Vollmacht:\n"
            "- Generalvollmacht: unbeschränkt\n"
            "- Spezialvollmacht: nur für bestimmte Geschäfte\n"
            "- Prokura (§§ 48 ff. HGB): handelsrechtliche Sonderform\n"
            "- Duldungsvollmacht: Vertretener duldet wissentlich das Auftreten des Vertreters\n"
            "- Anscheinsvollmacht: Vertretener hätte bei Sorgfalt das Auftreten erkennen können\n\n"
            "Erlöschen der Vollmacht (§ 168 BGB): durch Widerruf, Zeitablauf, Zweckerreichung, Tod (str.).\n\n"
            "Missbrauch der Vertretungsmacht: Vertreter handelt im Rahmen der formalen Vollmacht, aber entgegen dem Innenverhältnis. "
            "Grundsätzlich wirksam für den Dritten. Ausnahme: Kollusion (§ 138 BGB) oder evident missbräuchliches Handeln "
            "(Einwand des § 242 BGB, der Dritte handelt arglistig).\n\n"
            "Vertreter ohne Vertretungsmacht (§§ 177-180 BGB): "
            "Handelt jemand ohne Vertretungsmacht, ist das Geschäft schwebend unwirksam. "
            "Genehmigung des Vertretenen (§ 177 BGB) macht es rückwirkend wirksam. "
            "Verweigerung der Genehmigung: Vertreter haftet dem Dritten nach § 179 BGB "
            "(Erfüllung oder Schadensersatz), es sei denn, der Dritte kannte den Mangel.\n\n"
            "Insichgeschäft (§ 181 BGB): Ein Vertreter darf nicht im Namen des Vertretenen mit sich selbst "
            "ein Rechtsgeschäft vornehmen (Verbot des Insichgeschäfts), da Interessenkollision droht. "
            "Ausnahmen: Befreiung durch den Vertretenen, Erfüllung einer Verbindlichkeit.\n\n"
            "Wissenszurechnung (§ 166 BGB): Maßgeblich ist grundsätzlich das Wissen des Vertreters, nicht des Vertretenen. "
            "Ausnahme § 166 II BGB: Weisungsgebundener Vertreter – Kenntnis des Vertretenen relevant.\n\n"
            "Examenstipp: Im Gutachten stets prüfen: (1) Eigene WE des Vertreters? (2) Im fremden Namen? "
            "(3) Mit Vertretungsmacht? Fehlt einer dieser Punkte, keine wirksame Stellvertretung."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 164-181 BGB",
    },
    {
        "name": "SchuldR AT – Schadensersatz §§ 280-284 BGB",
        "topic": "Schuldrecht – Allgemeiner Teil",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "Der zentrale Schadensersatzanspruch im Schuldrecht ergibt sich aus § 280 I BGB: "
            "Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, kann der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen. "
            "Dies gilt nicht, wenn der Schuldner die Pflichtverletzung nicht zu vertreten hat.\n\n"
            "Voraussetzungen des § 280 I BGB:\n"
            "1. Schuldverhältnis (vertraglich, gesetzlich, vorvertraglich)\n"
            "2. Pflichtverletzung: Verletzung einer Haupt- oder Nebenpflicht (§ 241 II BGB)\n"
            "3. Vertretenmüssen (§§ 276-278 BGB): Vorsatz oder Fahrlässigkeit; Verschulden wird vermutet (Beweislastumkehr!)\n"
            "4. Schaden (Differenzhypothese: Vergleich Vermögen mit/ohne Pflichtverletzung)\n\n"
            "Qualifizierte Voraussetzungen für Folgetatbestände:\n"
            "- § 280 II i.V.m. § 286 BGB (Verzugsschaden): zusätzlich Mahnung und Verzug\n"
            "- § 280 III i.V.m. § 281 BGB (Schadensersatz statt der Leistung): Fristsetzung + Fristablauf\n"
            "- § 280 III i.V.m. § 283 BGB: nachträgliche Unmöglichkeit\n"
            "- § 280 III i.V.m. § 282 BGB: unzumutbare Weiterleistung wegen Nebenpflichtverletzung\n\n"
            "Verschulden (§ 276 BGB):\n"
            "- Vorsatz: Wissen und Wollen der Tatbestandsverwirklichung\n"
            "- Fahrlässigkeit: Außerachtlassen der im Verkehr erforderlichen Sorgfalt (objektiver Maßstab!)\n"
            "- Haftungserleichterungen möglich (§ 276 I S. 2), aber kein Haftungsausschluss für Vorsatz (§ 276 III)\n"
            "- § 278 BGB: Haftung für Erfüllungsgehilfen wie für eigenes Verschulden (kein Exkulpationsbeweis!)\n\n"
            "Schaden und Schadensberechnung:\n"
            "- Differenzhypothese: Vergleich des tatsächlichen Vermögens mit dem hypothetischen ohne das schädigende Ereignis\n"
            "- Naturalrestitution (§ 249 I BGB) hat Vorrang vor Geldersatz\n"
            "- Geldersatz bei Unmöglichkeit oder Unverhältnismäßigkeit (§ 251 BGB)\n"
            "- Mitverschulden des Gläubigers mindert Anspruch (§ 254 BGB)\n\n"
            "§ 284 BGB – Ersatz vergeblicher Aufwendungen: "
            "Statt Schadensersatz statt der Leistung kann der Gläubiger Aufwendungen ersetzt verlangen, "
            "die er im Vertrauen auf den Erhalt der Leistung gemacht hat. Voraussetzung: Aufwendungen waren nicht ohnehin nutzlos.\n\n"
            "Verhältnis der Tatbestände: § 280 I ist Grundtatbestand. §§ 281-283 erfordern zusätzlich den Wegfall des Primäranspruchs. "
            "§ 281 IV BGB: Rücktritt und Schadensersatz sind kumulierbar (§ 325 BGB). "
            "§ 311a BGB: Schadensersatz bei anfänglicher Unmöglichkeit, wenn Schuldner den Mangel bei Vertragsschluss kannte.\n\n"
            "Examenstipp: Beim Schadensersatz statt der Leistung (§§ 280 III, 281 BGB) stets die Fristsetzung prüfen! "
            "Ausnahmen in § 281 II BGB (ernsthafte Erfüllungsverweigerung, relative Fixschuld)."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 280-284 BGB",
    },
    {
        "name": "SchuldR BT – Kaufvertrag §§ 433-453 BGB",
        "topic": "Schuldrecht – Besonderer Teil",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "Der Kaufvertrag (§ 433 BGB) ist das praktisch wichtigste Schuldverhältnis. "
            "Beim Kauf verpflichtet sich der Verkäufer, dem Käufer die Sache zu übergeben und das Eigentum zu verschaffen. "
            "Der Käufer verpflichtet sich zur Zahlung des Kaufpreises und zur Abnahme der Sache.\n\n"
            "Pflichten des Verkäufers (§ 433 I BGB):\n"
            "- Übergabe der Sache (Besitzverschaffung)\n"
            "- Verschaffung des Eigentums (§§ 929 ff. BGB)\n"
            "- Frei von Sach- und Rechtsmängeln (§ 433 I S. 2 BGB)\n\n"
            "Sachmangel (§ 434 BGB): Eine Sache ist mangelhaft, wenn sie nicht die vereinbarte Beschaffenheit hat (§ 434 I Nr. 1), "
            "sich nicht für die vertraglich vorausgesetzte Verwendung eignet (§ 434 I Nr. 2), "
            "oder nicht die übliche Beschaffenheit aufweist und der Käufer die übliche Beschaffenheit erwarten durfte (§ 434 I Nr. 3). "
            "Seit der Schuldrechtsreform 2022: öffentliche Äußerungen des Herstellers (Werbung) können Beschaffenheit begründen. "
            "Auch Montagefehler gem. § 434 IV BGB und Falsch- und Zuweniglieferung gem. § 434 III BGB sind Sachmängel.\n\n"
            "Rechtsmangel (§ 435 BGB): Dritte können gegen den Käufer Rechte geltend machen (z.B. Eigentum, beschränkte dingliche Rechte).\n\n"
            "Gewährleistungsrechte (§§ 437-441 BGB):\n"
            "Bei Mangel beim Gefahrübergang (§ 446 BGB) hat der Käufer folgende Rechte:\n"
            "1. Nacherfüllung (§§ 437 Nr. 1, 439 BGB) – Vorrang!\n"
            "   Käufer kann Nachbesserung oder Neulieferung verlangen. "
            "   Verkäufer kann die gewählte Art verweigern, wenn unverhältnismäßig teuer.\n"
            "2. Rücktritt (§§ 437 Nr. 2, 440, 323, 326 V BGB) – nach erfolgloser Fristsetzung\n"
            "3. Minderung (§§ 437 Nr. 2, 441 BGB)\n"
            "4. Schadensersatz (§§ 437 Nr. 3, 440, 280, 281, 283, 311a BGB)\n"
            "5. Aufwendungsersatz (§§ 437 Nr. 3, 284 BGB)\n\n"
            "Verjährung: § 438 BGB: Grundsätzlich 2 Jahre ab Ablieferung; "
            "bei Bauwerken 5 Jahre; arglistiges Verschweigen → regelmäßige Verjährung (§ 195: 3 Jahre).\n\n"
            "Verbrauchsgüterkauf (§§ 474 ff. BGB): Sonderregelung beim B2C-Kauf. "
            "Beweislastumkehr nach § 477 BGB: Mangel wird bei Auftreten innerhalb von 1 Jahr vermutet als bei Gefahrübergang vorhanden. "
            "AGB-Einschränkungen sind weitgehend unzulässig.\n\n"
            "Gefahrübergang (§ 446 BGB): Mit Übergabe der Kaufsache geht die Preisgefahr auf den Käufer über. "
            "Beim Versendungskauf (§ 447 BGB) mit Übergabe an die Transportperson, aber im Verbrauchsgüterkauf erst bei Ablieferung.\n\n"
            "Examenstipp: Bei Sachmangel-Klausuren stets prüfen: (1) Kaufvertrag geschlossen? "
            "(2) Mangel i.S.d. § 434 BGB? (3) Bei Gefahrübergang vorhanden? (4) Fristsetzung zur Nacherfüllung? (5) Richtige Rechtsfolge."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 433-453 BGB",
    },
    {
        "name": "StGB AT – Vorsatz und Fahrlässigkeit §§ 15-16 StGB",
        "topic": "Strafrecht – Allgemeiner Teil",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "§ 15 StGB normiert, dass nur vorsätzliches Handeln strafbar ist, soweit das Gesetz fahrlässiges Handeln nicht ausdrücklich mit Strafe bedroht. "
            "Die Unterscheidung von Vorsatz und Fahrlässigkeit ist damit von grundlegender Bedeutung.\n\n"
            "Vorsatz: Vorsatz ist das Wissen und Wollen der Tatbestandsverwirklichung (klassische Definition). "
            "Unterschieden werden:\n\n"
            "1. Dolus directus 1. Grades (Absicht): Der Täter handelt mit dem zielgerichteten Willen, den Taterfolg herbeizuführen. "
            "   Der Erfolg ist dem Täter gerade auf die Verwirklichung seines Handlungsziels gerichtet. "
            "   Auf das Wissen kommt es weniger an als auf den Willen.\n\n"
            "2. Dolus directus 2. Grades (sicheres Wissen): Der Täter hält den Eintritt des Tatbestandserfolges für sicher, "
            "   auch wenn dieser nicht sein eigentliches Handlungsziel ist (sog. notwendige Nebenfolge).\n\n"
            "3. Dolus eventualis (bedingter Vorsatz): Der Täter hält die Tatbestandsverwirklichung für möglich und nimmt sie "
            "   billigend in Kauf bzw. findet sich mit ihr ab. "
            "   Abgrenzung zur bewussten Fahrlässigkeit ist die wichtigste und schwierigste Abgrenzungsfrage im StGB AT!\n\n"
            "Abgrenzung dolus eventualis / bewusste Fahrlässigkeit – Theorien:\n"
            "- Billigungstheorie (BGH): Vorsatz, wenn der Täter den Erfolg billigend in Kauf nimmt; Fahrlässigkeit, wenn er ernsthaft darauf vertraute, "
            "  der Erfolg werde ausbleiben (BGHSt 7, 363 – Lederriemen-Fall).\n"
            "- Möglichkeitstheorie: Vorsatz bereits bei Für-möglich-Halten und Vorausnehmen des Erfolges.\n"
            "- Risikotheorie: Vorsatz, wenn das Risiko außerhalb des sozialadäquaten Rahmens liegt.\n\n"
            "Fahrlässigkeit: § 276 II BGB-Maßstab gilt sinngemäß: Außerachtlassen der im Verkehr erforderlichen Sorgfalt.\n\n"
            "- Bewusste Fahrlässigkeit (luxuria): Täter erkennt die Möglichkeit des Erfolgseintritts, "
            "  vertraut aber pflichtwidrig-leichtfertig auf dessen Ausbleiben.\n"
            "- Unbewusste Fahrlässigkeit (negligentia): Täter erkennt die Gefahr nicht, obwohl er sie bei Anwendung der "
            "  erforderlichen Sorgfalt hätte erkennen können und müssen.\n\n"
            "Irrtum über Tatumstände (§ 16 StGB): "
            "Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört, handelt nicht vorsätzlich. "
            "§ 16 I S. 2 StGB: Fahrlässigkeitsstrafbarkeit bleibt möglich. "
            "Abzugrenzen vom Verbotsirrtum (§ 17 StGB), der nur die Schuld betrifft.\n\n"
            "Prüfungsschema Fahrlässigkeitsdelikt: (1) Tatbestand: Sorgfaltspflichtverletzung, Kausalität, objektive Zurechnung, "
            "objektive Vorhersehbarkeit; (2) Rechtswidrigkeit; (3) Schuld: subjektive Vorhersehbarkeit, individuelle Sorgfaltsfähigkeit.\n\n"
            "Examenstipp: Im Gutachten beim Vorsatz stets alle drei Vorsatzformen kurz ansprechen und dann die relevante herausarbeiten. "
            "Bei dolus eventualis die Abgrenzung zur bewussten Fahrlässigkeit mit der BGH-Billigungstheorie begründen."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 15-16 StGB; BGHSt 7, 363",
    },
    {
        "name": "GG – Grundrechtsprüfung Art. 1-19 GG",
        "topic": "Öffentliches Recht – Verfassungsrecht",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "Die Grundrechtsprüfung folgt einem einheitlichen dreistufigen Schema, "
            "das unabhängig vom jeweiligen Grundrecht angewendet wird.\n\n"
            "Stufe 1 – Schutzbereich:\n"
            "Zunächst ist der persönliche und sachliche Schutzbereich zu bestimmen.\n"
            "- Persönlicher Schutzbereich: Wer kann sich auf das Grundrecht berufen? "
            "  Jedermann-Grundrechte (z.B. Art. 2, 4, 5 GG) vs. Deutschengrundrechte (z.B. Art. 8, 9, 12 GG). "
            "  Juristische Personen: Art. 19 III GG, soweit das Grundrecht dem Wesen nach anwendbar ist.\n"
            "- Sachlicher Schutzbereich: Welche Verhaltensweisen, Zustände oder Positionen werden geschützt? "
            "  Strenge Definition: Nur Verhaltensweisen, die unter den Schutzbereich fallen, können beeinträchtigt sein.\n\n"
            "Stufe 2 – Eingriff:\n"
            "Klassischer Eingriffsbegriff: staatliches Handeln, das final, unmittelbar, rechtsförmig und imperativ "
            "in den Schutzbereich eingreift. Moderner Eingriffsbegriff (h.M.): jedes staatliche Handeln mit zurechenbarer "
            "Beeinträchtigung des Schutzbereichs, unabhängig von Finalität und Rechtsförmigkeit (auch mittelbare, faktische Eingriffe).\n\n"
            "Stufe 3 – Verfassungsrechtliche Rechtfertigung:\n"
            "a) Schranken: Welche Einschränkungen erlaubt das Grundrecht?\n"
            "   - Einfacher Gesetzesvorbehalt: Einschränkung durch oder aufgrund eines Gesetzes möglich (z.B. Art. 2 I, 12 I GG)\n"
            "   - Qualifizierter Gesetzesvorbehalt: Einschränkung nur unter bestimmten Voraussetzungen (z.B. Art. 13 III GG)\n"
            "   - Schrankenlos gewährleistete Grundrechte (Art. 1 I, 4 I, II GG): nur durch kollidierende Verfassungsgüter einschränkbar\n\n"
            "b) Schranken-Schranken (Verhältnismäßigkeit!):\n"
            "   - Gesetzesvorbehalt und formelle Anforderungen erfüllt?\n"
            "   - Zitiergebot (Art. 19 I S. 2 GG) bei Einschränkung von Grundrechten mit ausdrücklichem Gesetzesvorbehalt\n"
            "   - Wesensgehaltgarantie (Art. 19 II GG): kein Antasten des Wesensgehalts\n"
            "   - Verhältnismäßigkeitsgrundsatz (Art. 20 III GG i.V.m. Rechtsstaatsprinzip):\n"
            "     * Legitimer Zweck\n"
            "     * Geeignetheit: Maßnahme fördert den Zweck\n"
            "     * Erforderlichkeit: kein milderes, gleich geeignetes Mittel\n"
            "     * Angemessenheit (Verhältnismäßigkeit i.e.S.): Zweck-Mittel-Relation nicht außer Verhältnis\n\n"
            "Besonderheiten einzelner Grundrechte:\n"
            "- Art. 3 I GG (Gleichheitssatz): kein Eingriffs-Rechtfertigungs-Schema, sondern Vergleichsgruppenbildung und Differenzierungsgrund\n"
            "- Art. 14 GG (Eigentum): Unterscheidung Sozialbindung (§ 14 II GG) vs. Enteignung (§ 14 III GG)\n"
            "- Art. 1 I GG (Menschenwürde): absolutes, schrankenlos gewährleistetes Grundrecht\n\n"
            "Leitentscheidungen:\n"
            "- BVerfGE 7, 377 (Lüth): Grundrechte als objektive Wertordnung; Verhältnismäßigkeit bei Meinungsfreiheit\n"
            "- BVerfGE 65, 1 (Volkszählung): informationelle Selbstbestimmung; strengste Verhältnismäßigkeitsprüfung\n"
            "- BVerfGE 120, 274 (Online-Durchsuchung): IT-Grundrecht als neues Grundrecht aus Art. 2 I i.V.m. 1 I GG\n\n"
            "Examenstipp: Im öffentlich-rechtlichen Klausuraufbau: Erst Zulässigkeit des Rechtswegs und der Klage prüfen, "
            "dann in der Begründetheit das Grundrechtsschema abarbeiten."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "Art. 1-19 GG; BVerfGE 7, 377 (Lüth); BVerfGE 65, 1 (Volkszählung)",
    },
    {
        "name": "VwGO – Verwaltungsgerichtsbarkeit §§ 40-113 VwGO",
        "topic": "Öffentliches Recht – Verwaltungsrecht",
        "art": "Skript",
        "kategorie": "Gesetzgebung",
        "text": (
            "Die Verwaltungsgerichtsordnung (VwGO) regelt den Rechtsschutz gegen Maßnahmen der öffentlichen Verwaltung.\n\n"
            "Eröffnung des Verwaltungsrechtswegs (§ 40 I VwGO):\n"
            "Der Verwaltungsrechtsweg ist eröffnet, wenn eine öffentlich-rechtliche Streitigkeit nicht-verfassungsrechtlicher Art vorliegt "
            "und keine abdrängende Sonderzuweisung besteht. Abgrenzung öffentl. Recht / Privatrecht: "
            "Modifizierte Subjektstheorie (h.M.): Norm, die nur einen Hoheitsträger berechtigt/verpflichtet, ist öffentlich-rechtlich.\n\n"
            "Klagearten:\n\n"
            "1. Anfechtungsklage (§ 42 I Alt. 1 VwGO): Ziel: Aufhebung eines belastenden Verwaltungsakts (VA). "
            "   Besondere Zulässigkeitsvoraussetzungen: Klagebefugnis (Möglichkeit der Verletzung in eigenen Rechten, § 42 II VwGO), "
            "   Vorverfahren (§§ 68 ff. VwGO – Widerspruch), Klagefrist (§ 74 VwGO: 1 Monat nach Zustellung des Widerspruchsbescheids). "
            "   Begründetheit: VA rechtswidrig + Kläger in seinen Rechten verletzt (§ 113 I S. 1 VwGO).\n\n"
            "2. Verpflichtungsklage (§ 42 I Alt. 2 VwGO): Ziel: Erlass eines abgelehnten/unterlassenen VA. "
            "   Versagungsgegenklage vs. Untätigkeitsklage (§ 75 VwGO). "
            "   Begründetheit: Kläger hat Anspruch auf den begehrten VA (§ 113 V VwGO).\n\n"
            "3. Allgemeine Leistungsklage: Ziel: Vornahme eines tatsächlichen Verwaltungshandelns, das kein VA ist. "
            "   Keine ausdrückliche Regelung in VwGO, aber allgemein anerkannt.\n\n"
            "4. Feststellungsklage (§ 43 VwGO): Ziel: Feststellung des Bestehens/Nichtbestehens eines Rechtsverhältnisses "
            "   oder Nichtigkeit eines VA. Subsidiarität gegenüber Gestaltungs- und Leistungsklage.\n\n"
            "5. Normenkontrolle (§ 47 VwGO): Überprüfung von Rechtsnormen unterhalb von Bundesgesetzen "
            "   (v.a. Bebauungspläne). Antrag beim OVG/VGH.\n\n"
            "Allgemeine Zulässigkeitsvoraussetzungen:\n"
            "- Verwaltungsrechtsweg (§ 40 VwGO)\n"
            "- Zuständiges Gericht (örtlich, sachlich)\n"
            "- Beteiligtenfähigkeit (§ 61 VwGO)\n"
            "- Prozessfähigkeit (§ 62 VwGO)\n"
            "- Statthafte Klageart\n"
            "- Klagebefugnis (§ 42 II VwGO analog)\n"
            "- Rechtsschutzbedürfnis\n\n"
            "Einstweiliger Rechtsschutz:\n"
            "- § 80 VwGO: Aufschiebende Wirkung von Widerspruch und Anfechtungsklage (Grundsatz), "
            "  Ausnahmen in § 80 II VwGO (z.B. Steuern, besonderes öffentliches Interesse).\n"
            "- § 80 V VwGO: Antrag auf Wiederherstellung der aufschiebenden Wirkung beim Verwaltungsgericht.\n"
            "- § 123 VwGO: Einstweilige Verfügung / Anordnung bei allgemeiner Leistungsklage.\n\n"
            "Examenstipp: Zulässigkeit immer vollständig durchprüfen, bevor zur Begründetheit übergegangen wird. "
            "Bei Anfechtungsklage die dreistufige Begründetheitsprüfung: formelle Rechtmäßigkeit, materielle Rechtmäßigkeit, "
            "Rechtsverletzung des Klägers."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 40-113 VwGO",
    },

    # ─────────────────────────────────────────────────────────────
    # RECHTSPRECHUNG – Leitentscheidungen
    # ─────────────────────────────────────────────────────────────
    {
        "name": "BVerfG – Verhältnismäßigkeitsgrundsatz",
        "topic": "Öffentliches Recht – Verfassungsrecht",
        "art": "Kommentarauszug",
        "kategorie": "Rechtsprechung",
        "text": (
            "Der Verhältnismäßigkeitsgrundsatz (auch: Übermaßverbot) ist ein aus dem Rechtsstaatsprinzip (Art. 20 III GG) "
            "und dem Wesen der Grundrechte abgeleiteter allgemeiner Verfassungsgrundsatz "
            "(BVerfGE 19, 342; st. Rspr.). Er gilt für jede staatliche Maßnahme, die in Grundrechte eingreift.\n\n"
            "Die vier Teilgrundsätze:\n\n"
            "1. Legitimer Zweck:\n"
            "Der mit der Maßnahme verfolgte Zweck muss verfassungsrechtlich legitim sein. "
            "Ein Zweck, der gegen die Verfassung verstößt (z.B. Diskriminierung aus rassischen Gründen), "
            "kann nicht als legitimer Zweck anerkannt werden. "
            "Maßstab: Zweck muss dem Gemeinwohl dienen oder auf einem anderen anerkennungswürdigen Ziel beruhen.\n\n"
            "2. Geeignetheit:\n"
            "Die Maßnahme muss geeignet sein, den angestrebten Zweck zu fördern. "
            "Es genügt, dass die Maßnahme den Zweck fördert – ein vollständiges Erreichen ist nicht erforderlich. "
            "BVerfG übt zurückhaltende Kontrolle (Einschätzungsprärogative des Gesetzgebers). "
            "Ungeeignet ist eine Maßnahme, wenn sie den Zweck überhaupt nicht fördern kann oder sogar kontraproduktiv ist "
            "(BVerfGE 67, 157 – Anachronistischer Zug).\n\n"
            "3. Erforderlichkeit (milderes Mittel):\n"
            "Unter mehreren gleich geeigneten Mitteln ist das den Grundrechtsträger am wenigsten belastende zu wählen. "
            "Beispiel: BVerfGE 53, 135 (Schallschutz): Statt Nachtflugverbot hätte technischer Lärmschutz gereicht. "
            "Achtung: Das mildere Mittel muss gleich geeignet sein – ein weniger geeignetes Mittel ist kein taugliches milderes Mittel!\n\n"
            "4. Angemessenheit (Verhältnismäßigkeit i.e.S.):\n"
            "Die Maßnahme darf nicht außer Verhältnis zum verfolgten Zweck stehen. "
            "Es ist eine Abwägung zwischen dem Gewicht des Eingriffs und der Bedeutung des verfolgten Zwecks vorzunehmen. "
            "Dies ist das eigentliche Wertungsproblem und der Hauptanwendungsfall richterlicher Kontrolle. "
            "Beispiel: BVerfGE 90, 145 (Cannabis): Auch bei gefährlichen Drogen kann ein absolutes Verbot unverhältnismäßig sein, "
            "wenn die Eingriffsintensität die Schutzwirkung deutlich übersteigt.\n\n"
            "Wichtige Leitentscheidungen:\n"
            "- BVerfGE 7, 377 (Lüth): Grundrechte als objektive Wertordnung; Verhältnismäßigkeit bei Meinungsfreiheit\n"
            "- BVerfGE 65, 1 (Volkszählung): informationelle Selbstbestimmung; strengste Verhältnismäßigkeitsprüfung\n"
            "- BVerfGE 120, 274 (Online-Durchsuchung): IT-Grundrecht; Verhältnismäßigkeit bei Überwachungsmaßnahmen\n"
            "- BVerfGE 125, 175 (Hartz IV): Grundrecht auf Gewährleistung des Existenzminimums\n\n"
            "Examenstipp: Im öffentlich-rechtlichen Gutachten stets alle vier Stufen der Verhältnismäßigkeit "
            "ausführlich prüfen. Die Angemessenheit erfordert echte Abwägungsarbeit mit Argumenten für beide Seiten."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "BVerfGE 19, 342; BVerfGE 65, 1; BVerfGE 90, 145",
    },
    {
        "name": "BGH – Culpa in contrahendo (c.i.c.) §§ 280, 241 II, 311 II BGB",
        "topic": "Schuldrecht – Allgemeiner Teil",
        "art": "Kommentarauszug",
        "kategorie": "Rechtsprechung",
        "text": (
            "Die culpa in contrahendo (c.i.c.) ist die Haftung aus vorvertraglich verletzten Pflichten. "
            "Seit der Schuldrechtsreform 2002 ist sie in §§ 280 I, 241 II, 311 II BGB kodifiziert, "
            "nachdem sie zuvor von der Rechtsprechung aus dem Grundsatz von Treu und Glauben (§ 242 BGB) entwickelt worden war.\n\n"
            "Tatbestandsvoraussetzungen:\n"
            "1. Vorvertragliches Schuldverhältnis (§ 311 II BGB):\n"
            "   - Nr. 1: Aufnahme von Vertragsverhandlungen\n"
            "   - Nr. 2: Anbahnung eines Vertrags, bei der eine Partei Einwirkung auf Rechte, Rechtsgüter oder Interessen "
            "     der anderen Partei ermöglicht\n"
            "   - Nr. 3: ähnliche geschäftliche Kontakte\n\n"
            "2. Verletzung einer Pflicht aus § 241 II BGB:\n"
            "   Schutzpflichten: Rücksichtnahmepflicht, Aufklärungspflicht, Obhutspflicht.\n"
            "   Keine Leistungspflichten (die entstehen erst mit Vertragsschluss)!\n\n"
            "3. Verschulden (§§ 276-278 BGB), Schaden und Kausalität.\n\n"
            "Wichtige Fallgruppen aus der BGH-Rechtsprechung:\n\n"
            "Verletzung von Aufklärungspflichten:\n"
            "BGH NJW 1989, 763: Verkäufer muss über offenbarungspflichtige Mängel aufklären, "
            "die der Käufer nicht erkennen kann. Schadensersatz: negatives Interesse "
            "(Vertrauen auf das Nichtvorliegen des Mangels).\n\n"
            "Abbruch von Vertragsverhandlungen:\n"
            "BGH NJW 1996, 1884: Schadensersatz wegen treuwidrigen Abbruchs von Verhandlungen "
            "nur bei Vertrauenstatbestand, auf den die andere Partei sich verlassen hat. "
            "Bloßes Verhandeln begründet noch keine Haftung, da kein Kontrahierungszwang besteht.\n\n"
            "Sachwalterhaftung Dritter (§ 311 III BGB):\n"
            "BGH NJW 2001, 2163: Ein Dritter, der bei den Verhandlungen besonderes Vertrauen in Anspruch nimmt "
            "oder ein besonderes wirtschaftliches Interesse am Vertragsschluss hat, kann persönlich haften. "
            "Klassisch: Vertreter ohne Vertretungsmacht, Sachwalter.\n\n"
            "Rechtsfolge:\n"
            "Schadensersatz in Form des negativen Interesses (Vertrauensschaden): "
            "Kläger ist so zu stellen, als hätte er auf den Vertragsschluss nicht vertraut (nicht: Erfüllungsinteresse!). "
            "Ausnahme: Wenn der Vertrag nicht zustande gekommen wäre, besteht kein Anspruch auf das Erfüllungsinteresse.\n\n"
            "Verhältnis zu anderen Ansprüchen:\n"
            "c.i.c. und Anfechtung (§§ 119 ff. BGB): c.i.c. tritt nicht hinter Anfechtungsrecht zurück (BGH NJW 2006, 3139). "
            "c.i.c. und Kaufrecht: Neben Gewährleistungsrechten möglich, wenn eine eigenständige Pflichtverletzung vorliegt.\n\n"
            "Examenstipp: c.i.c. ist examensrelevant v.a. bei Fallkonstellationen ohne Vertrag oder "
            "bei vorvertraglichen Aufklärungspflichtverletzungen. Stets das Verschulden prüfen!"
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 280 I, 241 II, 311 II BGB; BGH NJW 1989, 763; BGH NJW 1996, 1884",
    },
    {
        "name": "BGH – Eigentümer-Besitzer-Verhältnis §§ 985-1007 BGB",
        "topic": "Sachenrecht",
        "art": "Kommentarauszug",
        "kategorie": "Rechtsprechung",
        "text": (
            "Das Eigentümer-Besitzer-Verhältnis (EBV) bildet ein geschlossenes Sondersystem des Sachenrechts, "
            "das die Rechte und Pflichten zwischen dem Eigentümer einer Sache und dem unberechtigten Besitzer regelt.\n\n"
            "Anwendungsbereich des EBV:\n"
            "Das EBV nach §§ 987-1003 BGB kommt nur zur Anwendung, wenn der Besitzer gegenüber dem Eigentümer "
            "kein Recht zum Besitz hat (§ 986 BGB). Bei berechtigtem Besitz (z.B. aus Mietvertrag) gelten die "
            "allgemeinen schuldrechtlichen Regelungen.\n\n"
            "Vindikationsanspruch (§ 985 BGB):\n"
            "Voraussetzungen: Eigentum des Klägers, Besitz des Beklagten, kein Recht zum Besitz des Beklagten (§ 986 BGB).\n"
            "Der Vindikationsanspruch geht auf Herausgabe der Sache. Er unterliegt der regelmäßigen Verjährung nach § 195 BGB (3 Jahre), "
            "bei Grundstücken gelten Besonderheiten (§ 902 BGB).\n\n"
            "Nutzungsherausgabe (§§ 987-993 BGB):\n"
            "- Bösgläubiger Besitzer (§ 990 BGB): haftet für alle gezogenen und schuldhaft nicht gezogenen Nutzungen\n"
            "- Redlicher Besitzer (§ 993 I BGB): haftet nur für tatsächlich gezogene, nach § 101 BGB nicht ihm gebührende Nutzungen\n"
            "- Deliktischer Besitzer (§ 992 BGB): volle Haftung nach Deliktsrecht\n\n"
            "Schadensersatz (§§ 989, 990, 992 BGB):\n"
            "- § 989 BGB: Schadensersatz wegen Verschlechterung/Verlustes der Sache ab Rechtshängigkeit der Klage\n"
            "- § 990 BGB: Vorzeitige Haftung bei Bösgläubigkeit (Kenntnis oder grob fahrlässige Unkenntnis)\n"
            "- § 992 BGB: Deliktische Haftung bei Besitzerwerb durch verbotene Eigenmacht oder Straftat\n\n"
            "Gutgläubiger Erwerb (§§ 929 ff. BGB):\n"
            "BGH NJW 1994, 2549: Gutgläubiger Erwerb setzt voraus:\n"
            "1. Einigung (§ 929 S. 1 BGB)\n"
            "2. Übergabe der Sache\n"
            "3. Berechtigung des Veräußerers oder guter Glaube des Erwerbers (§§ 932 ff. BGB)\n"
            "Guter Glaube: Erwerber darf keine positive Kenntnis und keine grob fahrlässige Unkenntnis "
            "vom fehlenden Eigentum des Veräußerers haben (§ 932 II BGB).\n"
            "Ausschluss: gestohlene/abhandengekommene Sachen (§ 935 BGB).\n\n"
            "Verwendungsersatz (§§ 994-1003 BGB):\n"
            "Notwendige Verwendungen sind vom Eigentümer stets zu ersetzen (§ 994 I BGB). "
            "Nützliche Verwendungen: nur der bösgläubige Besitzer hat keinen Anspruch (§ 996 BGB). "
            "Zurückbehaltungsrecht des Besitzers bis zur Erstattung (§ 1000 BGB).\n\n"
            "Sperrwirkung des EBV:\n"
            "Das EBV sperrt konkurrierende Ansprüche aus ungerechtfertigter Bereicherung (§§ 812 ff. BGB) "
            "und Deliktsrecht (§§ 823 ff. BGB), soweit sie auf denselben Tatbestand gestützt werden "
            "(BGH NJW 1992, 2570 – str. bzgl. Deliktsrecht).\n\n"
            "Examenstipp: Im Gutachten prüfen: (1) EBV eröffnet? (2) gut- oder bösgläubiger Besitzer? "
            "(3) Sperrwirkung beachten!"
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 985-1007 BGB; BGH NJW 1994, 2549; BGH NJW 1992, 2570",
    },
    {
        "name": "BVerwG – Ermessensfehlerlehre",
        "topic": "Öffentliches Recht – Verwaltungsrecht",
        "art": "Kommentarauszug",
        "kategorie": "Rechtsprechung",
        "text": (
            "Das Ermessen der Verwaltung ist gerichtlich nur eingeschränkt überprüfbar (§ 114 S. 1 VwGO). "
            "Gerichte prüfen nur, ob die Behörde die gesetzlichen Grenzen des Ermessens eingehalten und das Ermessen "
            "entsprechend dem Zweck der Ermächtigung ausgeübt hat (§ 40 VwVfG).\n\n"
            "Arten von Ermessensfehlern (nach BVerwG-Rechtsprechung):\n\n"
            "1. Ermessensausfall (Ermessensnichtgebrauch):\n"
            "Die Behörde erkennt nicht, dass ihr Ermessen zusteht, und handelt, als wäre sie gebunden. "
            "Beispiel: BVerwGE 72, 1: Behörde lehnt Antrag ab mit der Begründung, das Gesetz lasse keine andere "
            "Entscheidung zu, obwohl tatsächlich Ermessen bestand. "
            "Folge: Aufhebung des VA und Verpflichtung zur Neuverbescheidung (kein Spruchreifemachen!).\n\n"
            "2. Ermessensüberschreitung:\n"
            "Die Behörde wählt eine Maßnahme, die außerhalb des durch das Gesetz eingeräumten Rahmens liegt, "
            "oder berücksichtigt sachfremde Erwägungen. "
            "Beispiel: BVerwGE 38, 274: Polizeiliche Maßnahme gegen einen unbeteiligten Dritten trotz Inanspruchnahme "
            "nur gegen den Störer. "
            "Abgrenzung zur Ermessensunterschreitung: Behörde schränkt das ihr zustehende Ermessen durch eigene "
            "Verwaltungsvorschriften ein, ohne im Einzelfall zu prüfen (Ermessensunterschreitung).\n\n"
            "3. Ermessensmissbrauch (Ermessensfehlgebrauch):\n"
            "Die Behörde übt das Ermessen nicht dem Zweck der Ermächtigungsgrundlage entsprechend aus. "
            "Beispiel: BVerwGE 80, 178: Ablehnung einer Genehmigung aus Gründen, die mit dem Schutzzweck der Norm "
            "nichts zu tun haben (z.B. parteipolitische Erwägungen). "
            "Häufig auch: Ermessensdefizit – die Behörde hat relevante Gesichtspunkte nicht berücksichtigt.\n\n"
            "4. Ermessensreduktion auf Null:\n"
            "In Ausnahmefällen schrumpft das Ermessen auf null, sodass nur eine Entscheidung rechtmäßig ist. "
            "BVerwGE 94, 307: Bei Vorliegen besonderer Umstände (z.B. erhebliche Grundrechtsgefährdung) "
            "ist die Behörde verpflichtet, eine bestimmte Maßnahme zu ergreifen. "
            "Folge: Gericht kann Verpflichtungsurteil auf Erlass des begehrten VA aussprechen.\n\n"
            "Gerichtliche Kontrolle (§ 114 VwGO):\n"
            "Grundsatz: Gerichte dürfen das Ermessen nicht selbst ausüben (Gewaltenteilung!). "
            "Sie können nur die Ermessensfehlerhaftigkeit feststellen und zur Neuverbescheidung verurteilen. "
            "Ausnahme: Ermessensreduktion auf Null → Verpflichtungsurteil möglich.\n\n"
            "Verhältnis zu Beurteilungsspielraum:\n"
            "Ermessen betrifft die Rechtsfolgenseite ('kann', 'darf', 'soll'). "
            "Beurteilungsspielraum betrifft die Tatbestandsseite (unbestimmte Rechtsbegriffe). "
            "BVerwGE 39, 197: Prüfungsrecht bei unbestimmten Rechtsbegriffen nur eingeschränkt nachprüfbar.\n\n"
            "Examenstipp: Im Verwaltungsrecht bei Ermessensvorschriften immer alle Ermessensfehlerarten prüfen. "
            "Auf 'Soll'-Vorschriften achten: diese begründen in der Regel gebundenes Ermessen mit "
            "Ausnahmevorbehalt für atypische Fälle."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§ 114 VwGO; § 40 VwVfG; BVerwGE 72, 1; BVerwGE 38, 274; BVerwGE 94, 307",
    },

    # ─────────────────────────────────────────────────────────────
    # LITERATUR – Doktrin / Schema
    # ─────────────────────────────────────────────────────────────
    {
        "name": "Gutachtenstil – Aufbau und Methodik",
        "topic": "Juristische Methodik",
        "art": "Lehrbuchauszug",
        "kategorie": "Literatur",
        "text": (
            "Der Gutachtenstil ist die Kerntechnik juristischer Falllösung in Studium und Examen. "
            "Er unterscheidet sich grundlegend vom Urteilsstil (Ergebnis → Begründung): "
            "Im Gutachten wird das Ergebnis erst am Ende einer logisch aufgebauten Prüfung genannt.\n\n"
            "Die vier Schritte des Gutachtenstils:\n\n"
            "1. Obersatz (These):\n"
            "Formulierung dessen, was geprüft werden soll. Stets: 'X könnte Y haben / sein / ... wenn ...' "
            "Beispiel: 'K könnte gegen V einen Anspruch auf Kaufpreisrückzahlung aus § 346 I BGB haben, "
            "wenn ein wirksamer Rücktritt vorliegt.'\n\n"
            "2. Definition (Abstrakte Begriffsbestimmung):\n"
            "Das entscheidende Tatbestandsmerkmal wird abstrakt definiert, ohne den konkreten Fall zu nennen. "
            "Beispiel: 'Verzug liegt vor, wenn der Schuldner trotz Fälligkeit und Mahnung nicht leistet (§ 286 I BGB).'\n\n"
            "3. Subsumtion (Anwendung auf den Sachverhalt):\n"
            "Die abstrakten Definitionsmerkmale werden auf den konkreten Sachverhalt angewendet. "
            "Stets mit konkreten Sachverhaltsangaben arbeiten! "
            "Beispiel: 'V hat die Kaufsache am 1. März trotz Fälligkeit am 15. Februar nicht übergeben. "
            "K mahnte am 20. Februar schriftlich. Damit waren alle Voraussetzungen des Verzuges am 1. März erfüllt.'\n\n"
            "4. Ergebnis:\n"
            "Kurze, eindeutige Feststellung. Stets im Konjunktiv, bis das Endergebnis feststeht. "
            "Beispiel: 'V befand sich damit am 1. März in Verzug.' "
            "Am Ende: definitives Ergebnis ohne Konjunktiv.\n\n"
            "Häufige Fehler:\n"
            "- Fehlendes Prüfungsprogramm: Merkmale werden nicht alle geprüft\n"
            "- Vorweggenommenes Ergebnis im Obersatz (Urteilsstil statt Gutachtenstil)\n"
            "- Subsumtion ohne Sachverhaltsangaben ('da alle Voraussetzungen vorliegen...')\n"
            "- Fehlende oder unpräzise Definition\n"
            "- Unnötige Prüfung unstreitiger Merkmale (Zeitverschwendung!)\n\n"
            "Wechsel von Gutachten- zu Urteilsstil:\n"
            "Bei offensichtlich unproblematischen Merkmalen ist der Urteilsstil zulässig und effizient. "
            "Beispiel: 'V und K sind geschäftsfähig.' "
            "Gut ausgebildete Juristen wissen, wann ein Merkmal vertieft werden muss und wann nicht.\n\n"
            "Aufbau der Anspruchsgrundlagensystematik:\n"
            "In zivilrechtlichen Klausuren stets nach dem sog. 'Anspruchsaufbau':\n"
            "1. Anspruch entstanden? (Tatbestandsvoraussetzungen)\n"
            "2. Anspruch erloschen? (Einwendungen: Erfüllung, Unmöglichkeit, Rücktritt etc.)\n"
            "3. Anspruch durchsetzbar? (Einreden: Verjährung, § 273 BGB, § 320 BGB)\n\n"
            "Reihenfolge der Anspruchsgrundlagen:\n"
            "Im Zivilrecht immer zunächst vertragliche Ansprüche, dann quasi-vertragliche (c.i.c., GoA), "
            "dann dingliche Ansprüche, zuletzt deliktische Ansprüche prüfen. "
            "Dies entspricht der Systematik und der Subsidiarität bestimmter Anspruchsgrundlagen.\n\n"
            "Examenstipp: Im Examen zählt nicht nur das richtige Ergebnis, sondern die methodisch korrekte "
            "Herleitung. Ein falsches Ergebnis mit sauberem Gutachtenstil kann mehr Punkte bringen als "
            "ein richtiges Ergebnis ohne methodischen Aufbau."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "Lüke, Zivilprozessrecht; Medicus/Petersen, Bürgerliches Recht",
    },
    {
        "name": "Deliktsrecht – §§ 823 ff. BGB Schema",
        "topic": "Schuldrecht – Besonderer Teil",
        "art": "Lehrbuchauszug",
        "kategorie": "Literatur",
        "text": (
            "Das Deliktsrecht (§§ 823-853 BGB) regelt die außervertragliche Haftung für Schäden, "
            "die durch unerlaubte Handlungen verursacht werden. Die wichtigsten Normen sind §§ 823 I, 823 II und 826 BGB.\n\n"
            "§ 823 I BGB – Grundtatbestand:\n"
            "Wer vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum "
            "oder ein sonstiges absolutes Recht eines anderen widerrechtlich verletzt, haftet auf Schadensersatz.\n\n"
            "Prüfungsschema:\n"
            "1. Rechtsgutsverletzung: eines der enumerierten absoluten Rechte verletzt?\n"
            "   - Körper/Gesundheit: jede physische Substanzbeeinträchtigung\n"
            "   - Eigentum: Substanzverletzung oder -vernichtung (nicht: reiner Vermögensschaden!)\n"
            "   - Sonstige absolute Rechte: allg. Persönlichkeitsrecht (APR), Recht am eingerichteten und ausgeübten Gewerbebetrieb\n"
            "2. Handlung oder Unterlassen (bei Unterlassen: Verkehrssicherungspflicht oder Garantenstellung)\n"
            "3. Haftungsbegründende Kausalität (Äquivalenz-, Adäquanztheorie, Schutzzwecklehre)\n"
            "4. Widerrechtlichkeit (Erfolgsunrecht, grds. indiziert durch Rechtsgutsverletzung; Rechtfertigungsgründe: Notwehr § 227, Notstand § 228, 904)\n"
            "5. Verschulden: Vorsatz oder Fahrlässigkeit (§ 276 BGB, objektiver Maßstab)\n"
            "6. Haftungsausfüllende Kausalität und Schaden\n\n"
            "§ 823 II BGB – Schutzgesetzverletzung:\n"
            "Wer gegen ein den Schutz eines anderen bezweckendes Gesetz verstößt, haftet ebenfalls.\n"
            "Prüfungsschema:\n"
            "1. Schutzgesetz: Welche Norm dient dem Individualschutz? (StVG, StGB-Normen als Schutzgesetze)\n"
            "2. Verletzung des Schutzgesetzes (Normverstoß)\n"
            "3. Der Kläger gehört zum Schutzbereich des Gesetzes\n"
            "4. Verschulden hinsichtlich des Normverstoßes\n"
            "5. Kausalität und Schaden\n\n"
            "§ 826 BGB – Sittenwidrige vorsätzliche Schädigung:\n"
            "Wer einem anderen in einer gegen die guten Sitten verstoßenden Weise vorsätzlich Schaden zufügt, "
            "haftet auf Schadensersatz. Besonderheit: erfasst auch reine Vermögensschäden!\n"
            "Voraussetzungen: Sittenwidrige Handlung, Vorsatz (auch dolus eventualis bzgl. Schaden), Schaden.\n"
            "BGH NJW 2020, 1962 (VW-Dieselskandal): Strategische Täuschung über Produkteigenschaften zur Profitmaximierung ist sittenwidrig.\n\n"
            "Mitverschulden (§ 254 BGB):\n"
            "Hat der Geschädigte durch eigenes Verschulden zur Schadensentstehung beigetragen, "
            "mindert sich der Ersatzanspruch nach dem Maß des beiderseitigen Verschuldens.\n\n"
            "Haftung für Verrichtungsgehilfen (§ 831 BGB):\n"
            "Verrichtungsgehilfen-Haftung mit Exkulpationsmöglichkeit (sog. dezentralisierte Verschuldenshaftung). "
            "Abgrenzung zu § 278 BGB (kein Exkulpationsbeweis).\n\n"
            "Produzentenhaftung (BGHZ 51, 91 – Hühnerpest):\n"
            "BGH entwickelte Beweislastumkehr bei Produktfehlern. Hersteller muss beweisen, dass kein Fabrikations-, "
            "Konstruktions- oder Instruktionsfehler vorlag. Neben dem ProdHaftG (Gefährdungshaftung) anwendbar.\n\n"
            "Examenstipp: Im Deliktsrecht immer nach dem Schema vorgehen: § 823 I → § 823 II → § 826 → "
            "spezialgesetzliche Gefährdungshaftung (z.B. § 7 StVG, § 1 ProdHaftG)."
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 823-853 BGB; BGH NJW 2020, 1962; MüKoBGB § 823",
    },
    {
        "name": "Strafrecht AT – Verbrechensaufbau",
        "topic": "Strafrecht – Allgemeiner Teil",
        "art": "Lehrbuchauszug",
        "kategorie": "Literatur",
        "text": (
            "Der Verbrechensaufbau ist das zentrale Prüfungsschema im Strafrecht. "
            "Die Strafbarkeit einer Person setzt das Vorliegen aller drei Elemente voraus: "
            "Tatbestand, Rechtswidrigkeit und Schuld.\n\n"
            "I. Tatbestand:\n\n"
            "A. Objektiver Tatbestand:\n"
            "1. Tathandlung (actus reus): Was muss der Täter getan haben?\n"
            "2. Taterfolg (bei Erfolgsdelikten): Welcher Erfolg muss eingetreten sein?\n"
            "3. Kausalität: conditio-sine-qua-non-Formel (Äquivalenztheorie); "
            "   bei alternativer Kausalität und Unterlassen Besonderheiten.\n"
            "4. Objektive Zurechnung (h.L.): Schaffung eines rechtlich missbilligten Risikos, "
            "   das sich im Erfolg realisiert hat. "
            "   Ausschlüsse: Risikoverringerung, sozialadäquates Verhalten, eigenverantwortliche Selbstgefährdung, "
            "   atypischer Kausalverlauf.\n\n"
            "B. Subjektiver Tatbestand:\n"
            "1. Vorsatz (§ 15 StGB): dolus directus I°, II° oder eventualis\n"
            "2. Besondere subjektive Merkmale: Absicht (z.B. Zueignungsabsicht § 242 StGB), "
            "   überschießende Innentendenz (z.B. § 263 StGB: Bereicherungsabsicht)\n\n"
            "II. Rechtswidrigkeit:\n"
            "Die Tatbestandserfüllung indiziert die Rechtswidrigkeit. "
            "Prüfung erfolgt nur, wenn ein Rechtfertigungsgrund in Betracht kommt:\n\n"
            "1. Notwehr (§ 32 StGB):\n"
            "   - Notwehrlage: Angriff eines Menschen, gegenwärtig, rechtswidrig\n"
            "   - Notwehrhandlung: Verteidigung, erforderlich (mildestes geeignetes Mittel), geboten\n"
            "   Einschränkungen bei sozialadäquatem Angriff, Angriff von Schuldlosen, Absichtsprovokation.\n\n"
            "2. Rechtfertigender Notstand (§ 34 StGB):\n"
            "   - Notstandslage: Gefahr für Rechtsgut\n"
            "   - Notstandshandlung: nicht anders abwendbar\n"
            "   - Interessenabwägung: wesentliches Überwiegen des geschützten Interesses\n\n"
            "3. Einwilligung: wirksame Einwilligung des Rechtsgutsträgers (Einwilligungsfähigkeit, keine Täuschung)\n"
            "4. Weitere: §§ 127 StPO, 229, 228 BGB, § 193 StGB (Wahrnehmung berechtigter Interessen)\n\n"
            "III. Schuld:\n"
            "Schuld setzt voraus, dass dem Täter persönlich ein Vorwurf gemacht werden kann.\n\n"
            "1. Schuldfähigkeit (§§ 19-21 StGB):\n"
            "   - § 19 StGB: Kinder unter 14 Jahren schuldunfähig\n"
            "   - § 20 StGB: Aufhebung der Einsichts- oder Steuerungsfähigkeit durch psych. Störung\n"
            "   - § 21 StGB: Erhebliche Verminderung → fakultative Strafmilderung\n\n"
            "2. Unrechtsbewusstsein / Verbotsirrtum (§ 17 StGB):\n"
            "   Fehlte dem Täter das Unrechtsbewusstsein und war der Irrtum unvermeidbar → kein Vorwurf. "
            "   Vermeidbarer Irrtum: Strafmilderung möglich.\n\n"
            "3. Entschuldigungsgründe: Entschuldigender Notstand (§ 35 StGB), Überschreitung der Notwehr (§ 33 StGB)\n\n"
            "Besonderheiten bei Versuch:\n"
            "§§ 22, 23 StGB: unmittelbares Ansetzen zum Tatbestand, Rücktritt möglich (§ 24 StGB).\n\n"
            "Beteiligungsformen:\n"
            "- Mittäterschaft (§ 25 II StGB): gemeinschaftlicher Tatentschluss, arbeitsteilige Ausführung\n"
            "- Anstiftung (§ 26 StGB): Hervorrufen des Tatentschlusses\n"
            "- Beihilfe (§ 27 StGB): Hilfeleistung zur fremden Tat\n\n"
            "Examenstipp: Schema immer vollständig durchgehen, auch wenn Merkmale unproblematisch sind. "
            "Rechtfertigungs- und Entschuldigungsgründe nie vermischen!"
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 1-79b StGB; Roxin, Strafrecht AT I; Wessels/Beulke/Satzger, Strafrecht AT",
    },
    {
        "name": "Öffentliches Recht – Verwaltungsakt §§ 35 ff. VwVfG",
        "topic": "Öffentliches Recht – Verwaltungsrecht",
        "art": "Lehrbuchauszug",
        "kategorie": "Literatur",
        "text": (
            "Der Verwaltungsakt (VA) ist die zentrale Handlungsform der Verwaltung und Anknüpfungspunkt "
            "für den verwaltungsgerichtlichen Rechtsschutz.\n\n"
            "Definition (§ 35 S. 1 VwVfG):\n"
            "Verwaltungsakt ist jede Verfügung, Entscheidung oder andere hoheitliche Maßnahme, "
            "die eine Behörde zur Regelung eines Einzelfalls auf dem Gebiet des öffentlichen Rechts trifft "
            "und die auf unmittelbare Rechtswirkung nach außen gerichtet ist.\n\n"
            "Tatbestandsmerkmale im Überblick:\n"
            "1. Maßnahme einer Behörde (§ 1 IV VwVfG: Behörde = staatliche Organisationseinheit zur Wahrnehmung öffentlicher Aufgaben)\n"
            "2. Hoheitliche Maßnahme: Staat handelt übergeordnet mit einseitig-bindender Wirkung\n"
            "3. Auf dem Gebiet des öffentlichen Rechts (Abgrenzung durch modifizierte Subjektstheorie)\n"
            "4. Zur Regelung: verbindliche Festsetzung von Rechtsfolgen (nicht: bloße Informationen)\n"
            "5. Eines Einzelfalls: konkret-individuelle Regelung (Abgrenzung zur Allgemeinverfügung § 35 S. 2 VwVfG und zur Rechtsnorm)\n"
            "6. Unmittelbare Außenwirkung: Wirkung auf Außenstehende, nicht nur behördenintern\n\n"
            "Allgemeinverfügung (§ 35 S. 2 VwVfG):\n"
            "Eine an einen nach allgemeinen Merkmalen bestimmten oder bestimmbaren Personenkreis gerichtete Regelung "
            "oder die öffentlich-rechtliche Eigenschaft einer Sache (z.B. Widmung einer Straße). "
            "Bsp.: Verkehrszeichen, Versammlungsverbote.\n\n"
            "Formelle Rechtmäßigkeit:\n"
            "- Zuständigkeit der Behörde (sachlich, örtlich, instanziell)\n"
            "- Verfahren: ggf. Anhörung des Betroffenen (§ 28 VwVfG)\n"
            "- Form: grds. keine Formvorschriften (§ 37 II VwVfG), schriftliche VA mit Begründungspflicht (§ 39 VwVfG) "
            "  und Rechtsbehelfsbelehrung (§ 37 VI VwVfG)\n\n"
            "Materielle Rechtmäßigkeit:\n"
            "- Rechtsgrundlage vorhanden (Gesetzesvorbehalt!)\n"
            "- Tatbestandsvoraussetzungen der Rechtsgrundlage erfüllt\n"
            "- Rechtsfolge rechtmäßig: bei Ermessen Ermessensfehlerfreiheit; bei gebundenen Entscheidungen Einhaltung\n\n"
            "Bestandskraft:\n"
            "Mit Ablauf der Widerspruchs-/Klagefrist wird der VA formell bestandskräftig. "
            "Der Adressat kann ihn nicht mehr mit ordentlichen Rechtsbehelfen anfechten. "
            "Materielle Bestandskraft: bindende Wirkung für Behörde und Betroffenen. "
            "Rücknahme rechtswidriger VA: § 48 VwVfG (Vertrauensschutz beachten!). "
            "Widerruf rechtmäßiger VA: § 49 VwVfG (engere Voraussetzungen).\n\n"
            "Nichtigkeit (§ 44 VwVfG):\n"
            "Besonders schwerwiegende und offensichtliche Mängel führen zur Nichtigkeit (absolute Nichtigkeit). "
            "§ 44 II VwVfG zählt Regelbeispiele auf. Nichtiger VA ist von Anfang an unwirksam, jederzeit angreifbar.\n\n"
            "Examenstipp: Bei VA-Klausuren immer Wirksamkeit (§§ 43-44 VwVfG), formelle und materielle "
            "Rechtmäßigkeit sowie Bestandskraftfragen prüfen. Abgrenzung VA / Allgemeinverfügung / Rechtsnorm!"
        ),
        "chars": 0,
        "pages": 1,
        "uploader": "system",
        "source_type": "shared",
        "quelle": "§§ 35-53 VwVfG; BVerwGE 12, 87",
    },
]


if __name__ == "__main__":
    import json

    for m in SEED_MATERIALS:
        m["chars"] = len(m["text"])  # chars automatisch berechnen

    output = json.dumps(SEED_MATERIALS, ensure_ascii=False, indent=2)
    with open("seed_materials_output.json", "w", encoding="utf-8") as f:
        f.write(output)
    print(f"✅ {len(SEED_MATERIALS)} Materialien → seed_materials_output.json")
    print("→ Inhalt als users/shared/materials_index.json ins Daten-Repo hochladen")

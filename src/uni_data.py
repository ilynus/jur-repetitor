"""Datenbank aller deutschen Jurafakultäten mit Schwerpunktbereichen und Bundesländern."""
from __future__ import annotations

UNI_DATA: dict[str, dict] = {
    "Universität Augsburg": {
        "bundesland": "Bayern",
        "schwerpunkte": [
            "Unternehmens- und Kapitalmarktrecht",
            "Steuerrecht",
            "Recht der Informationsgesellschaft",
            "Internationales Recht und Europarecht",
            "Arbeits- und Sozialrecht",
            "Strafrecht und Kriminologie",
        ],
        "examensamt": "Landesjustizprüfungsamt Bayern",
        "besonderheiten": "Starke Wirtschaftsrechtsprofessur, Informatik-Jura-Kombination",
    },
    "Universität Bayreuth": {
        "bundesland": "Bayern",
        "schwerpunkte": [
            "Internationales Wirtschaftsrecht",
            "Sport und Recht",
            "Umwelt- und Planungsrecht",
            "Arbeits- und Sozialrecht",
            "Unternehmensrecht und Steuerrecht",
            "Geistiges Eigentum und Wettbewerb",
        ],
        "examensamt": "Landesjustizprüfungsamt Bayern",
        "besonderheiten": "Einziger Studiengang Internationales Wirtschaftsrecht (LL.B./LL.M.), starkes Sportrecht",
    },
    "Universität Bielefeld": {
        "bundesland": "Nordrhein-Westfalen",
        "schwerpunkte": [
            "Zivilrechtspflege, Anwaltsberatung und Notariat",
            "Kriminalwissenschaften",
            "Arbeit, Soziales und Unternehmen",
            "Internationales Recht und Europarecht",
            "Öffentliches Wirtschaftsrecht",
            "Umwelt und Verbraucher",
        ],
        "examensamt": "Landesjustizprüfungsamt NRW",
        "besonderheiten": "Kritische Rechtswissenschaft, Law & Society",
    },
    "Universität Bochum (Ruhr)": {
        "bundesland": "Nordrhein-Westfalen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmen, Kapitalmarkt und Steuern",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und Regulierung",
            "Arbeit und Soziales",
            "Internationales Recht",
        ],
        "examensamt": "Landesjustizprüfungsamt NRW",
        "besonderheiten": "Starkes Bergrecht, Energierecht und Bergbaurecht",
    },
    "Universität Bonn": {
        "bundesland": "Nordrhein-Westfalen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmen und Finanzen",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und öffentliche Unternehmen",
            "Internationales Recht und Europarecht",
            "Arbeit und Soziales",
        ],
        "examensamt": "Landesjustizprüfungsamt NRW",
        "besonderheiten": "Traditionsreiche Fakultät, Institut für Öffentliches Recht renommiert",
    },
    "Universität Bremen": {
        "bundesland": "Bremen",
        "schwerpunkte": [
            "Rechtswissenschaft und Gesellschaft",
            "Arbeit, Wirtschaft und Soziales",
            "Kriminalwissenschaften",
            "Internationales Recht und Europarecht",
            "Rechtsgestaltung und Rechtspflege",
            "Umwelt- und Planungsrecht",
        ],
        "examensamt": "Prüfungsamt beim Senator für Justiz und Verfassung Bremen",
        "besonderheiten": "Bremer Modell, Praxisorientierung, sozialwissenschaftliche Juristenausbildung",
    },
    "Universität Düsseldorf (HHU)": {
        "bundesland": "Nordrhein-Westfalen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmen, Kapitalmarkt und Steuern",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und Europa",
            "Arbeit, Soziales und Gesundheit",
            "Internationales und Europäisches Recht",
        ],
        "examensamt": "Landesjustizprüfungsamt NRW",
        "besonderheiten": "Institut für Kartell- und Wirtschaftsrecht, Medizinrecht",
    },
    "Universität Erlangen-Nürnberg (FAU)": {
        "bundesland": "Bayern",
        "schwerpunkte": [
            "Privatrecht und Wirtschaft",
            "Strafrecht und Kriminologie",
            "Öffentliches Recht und Staatsrecht",
            "Internationales Recht",
            "Arbeits- und Sozialrecht",
            "Geistiges Eigentum und Wettbewerb",
        ],
        "examensamt": "Landesjustizprüfungsamt Bayern",
        "besonderheiten": "Starkes Wirtschaftsstrafrecht, Patentrecht (Nähe zu Industrie)",
    },
    "Universität Frankfurt (Goethe)": {
        "bundesland": "Hessen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmens- und Kapitalmarktrecht",
            "Kriminalwissenschaften",
            "Öffentliches Wirtschaftsrecht",
            "Arbeit, Soziales und Gesundheit",
            "Internationales Recht und Europarecht",
        ],
        "examensamt": "Justizprüfungsamt beim OLG Frankfurt",
        "besonderheiten": "Finanzrecht und Bankrecht (Nähe zu EZB/Finanzplatz Frankfurt), starkes Steuerrecht",
    },
    "Universität Freiburg": {
        "bundesland": "Baden-Württemberg",
        "schwerpunkte": [
            "Grundlagen des Rechts",
            "Wirtschaft und Unternehmen",
            "Kriminalwissenschaften",
            "Internationales Recht und Europarecht",
            "Arbeits- und Sozialrecht",
            "Staat, Verfassung und Verwaltung",
        ],
        "examensamt": "Landesjustizprüfungsamt Baden-Württemberg",
        "besonderheiten": "Starke Rechtsphilosophie und Rechtsgeschichte, Max-Planck-Institut für ausländisches und internationales Privatrecht",
    },
    "Universität Gießen (JLU)": {
        "bundesland": "Hessen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Wirtschaft und Unternehmen",
            "Kriminalwissenschaften",
            "Staat, Verfassung und Verwaltung",
            "Arbeit und Soziales",
            "Internationales Recht",
        ],
        "examensamt": "Justizprüfungsamt beim OLG Frankfurt",
        "besonderheiten": "Agrarrecht, Lebensmittelrecht, Umweltrecht",
    },
    "Universität Halle-Wittenberg (MLU)": {
        "bundesland": "Sachsen-Anhalt",
        "schwerpunkte": [
            "Zivilrechtliche Rechtspraxis",
            "Unternehmens- und Wirtschaftsrecht",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und öffentliche Unternehmen",
            "Arbeit, Soziales und Gesundheit",
            "Internationales Recht",
        ],
        "examensamt": "Landesjustizprüfungsamt Sachsen-Anhalt",
        "besonderheiten": "Ostdeutsche Rechtsentwicklung, Transformationsrecht",
    },
    "Universität Hamburg": {
        "bundesland": "Hamburg",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmens- und Kapitalmarktrecht",
            "Kriminalwissenschaften",
            "Öffentliches Recht und Verwaltung",
            "Arbeit und Soziales",
            "Internationales Recht und Europarecht",
        ],
        "examensamt": "Prüfungsamt der Behörde für Justiz Hamburg",
        "besonderheiten": "Seehandelsrecht, Transportrecht, Internationales Handelsrecht (Hafenstadt)",
    },
    "Universität Heidelberg": {
        "bundesland": "Baden-Württemberg",
        "schwerpunkte": [
            "Grundlagen des Rechts",
            "Unternehmens- und Wirtschaftsrecht",
            "Kriminalwissenschaften",
            "Öffentliches Recht und Regulierung",
            "Arbeit und Soziales",
            "Internationales und Europäisches Recht",
        ],
        "examensamt": "Landesjustizprüfungsamt Baden-Württemberg",
        "besonderheiten": "Älteste deutsche Universität, traditionsreiche Strafrechtswissenschaft, Max-Planck-Institut für ausländisches öffentliches Recht",
    },
    "Humboldt-Universität zu Berlin (HU)": {
        "bundesland": "Berlin",
        "schwerpunkte": [
            "Grundlagen des Rechts",
            "Unternehmens- und Wirtschaftsrecht",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und Europa",
            "Arbeit und Soziales",
            "Internationales Recht",
        ],
        "examensamt": "Gemeinsames Juristisches Prüfungsamt Berlin-Brandenburg",
        "besonderheiten": "Starke Rechtstheorie, Rechtssoziologe, Sitz vieler Bundesbehörden",
    },
    "Universität Jena (FSU)": {
        "bundesland": "Thüringen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Wirtschaft, Arbeit und Soziales",
            "Kriminalwissenschaften",
            "Staat und Verfassung",
            "Internationales und Europäisches Recht",
            "Umwelt- und Technikrecht",
        ],
        "examensamt": "Thüringer Landesjustizprüfungsamt",
        "besonderheiten": "Medizinrecht, Technikrecht",
    },
    "Universität Kiel (CAU)": {
        "bundesland": "Schleswig-Holstein",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Wirtschafts- und Steuerrecht",
            "Kriminalwissenschaften",
            "Öffentliches Recht und Verwaltung",
            "Arbeit, Soziales und Gesundheit",
            "Internationales Recht und Seerecht",
        ],
        "examensamt": "Landesjustizprüfungsamt Schleswig-Holstein",
        "besonderheiten": "Seerecht, Völkerrecht (Küstenstandort), Institut für Weltwirtschaft",
    },
    "Universität Köln": {
        "bundesland": "Nordrhein-Westfalen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmens- und Kapitalmarktrecht",
            "Kriminalwissenschaften",
            "Staat, Wirtschaft und Gesellschaft",
            "Arbeit, Soziales und Gesundheit",
            "Internationales Recht und Europarecht",
        ],
        "examensamt": "Landesjustizprüfungsamt NRW",
        "besonderheiten": "Größte Jurafakultät Deutschlands, Institut für Versicherungsrecht, starkes Handels- und Gesellschaftsrecht",
    },
    "Universität Konstanz": {
        "bundesland": "Baden-Württemberg",
        "schwerpunkte": [
            "Privatrecht und Wirtschaft",
            "Öffentliches Recht und Regulierung",
            "Kriminalwissenschaften",
            "Internationales und Europäisches Recht",
            "Arbeit und Soziales",
            "Grundlagen des Rechts",
        ],
        "examensamt": "Landesjustizprüfungsamt Baden-Württemberg",
        "besonderheiten": "Kleine, forschungsstarke Fakultät, starkes Europarecht",
    },
    "Universität Leipzig": {
        "bundesland": "Sachsen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Unternehmens- und Kapitalmarktrecht",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und öffentliche Unternehmen",
            "Arbeit und Soziales",
            "Internationales Recht und Europarecht",
        ],
        "examensamt": "Landesjustizprüfungsamt Sachsen",
        "besonderheiten": "Älteste Jurafakultät Deutschlands, starkes Medienrecht (Leipzig als Medienstadt)",
    },
    "Universität Mainz (JGU)": {
        "bundesland": "Rheinland-Pfalz",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Wirtschaft und Finanzen",
            "Kriminalwissenschaften",
            "Öffentliches Recht und Verwaltung",
            "Arbeit und Soziales",
            "Internationales Recht und Europarecht",
        ],
        "examensamt": "Landesjustizprüfungsamt Rheinland-Pfalz",
        "besonderheiten": "Medienrecht (Mainz als Medienstandort), Stiftungsrecht",
    },
    "Universität Mannheim": {
        "bundesland": "Baden-Württemberg",
        "schwerpunkte": [
            "Unternehmens- und Kapitalmarktrecht",
            "Steuerrecht",
            "Internationales und Europäisches Wirtschaftsrecht",
            "Arbeit und Soziales",
            "Wettbewerbs- und Immaterialgüterrecht",
            "Öffentliches Wirtschaftsrecht",
        ],
        "examensamt": "Landesjustizprüfungsamt Baden-Württemberg",
        "besonderheiten": "Ausgeprägter Wirtschaftsrechtsschwerpunkt, Business Law School, enge Verzahnung mit BWL-Fakultät",
    },
    "Universität Marburg (Philipps)": {
        "bundesland": "Hessen",
        "schwerpunkte": [
            "Zivilrechtspflege und Anwaltsberatung",
            "Wirtschaft und Gesellschaft",
            "Kriminalwissenschaften",
            "Staat, Verfassung und Verwaltung",
            "Arbeit und Soziales",
            "Internationales Recht",
        ],
        "examensamt": "Justizprüfungsamt beim OLG Frankfurt",
        "besonderheiten": "Stark im Öffentlichen Recht, Sozialrecht",
    },
    "Universität München (LMU)": {
        "bundesland": "Bayern",
        "schwerpunkte": [
            "Grundlagen des Rechts",
            "Internationales Recht",
            "Wirtschafts- und Steuerrecht",
            "Geistiges Eigentum und Wettbewerb",
            "Arbeits- und Sozialrecht",
            "Strafrecht und Kriminologie",
        ],
        "examensamt": "Landesjustizprüfungsamt Bayern",
        "besonderheiten": "Schwerpunkt Europarecht, starke Wirtschaftsrechtsprofessur, Max-Planck-Institute in der Nähe",
    },
    "Universität Münster (WWU)": {
        "bundesland": "Nordrhein-Westfalen",
        "schwerpunkte": [
            "Zivilrechtspflege, Anwaltsberatung und Notariat",
            "Unternehmen und Finanzen",
            "Kriminalwissenschaften",
            "Öffentliches Recht, Finanzrecht und Steuern",
            "Arbeit und Soziales",
            "Internationales Recht und Europarecht",
        ],
        "examensamt": "Landesjustizprüfungsamt NRW",
        "besonderheiten": "Zweitgrößte Jurafakultät Deutschlands, starkes Kirchenrecht, Europarecht-Institut",
    },
    "Universität Passau": {
        "bundesland": "Bayern",
        "schwerpunkte": [
            "Internationales Wirtschaftsrecht",
            "Digitales Recht und IT-Recht",
            "Europarecht",
            "Unternehmens- und Kapitalmarktrecht",
            "Kriminalwissenschaften",
            "Recht der öffentlichen Verwaltung",
        ],
        "examensamt": "Landesjustizprüfungsamt Bayern",
        "besonderheiten": "Schwerpunkt IT-Recht und Digitalrecht, Internationales Wirtschaftsrecht, JurPC",
    },
    "Universität Regensburg": {
        "bundesland": "Bayern",
        "schwerpunkte": [
            "Privatrecht und Wirtschaft",
            "Strafrecht und Kriminologie",
            "Staat, Verwaltung und öffentliche Wirtschaft",
            "Arbeit und Soziales",
            "Internationales und Europäisches Recht",
            "Geistiges Eigentum und Medien",
        ],
        "examensamt": "Landesjustizprüfungsamt Bayern",
        "besonderheiten": "Medienrecht, Kanonisches Recht",
    },
    "Universität Saarbrücken (Universität des Saarlandes)": {
        "bundesland": "Saarland",
        "schwerpunkte": [
            "Europarecht und Europäische Integration",
            "Internationales Recht",
            "Unternehmens- und Wirtschaftsrecht",
            "Kriminalwissenschaften",
            "Arbeit und Soziales",
            "Öffentliches Recht",
        ],
        "examensamt": "Landesjustizprüfungsamt Saarland",
        "besonderheiten": "Starkes Europarecht (Grenzlage zu Frankreich/Luxemburg), Institut für Rechtsinformatik",
    },
    "Freie Universität Berlin (FU)": {
        "bundesland": "Berlin",
        "schwerpunkte": [
            "Grundlagen des Rechts",
            "Wirtschaft und Steuern",
            "Kriminalwissenschaften",
            "Staat, Verwaltung und Verfassung",
            "Arbeit und Soziales",
            "Internationales und Europäisches Recht",
        ],
        "examensamt": "Gemeinsames Juristisches Prüfungsamt Berlin-Brandenburg",
        "besonderheiten": "Starkes Öffentliches Recht, Verwaltungsrecht, Nähe zu Bundesverfassungsgericht-Entscheidungen",
    },
    "Universität Tübingen (Eberhard Karls)": {
        "bundesland": "Baden-Württemberg",
        "schwerpunkte": [
            "Grundlagen und Geschichte des Rechts",
            "Wirtschafts- und Steuerrecht",
            "Kriminalwissenschaften",
            "Staat und Gesellschaft",
            "Arbeit und Soziales",
            "Internationales Recht",
        ],
        "examensamt": "Landesjustizprüfungsamt Baden-Württemberg",
        "besonderheiten": "Traditionsreiche Rechtsgeschichte, Methodenlehre, kritische Jurisprudenz",
    },
}

# ── Hilfsfunktionen ────────────────────────────────────────────

def get_all_unis() -> list[str]:
    """Gibt alle Universitätsnamen sortiert zurück."""
    return sorted(UNI_DATA.keys())


def get_bundesland(uni: str) -> str:
    """Gibt das Bundesland der Universität zurück oder leeren String."""
    return UNI_DATA.get(uni, {}).get("bundesland", "")


def get_schwerpunkte(uni: str) -> list[str]:
    """Gibt die Schwerpunktbereiche der gewählten Uni zurück."""
    return UNI_DATA.get(uni, {}).get("schwerpunkte", [])


def get_uni_info(uni: str) -> dict:
    """Gibt das vollständige Info-Dict der Universität zurück."""
    return UNI_DATA.get(uni, {})

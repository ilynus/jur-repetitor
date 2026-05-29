"""Gesetzesverzeichnis — Direkte Links zu gesetze-im-internet.de, Paragraphen-Direktsuche."""
from __future__ import annotations
import streamlit as st

from src.theme import apply_theme, section_header, gold_divider, page_header
from src.llm import chat_complete

apply_theme()

# ── GESETZES-DATEN ────────────────────────────────────────────────────────────

GESETZE: dict[str, list[dict]] = {
    "Zivilrecht": [
        {"kuerzel": "BGB",    "name": "Bürgerliches Gesetzbuch"},
        {"kuerzel": "HGB",    "name": "Handelsgesetzbuch"},
        {"kuerzel": "ZPO",    "name": "Zivilprozessordnung"},
        {"kuerzel": "InsO",   "name": "Insolvenzordnung"},
        {"kuerzel": "WEG",    "name": "Wohnungseigentumsgesetz"},
        {"kuerzel": "BGB",    "name": "Bürgerliches Gesetzbuch"},  # duplicate guard below
        {"kuerzel": "GmbHG",  "name": "GmbH-Gesetz"},
        {"kuerzel": "AktG",   "name": "Aktiengesetz"},
        {"kuerzel": "UWG",    "name": "Gesetz gegen unlauteren Wettbewerb"},
        {"kuerzel": "MarkenG","name": "Markengesetz"},
        {"kuerzel": "EGBGB",  "name": "Einführungsgesetz zum BGB"},
        {"kuerzel": "BNotO",  "name": "Bundesnotarordnung"},
        {"kuerzel": "RPflG",  "name": "Rechtspflegergesetz"},
    ],
    "Strafrecht": [
        {"kuerzel": "StGB",   "name": "Strafgesetzbuch"},
        {"kuerzel": "StPO",   "name": "Strafprozessordnung"},
        {"kuerzel": "JGG",    "name": "Jugendgerichtsgesetz"},
        {"kuerzel": "OWiG",   "name": "Ordnungswidrigkeitengesetz"},
        {"kuerzel": "BtMG",   "name": "Betäubungsmittelgesetz"},
        {"kuerzel": "GVG",    "name": "Gerichtsverfassungsgesetz"},
        {"kuerzel": "BZRG",   "name": "Bundeszentralregistergesetz"},
        {"kuerzel": "StrVollzG", "name": "Strafvollzugsgesetz"},
    ],
    "Öffentliches Recht": [
        {"kuerzel": "GG",     "name": "Grundgesetz"},
        {"kuerzel": "VwGO",   "name": "Verwaltungsgerichtsordnung"},
        {"kuerzel": "VwVfG",  "name": "Verwaltungsverfahrensgesetz"},
        {"kuerzel": "BVerfGG","name": "Bundesverfassungsgerichtsgesetz"},
        {"kuerzel": "BVerwGG","name": "Bundesverwaltungsgerichtsgesetz"},
        {"kuerzel": "BRRG",   "name": "Beamtenrechtsrahmengesetz"},
        {"kuerzel": "BBG",    "name": "Bundesbeamtengesetz"},
        {"kuerzel": "SGB_1",  "name": "Sozialgesetzbuch I — Allgemeiner Teil"},
        {"kuerzel": "SGG",    "name": "Sozialgerichtsgesetz"},
        {"kuerzel": "FGO",    "name": "Finanzgerichtsordnung"},
        {"kuerzel": "BauGB",  "name": "Baugesetzbuch"},
        {"kuerzel": "BImSchG","name": "Bundes-Immissionsschutzgesetz"},
        {"kuerzel": "WHG",    "name": "Wasserhaushaltsgesetz"},
        {"kuerzel": "BVFG",   "name": "Bundesvertriebenengesetz"},
        {"kuerzel": "AsylG",  "name": "Asylgesetz"},
        {"kuerzel": "AufenthG","name": "Aufenthaltsgesetz"},
    ],
    "Europarecht": [
        {"kuerzel": "AEUV",   "name": "Vertrag über die Arbeitsweise der EU"},
        {"kuerzel": "EUV",    "name": "Vertrag über die Europäische Union"},
        {"kuerzel": "EMRK",   "name": "Europäische Menschenrechtskonvention"},
        {"kuerzel": "GRC",    "name": "EU-Grundrechtecharta"},
    ],
    "Arbeitsrecht": [
        {"kuerzel": "BUrlG",  "name": "Bundesurlaubsgesetz"},
        {"kuerzel": "KSchG",  "name": "Kündigungsschutzgesetz"},
        {"kuerzel": "BetrVG", "name": "Betriebsverfassungsgesetz"},
        {"kuerzel": "ArbGG",  "name": "Arbeitsgerichtsgesetz"},
        {"kuerzel": "ArbZG",  "name": "Arbeitszeitgesetz"},
        {"kuerzel": "MuSchG", "name": "Mutterschutzgesetz"},
        {"kuerzel": "BEEG",   "name": "Bundeselterngeld- und Elternzeitgesetz"},
        {"kuerzel": "EntgFG",  "name": "Entgeltfortzahlungsgesetz"},
        {"kuerzel": "AGG",    "name": "Allgemeines Gleichbehandlungsgesetz"},
        {"kuerzel": "TVG",    "name": "Tarifvertragsgesetz"},
        {"kuerzel": "AÜG",    "name": "Arbeitnehmerüberlassungsgesetz"},
        {"kuerzel": "SGB_4",  "name": "Sozialgesetzbuch IV — Gemeinsame Vorschriften"},
    ],
    "Steuerrecht": [
        {"kuerzel": "AO",     "name": "Abgabenordnung"},
        {"kuerzel": "EStG",   "name": "Einkommensteuergesetz"},
        {"kuerzel": "UStG",   "name": "Umsatzsteuergesetz"},
        {"kuerzel": "KStG",   "name": "Körperschaftsteuergesetz"},
        {"kuerzel": "GewStG", "name": "Gewerbesteuergesetz"},
        {"kuerzel": "ErbStG", "name": "Erbschaft- und Schenkungsteuergesetz"},
        {"kuerzel": "GrStG",  "name": "Grundsteuergesetz"},
        {"kuerzel": "GrEStG", "name": "Grunderwerbsteuergesetz"},
        {"kuerzel": "UmwStG", "name": "Umwandlungssteuergesetz"},
        {"kuerzel": "FGO",    "name": "Finanzgerichtsordnung"},
    ],
}

# Sonderfall-Mappings für Kürzel, die nicht direkt als URL-Pfad funktionieren
URL_OVERRIDES: dict[str, str] = {
    "SGB_1":  "sgb-1",
    "SGB_4":  "sgb-4",
    "BNotO":  "bnoto",
    "RPflG":  "rpflg",
    "BRRG":   "brrg",
    "BVFG":   "bvfg",
    "BZRG":   "bzrg",
    "GRC":    "grcharta",
    "BVerwGG":"bverwgg",
    "BEEG":   "beeg",
    "EntgFG": "entgfg",
    "AÜG":    "aueg",
}

CATEGORY_ICONS: dict[str, str] = {
    "Zivilrecht":      "⚖️",
    "Strafrecht":      "🔒",
    "Öffentliches Recht": "🏛️",
    "Europarecht":     "🇪🇺",
    "Arbeitsrecht":    "👷",
    "Steuerrecht":     "💰",
}


def gesetz_url(kuerzel: str) -> str:
    """Gibt die Index-URL für ein Gesetz auf gesetze-im-internet.de zurück."""
    slug = URL_OVERRIDES.get(kuerzel, kuerzel.lower())
    return f"https://www.gesetze-im-internet.de/{slug}/"


def paragraph_url(kuerzel: str, nr: str) -> str:
    """Baut URL für einen einzelnen Paragraphen."""
    slug = URL_OVERRIDES.get(kuerzel, kuerzel.lower())
    return f"https://www.gesetze-im-internet.de/{slug}/_{nr}.html"


# ── SEITEN-HEADER ─────────────────────────────────────────────────────────────

page_header(
    "Gesetzesverzeichnis",
    "Direkte Links zu gesetze-im-internet.de · Paragraphen-Direktsuche",
    "📜",
)

gold_divider()

# ── LAYOUT: Suchleiste + Paragraphen-Suche oben ──────────────────────────────

col_search, col_para = st.columns([3, 2])

with col_search:
    section_header("🔍", "Gesetz suchen")
    suche = st.text_input(
        "Suche",
        placeholder="Kürzel oder Name eingeben, z.B. BGB, Strafgesetzbuch …",
        label_visibility="collapsed",
        key="gesetze_suche",
    )

with col_para:
    section_header("§", "Paragraphen-Direktsuche")
    p_col1, p_col2, p_col3 = st.columns([2, 3, 2])
    with p_col1:
        para_nr = st.text_input(
            "§",
            placeholder="433",
            label_visibility="collapsed",
            key="para_nr",
        )
    with p_col2:
        # Flache Liste aller Kürzel für Selectbox
        alle_kuerzel = list(dict.fromkeys(
            g["kuerzel"]
            for gesetze in GESETZE.values()
            for g in gesetze
        ))
        para_gesetz = st.selectbox(
            "Gesetz",
            alle_kuerzel,
            label_visibility="collapsed",
            key="para_gesetz",
        )
    with p_col3:
        if para_nr.strip() and para_gesetz:
            nr_clean = para_nr.strip().lstrip("§").strip()
            p_url = paragraph_url(para_gesetz, nr_clean)
            st.link_button(
                f"§ {nr_clean} {para_gesetz}",
                url=p_url,
                type="primary",
                use_container_width=True,
            )
        else:
            st.button("Nachschlagen", disabled=True, use_container_width=True)

gold_divider()

# ── GESETZES-LISTE ────────────────────────────────────────────────────────────

suche_lower = suche.strip().lower() if suche else ""

# Prüfe ob Suchergebnis in einem Rechtsgebiet vorhanden ist
def gesetz_matches(g: dict, q: str) -> bool:
    if not q:
        return True
    return q in g["kuerzel"].lower() or q in g["name"].lower()


def render_gesetze_kategorie(kategorie: str, gesetze: list[dict], query: str) -> None:
    """Rendert eine Kategorie mit ihren Gesetzen (dedupliziert, gefiltert)."""
    # Deduplizieren nach Kürzel
    seen: set[str] = set()
    unique: list[dict] = []
    for g in gesetze:
        if g["kuerzel"] not in seen:
            seen.add(g["kuerzel"])
            unique.append(g)

    # Filtern
    filtered = [g for g in unique if gesetz_matches(g, query)]
    if not filtered:
        return

    icon = CATEGORY_ICONS.get(kategorie, "📄")
    section_header(icon, kategorie)

    # Responsive Grid: 3 Spalten
    cols = st.columns(3)
    for idx, g in enumerate(filtered):
        url = gesetz_url(g["kuerzel"])
        with cols[idx % 3]:
            st.markdown(
                f"""<div style="background:white;border:1px solid #edeae0;border-radius:10px;
                padding:.75rem 1rem;margin-bottom:.5rem;
                box-shadow:0 1px 3px rgba(26,39,68,.06);
                transition:box-shadow .2s cubic-bezier(.4,0,.2,1),transform .2s cubic-bezier(.4,0,.2,1)">
                <div style="display:flex;align-items:baseline;gap:.45rem;margin-bottom:.15rem">
                  <span style="font-family:'IBM Plex Mono',monospace;font-size:.82rem;font-weight:600;
                    color:#1a2744;background:rgba(26,39,68,.07);padding:.1rem .4rem;
                    border-radius:4px">{g['kuerzel']}</span>
                  <span style="font-family:'IBM Plex Sans',sans-serif;font-size:.78rem;
                    color:#57534e;line-height:1.4">{g['name']}</span>
                </div></div>""",
                unsafe_allow_html=True,
            )
            st.link_button(
                f"Öffnen — {g['kuerzel']}",
                url=url,
                use_container_width=True,
            )


# Kategorie-Tabs wenn keine Suche aktiv, sonst alle zeigen
if not suche_lower:
    tab_labels = [f"{CATEGORY_ICONS.get(k,'📄')} {k}" for k in GESETZE]
    tabs = st.tabs(tab_labels)
    for tab, (kategorie, gesetze) in zip(tabs, GESETZE.items()):
        with tab:
            render_gesetze_kategorie(kategorie, gesetze, "")
else:
    # Bei Suche: alle Kategorien durchsuchen und Treffer anzeigen
    treffer_gesamt = sum(
        1
        for gesetze in GESETZE.values()
        for g in gesetze
        if gesetz_matches(g, suche_lower)
    )
    if treffer_gesamt == 0:
        st.info(f'Kein Gesetz gefunden für „{suche}“.')
    else:
        st.caption(f'{treffer_gesamt} Treffer für „{suche}“')
        for kategorie, gesetze in GESETZE.items():
            render_gesetze_kategorie(kategorie, gesetze, suche_lower)

gold_divider()

# ── HINWEIS ───────────────────────────────────────────────────────────────────
st.markdown(
    '<p style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.76rem;'
    'color:#78716c;text-align:center;margin-top:.25rem">'
    'Alle Links führen zu <strong>gesetze-im-internet.de</strong> — dem amtlichen '
    'Bundesrecht des Bundesministeriums der Justiz.</p>',
    unsafe_allow_html=True,
)

gold_divider()

# ── ⚖️ AUSLEGUNG ──────────────────────────────────────────────────────────────

section_header("⚖️", "Drei-Perspektiven-Auslegung")

st.markdown(
    '<p style="font-family:\'IBM Plex Sans\',sans-serif;font-size:.85rem;color:#57534e;'
    'margin-bottom:.75rem">Gib eine Norm ein und lass dir drei unabhängige '
    'Auslegungsperspektiven (Literatur, Rechtsprechung, Gesetzgeber) von Claude erklären.</p>',
    unsafe_allow_html=True,
)

norm_input = st.text_input(
    "Norm eingeben",
    placeholder="z.B. § 242 BGB, § 263 StGB, Art. 5 GG",
    key="auslegung_norm_input",
)

col1, col2, col3 = st.columns(3)
with col1:
    do_lit = st.checkbox("📚 Literatur", value=True, key="auslegung_cb_lit")
with col2:
    do_rspr = st.checkbox("⚖️ Rechtsprechung", value=True, key="auslegung_cb_rspr")
with col3:
    do_gesetzgeber = st.checkbox("🏛️ Gesetzgeber", value=True, key="auslegung_cb_gesetzgeber")

if st.button("🔍 Auslegung abrufen", type="primary", key="auslegung_btn") and norm_input:
    norm_clean = norm_input.strip()

    # ── System-Prompts für die drei Perspektiven ─────────────────────────────
    PERSPEKTIVEN = [
        {
            "key": "lit",
            "active": do_lit,
            "label": "📚 Literatur",
            "color": "#1d4ed8",
            "bg": "#eff6ff",
            "border": "#93c5fd",
            "system": (
                "Du bist ein Rechtswissenschaftler mit umfassendem Überblick über die "
                "juristische Fachliteratur. Erkläre die herrschende Meinung in der Literatur "
                f"zu {{norm}}. Nenne konkret: hM, aA, wichtige Streitstände. Zitiere Kommentare "
                "wie Palandt/Grüneberg, MüKo (Münchener Kommentar), Staudinger und weitere "
                "führende Kommentierungen mit typischen Fundstellen (§, Rn.). Strukturiere "
                "die Antwort klar mit kurzen Abschnitten."
            ),
            "user": f"Erkläre die Literaturmeinung zu {norm_clean}.",
        },
        {
            "key": "rspr",
            "active": do_rspr,
            "label": "⚖️ Rechtsprechung",
            "color": "#15803d",
            "bg": "#f0fdf4",
            "border": "#86efac",
            "system": (
                "Du bist ein erfahrener Richter mit tiefem Einblick in die höchstrichterliche "
                "Rechtsprechung. Fasse die wichtigsten BGH-, BVerfG- und BAG-Entscheidungen "
                f"zu {{norm}} zusammen. Nenne echte Aktenzeichen und Leitsätze. Erkläre die "
                "Entwicklung der Rechtsprechung chronologisch und hebe Leitentscheidungen "
                "besonders hervor. Zeige auf, wo die Rechtsprechung von der Literatur abweicht."
            ),
            "user": f"Fasse die wichtigsten Entscheidungen der Rechtsprechung zu {norm_clean} zusammen.",
        },
        {
            "key": "gesetzgeber",
            "active": do_gesetzgeber,
            "label": "🏛️ Gesetzgeber",
            "color": "#92400e",
            "bg": "#fffbeb",
            "border": "#fcd34d",
            "system": (
                "Du bist Verfassungsjurist und Gesetzgebungsexperte. Erkläre die "
                f"Gesetzgebungsgeschichte von {{norm}}: ursprüngliche Gesetzesbegründung, "
                "relevante BT-Drucksachen, spätere Änderungen und deren Begründungen. "
                "Was wollte der Gesetzgeber mit der Norm ursprünglich erreichen? Welche "
                "Zwecke und Ziele werden in den Materialien genannt? Erkläre auch den "
                "historischen Kontext der Normentstehung."
            ),
            "user": f"Erkläre die Gesetzgebungsgeschichte und den Willen des Gesetzgebers zu {norm_clean}.",
        },
    ]

    active_perspektiven = [p for p in PERSPEKTIVEN if p["active"]]

    if not active_perspektiven:
        st.warning("Bitte wähle mindestens eine Perspektive aus.")
    else:
        # Ergebnisse abrufen (mit Session-State-Cache)
        for p in active_perspektiven:
            cache_key = f"auslegung_{norm_clean}_{p['key']}"
            if cache_key not in st.session_state:
                with st.spinner(f"{p['label']} wird abgerufen …"):
                    system_prompt = p["system"].replace("{norm}", norm_clean)
                    result = chat_complete(
                        messages=[{"role": "user", "content": p["user"]}],
                        system_prompt=system_prompt,
                    )
                    st.session_state[cache_key] = result

        # Ergebnisse anzeigen
        display_cols = st.columns(len(active_perspektiven))
        for col, p in zip(display_cols, active_perspektiven):
            cache_key = f"auslegung_{norm_clean}_{p['key']}"
            result_text = st.session_state.get(cache_key, "")
            with col:
                container = st.container()
                with container:
                    st.markdown(
                        f'<div style="background:{p["bg"]};border:1px solid {p["border"]};'
                        f'border-radius:10px;padding:1rem 1.1rem;margin-bottom:.5rem">'
                        f'<span style="font-family:\'IBM Plex Sans\',sans-serif;'
                        f'font-size:1rem;font-weight:700;color:{p["color"]}">'
                        f'{p["label"]}</span></div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(result_text)

# Zeige gecachte Ergebnisse wenn vorhanden (auch ohne erneuten Button-Klick)
elif norm_input:
    norm_clean = norm_input.strip()
    cached_perspektiven = []
    for key_suffix, label, color, bg, border in [
        ("lit", "📚 Literatur", "#1d4ed8", "#eff6ff", "#93c5fd"),
        ("rspr", "⚖️ Rechtsprechung", "#15803d", "#f0fdf4", "#86efac"),
        ("gesetzgeber", "🏛️ Gesetzgeber", "#92400e", "#fffbeb", "#fcd34d"),
    ]:
        cache_key = f"auslegung_{norm_clean}_{key_suffix}"
        if cache_key in st.session_state:
            cached_perspektiven.append((label, color, bg, border, st.session_state[cache_key]))

    if cached_perspektiven:
        st.caption(f"Gespeicherte Auslegung für **{norm_clean}** (aus Cache):")
        display_cols = st.columns(len(cached_perspektiven))
        for col, (label, color, bg, border, result_text) in zip(display_cols, cached_perspektiven):
            with col:
                st.markdown(
                    f'<div style="background:{bg};border:1px solid {border};'
                    f'border-radius:10px;padding:1rem 1.1rem;margin-bottom:.5rem">'
                    f'<span style="font-family:\'IBM Plex Sans\',sans-serif;'
                    f'font-size:1rem;font-weight:700;color:{color}">'
                    f'{label}</span></div>',
                    unsafe_allow_html=True,
                )
                st.markdown(result_text)

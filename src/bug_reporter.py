"""Bug-Reporter — speichert Meldungen in PATH_FEEDBACK (shared → Admin sieht alle)."""
from __future__ import annotations
import uuid
import streamlit as st

from src.config import PATH_FEEDBACK
from src.github_db import read_json, write_json, now_iso


def save_bug_report(typ: str, beschreibung: str, seite: str = "", user: str = "anonym") -> bool:
    """Speichert einen Bug-Report. Gibt True bei Erfolg zurück, False bei Fehler."""
    return _save_report({
        "typ": typ,
        "beschreibung": beschreibung,
        "seite": seite,
        "user": user,
        "timestamp": now_iso(),
        "quelle": "sidebar",
    })


def _save_report(report: dict) -> bool:
    report.setdefault("id", str(uuid.uuid4())[:8])
    report.setdefault("status", "offen")
    report.setdefault("user", st.session_state.get("auth_user", {}).get("username", "anonym"))
    try:
        all_reports = read_json(PATH_FEEDBACK(), default=[]) or []
        all_reports.append(report)
        return write_json(
            PATH_FEEDBACK(), all_reports,
            commit_msg=f"bug: {report.get('typ','?')} — {str(report.get('beschreibung',''))[:40]}"
        )
    except Exception:
        return False

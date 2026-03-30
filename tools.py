import json
import os
import re

DATA_PATH = os.path.join("data", "faq.json")


def load_faq_data():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


FAQ_DATA = load_faq_data()


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def detect_tool(user_query: str) -> str:
    q = normalize_text(user_query)

    summarize_keywords = ["summarize:", "summary:", "summarise:", "summarize this"]
    faq_keywords = [
        "leave policy",
        "annual leave",
        "vacation leave",
        "remote work",
        "work from home",
        "wfh policy",
        "password reset",
        "reset password",
        "forgot password",
        "laptop support",
        "device issue",
        "it support",
        "contact hr",
        "hr support",
        "policy",
        "faq",
        "helpdesk",
    ]

    if any(keyword in q for keyword in summarize_keywords):
        return "summarize_text"

    if any(keyword in q for keyword in faq_keywords):
        return "faq_lookup"

    return "general_agent"


def faq_lookup(user_query: str) -> str:
    q = normalize_text(user_query)

    best_match = None
    best_score = 0

    for item in FAQ_DATA:
        score = 0
        keywords = item.get("keywords", [])
        for kw in keywords:
            if kw.lower() in q:
                score += 1

        if score > best_score:
            best_score = score
            best_match = item

    if best_match:
        return (
            f"Category: {best_match.get('category', 'General')}\n\n"
            f"Answer: {best_match.get('answer', '')}\n\n"
            f"Escalation / Contact: {best_match.get('contact', 'Not specified')}"
        )

    return ""


def summarize_text(text: str) -> str:
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

    if not sentences:
        return "I could not find enough content to summarize."

    key_points = sentences[:3]

    return (
        "Summary:\n"
        + "\n".join([f"- {point}" for point in key_points])
        + "\n\nNote: This is a lightweight built-in summarizer in the demo."
    )


def is_supported_query(user_query: str) -> bool:
    q = normalize_text(user_query)

    blocked_topics = [
        "hack",
        "bypass",
        "malware",
        "exploit",
        "make a bomb",
        "weapon",
        "steal password",
        "phishing",
    ]

    if any(term in q for term in blocked_topics):
        return False

    return True


def format_safe_refusal() -> str:
    return (
        "I can help with internal FAQ, policy, IT support, and summarization queries only. "
        "I cannot assist with unsafe, harmful, or unrelated requests."
    )
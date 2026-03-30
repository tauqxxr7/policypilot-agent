import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

from tools import (
    detect_tool,
    faq_lookup,
    summarize_text,
    is_supported_query,
    format_safe_refusal,
)

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = None
if GEMINI_API_KEY:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Gemini client initialization failed: {e}")
        client = None


SYSTEM_PROMPT = """
You are PolicyPilot, a production-aware enterprise support agent.

Your goals:
1. Help users with internal FAQ, support, and policy-related queries.
2. Be safe, concise, and grounded.
3. Do not invent company policies that are not given.
4. If a query is outside supported scope, politely refuse.
5. If the answer comes from local policy/FAQ data, present it clearly.
6. For summaries, keep the output structured and helpful.

Supported areas:
- HR and leave policy basics
- IT support basics
- Password reset guidance
- Remote work guidance
- Laptop support / helpdesk routing
- Summarization of user-provided text

Style:
- Professional
- Clear
- Short paragraphs
- No unnecessary jargon
"""


def generate_with_gemini(user_query: str, context: str = "") -> str:
    if not client:
        return (
            "Gemini is not configured right now. "
            "Please set your GEMINI_API_KEY in the .env file and restart the app."
        )

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

User query:
{user_query}

Respond helpfully and safely.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error while calling Gemini: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = (data.get("message") or "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a message."})

    if not is_supported_query(user_message):
        return jsonify({"reply": format_safe_refusal()})

    selected_tool = detect_tool(user_message)

    if selected_tool == "faq_lookup":
        faq_result = faq_lookup(user_message)
        if faq_result:
            return jsonify({"reply": faq_result})

        gemini_reply = generate_with_gemini(
            user_message,
            context="No exact local FAQ match was found. Stay within enterprise support scope."
        )
        return jsonify({"reply": gemini_reply})

    if selected_tool == "summarize_text":
        summary_input = (
            user_message.replace("summarize:", "")
            .replace("summary:", "")
            .replace("summarise:", "")
            .strip()
        )
        if not summary_input:
            return jsonify({"reply": "Please paste the text after 'summarize:'"})
        local_summary = summarize_text(summary_input)
        return jsonify({"reply": local_summary})

    gemini_reply = generate_with_gemini(
        user_message,
        context=(
            "This is an enterprise support agent demo. "
            "Prefer practical, policy-safe, organization-support answers."
        )
    )
    return jsonify({"reply": gemini_reply})


if __name__ == "__main__":
    app.run(debug=True)
# PolicyPilot

PolicyPilot is a production-aware AI support agent designed to improve internal enterprise support workflows through policy assistance, FAQ lookup, support routing, and summarization.

## Problem Statement
Organizations need an AI capability that improves a specific internal workflow while remaining safe, reliable, and easy to integrate.

## Solution
PolicyPilot acts as an enterprise AI support assistant that:
- answers internal FAQ and policy questions
- routes support-related queries
- summarizes incident or support text
- refuses unsafe or unsupported prompts

## Key Features
- Tool-based query routing
- Local FAQ/policy knowledge base
- Built-in summarization workflow
- Safety refusal layer
- Clean dashboard-style UI
- Gemini integration for broader AI responses

## Architecture
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- AI Layer: Gemini API
- Data Layer: JSON-based FAQ store
- Agent Logic: intent detection + tool routing + safety controls

## How It Works
1. User enters a query in the chat interface.
2. The agent identifies the user intent.
3. The query is routed to the correct tool:
   - FAQ lookup
   - summarization
   - general AI response
4. The system applies safety checks before responding.
5. The final answer is displayed in the dashboard.

## Example Queries
- What is the leave policy?
- How do I reset my password?
- What is the remote work policy?
- summarize: [paste text here]

## Setup
Future Improvements
Database-backed knowledge retrieval
Ticket creation integrations
Authentication and access controls
Cloud deployment with logging and monitoring
```bash
pip install -r requirements.txt
python app.py

# PolicyPilot Agent

> AI support agent for policy assistance, FAQ handling, routing, summarization, and safe response workflows.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Flask](https://img.shields.io/badge/Flask-0F172A?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Gemini_API-1A73E8?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

[![Source Code](https://img.shields.io/badge/Source_Code-111827?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tauqxxr7/policypilot-agent)

## Problem

Internal support teams repeatedly answer the same policy and IT questions, route common requests, and summarize issue context. Generic chatbots often overstep policy boundaries or answer without proper grounding.

## Solution

PolicyPilot Agent is a production-aware support assistant that combines FAQ retrieval, policy assistance, summarization, routing, and safety controls into one focused workflow.

## Features

- FAQ lookup
- Policy assistance
- Support routing
- Text summarization
- Safety refusal layer
- Lightweight dashboard-style UI

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask
- AI layer: Gemini API
- Data layer: local JSON FAQ store
- Logic layer: intent routing plus safety checks

## Architecture

```text
User query -> Flask app -> intent detection -> FAQ lookup or summarization or Gemini response -> safety checks -> UI response
```

This project is designed for real-world usage and demonstrates a production-style workflow with routing, safety, and grounded responses.

## ⚙️ Engineering Notes

- Built with clear frontend/backend/API separation
- Designed for deployable architecture (Vercel + Render style)
- Uses modular structure for scalability and maintainability
- Focused on real-world use cases, not isolated demos

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/tauqxxr7/policypilot-agent.git
cd policypilot-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask python-dotenv google-genai
```

### 4. Add environment variables

```bash
copy .env.example .env
```

### 5. Run the app

```bash
python app.py
```

Open the app at `http://127.0.0.1:5000`

## Environment Variables

```env
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=development
PORT=5000
```

## 📸 Screenshots

Screenshots coming soon

## 🚀 Deployment

Deployment in progress (planned: Vercel / Render)

## Future Improvements

- Database-backed retrieval
- Helpdesk or ticketing integrations
- Authentication and role-aware access control
- Logging and monitoring
- Expanded enterprise workflow automation

## Author

Built by **Tauqeer Bharde** as an AI support workflow project focused on safe responses, maintainable architecture, and deployability.

## Suggested GitHub Topics

`ai-agent, policy-assistant, enterprise-ai, faq-bot, python, genai, llm, automation, support-agent`

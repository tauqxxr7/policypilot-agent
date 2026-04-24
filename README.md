# PolicyPilot Agent

> AI-powered enterprise support assistant for FAQ lookup, policy guidance, routing, summarization, and safe responses.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Flask](https://img.shields.io/badge/Flask-0F172A?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Gemini_API-1A73E8?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

[![Source Code](https://img.shields.io/badge/Source_Code-111827?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tauqxxr7/policypilot-agent)

## Overview

PolicyPilot Agent is a production-aware AI support assistant built for internal enterprise workflows. It is designed to help teams answer policy questions, guide users through support issues, summarize text, and refuse unsupported or unsafe requests.

This project demonstrates more than just a chat UI. It shows intent detection, tool routing, local knowledge lookup, safety controls, and model-backed assistance in a clean full-stack flow.

## Problem

Internal support teams lose time answering repetitive questions, routing common requests, and summarizing issue context. Generic chatbots often hallucinate policies or respond beyond their safe operating scope.

## Solution

PolicyPilot solves that by combining:

- FAQ and policy retrieval from local structured data
- Query routing based on user intent
- Summarization for support or incident text
- Guardrails that refuse unsupported prompts
- Gemini-powered fallback responses for valid in-scope requests

## Core Features

- Enterprise FAQ and policy assistance
- Password reset and IT support guidance
- Remote work and leave-policy query handling
- Summarization flow for pasted text
- Safe refusal layer for unsupported requests
- Lightweight dashboard-style interface

## Architecture

```text
User Query
  -> Flask app
  -> intent detection and tool selection
  -> FAQ lookup or summarization or Gemini response
  -> safety validation
  -> final response in UI
```

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask
- AI layer: Gemini API
- Knowledge layer: local JSON FAQ store
- Logic layer: intent routing plus safety controls

## Example Queries

- `What is the leave policy?`
- `How do I reset my password?`
- `What is the remote work policy?`
- `summarize: [paste text here]`

## Local Setup

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

`.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
FLASK_ENV=development
PORT=5000
```

### 5. Run the app

```bash
python app.py
```

Open the app at `http://127.0.0.1:5000`

## Screenshots

### Main Dashboard

`Add screenshot: docs/screenshots/dashboard.png`

### FAQ / Policy Response State

`Add screenshot: docs/screenshots/faq-response.png`

### Summarization Flow

`Add screenshot: docs/screenshots/summarization.png`

## Demo Placeholder

- Live demo: `Add deployment URL here`
- Source code: `https://github.com/tauqxxr7/policypilot-agent`

## Future Improvements

- Database-backed retrieval
- Ticketing or helpdesk integrations
- Authentication and role-aware access control
- Logging, analytics, and monitoring
- Stronger enterprise workflow automation

## License

Built for experimentation, AI workflow demos, and portfolio use.

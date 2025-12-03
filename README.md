# Marketing Agent (CrewAgent)

**Marketing Agent** (also referenced as `crewagent`) is a small collection of tools and configurable agents for automating marketing tasks using LLM-driven agents. It includes role-configurable agents, task templates, and a few helper tools (email sender, SERP helper) to build marketing workflows.

---

## Project structure

```
Marketing_Agent-main/
├─ marketingCrew/
│  ├─ config/
│  │  ├─ agents.yaml       # Agent role definitions (LLM, role prompts, backstory)
│  │  └─ tasks.yaml        # Task templates and expected outputs
│  └─ crew.py              # Crew loader / orchestrator for agents/tasks
├─ emailagent.py           # Example email agent wrapper
├─ email_agent_tool.py     # Email sending helper/tool
├─ serptool.py             # Simple SERP / search helper (example)
├─ testapi.py              # Minimal example to call an LLM API (uses env API_KEY)
├─ pyproject.toml          # Project config / dependency declaration
└─ README.md               # This file
```

---

## What this repo provides

- **Config-driven agents** — `marketingCrew/config/agents.yaml` defines roles (e.g., Head of Marketing, Content Creator) with LLM model references and prompt/backstory.  
- **Task templates** — `marketingCrew/config/tasks.yaml` holds common marketing tasks (market research, content planning, ad copy, social posts) and expected outputs.  
- **Crew orchestrator** — `marketingCrew/crew.py` loads agent and task configuration and demonstrates how to instantiate agents and run tasks.  
- **Helpers** — `email_agent_tool.py`, `emailagent.py`, and `serptool.py` show example utilities for email sending and search result parsing.  
- **Example API call** — `testapi.py` demonstrates a minimal HTTP call to a generative LLM endpoint using `API_KEY` from environment.

---

## Requirements

- Python 3.11+
- `crewai[tools]>=0.175.0` (declared in `pyproject.toml`)
- `requests`, `python-dotenv` (used in `testapi.py`) — install via pip if not already present.

Install dependencies (example):

```bash
python -m pip install --upgrade pip
python -m pip install "crewai[tools]>=0.175.0" python-dotenv requests
```

---

## Setup

1. **Clone or extract** the project into your workspace.
2. **Create a `.env`** file at the project root (do NOT commit this to git). Example `.env`:

```
API_KEY=your_llm_or_google_cloud_api_key_here
```

3. Add `.env` to `.gitignore` (there is a `.gitignore` present in the repo).

---

## Configuration

- `marketingCrew/config/agents.yaml` — contains agent definitions. Each agent entry typically has:
  - `llm`: model identifier (e.g., `gemini/gemini-2.0-flash`)
  - `role`, `goal`, `backstory`: prompt fragments that shape the agent's behavior

- `marketingCrew/config/tasks.yaml` — contains task names, `description`, `expected_output` and templates. Tasks use template variables (e.g., `{product_name}`, `{budget}`) — replace them before running.

---

## Usage

There are multiple entry points / examples:

### 1. Loading the crew (example)
Open `marketingCrew/crew.py` to see how config is loaded. Typically you'll:

```python
from marketingCrew.crew import load_crew

crew = load_crew(config_dir="marketingCrew/config")
# choose agent & task, then run
```

(See `crew.py` for exact function names and usage — it loads `agents.yaml` and `tasks.yaml` and provides helpers to create agent instances.)

### 2. Test API call
`testapi.py` shows a minimal example to call a generative LLM HTTP endpoint using `API_KEY` from environment variables. This is useful to test your API key and endpoint.

Run:

```bash
python testapi.py
```

### 3. Email tool
`email_agent_tool.py` and `emailagent.py` contain simple wrappers demonstrating how an agent could format and send emails. Inspect these files to adapt to your SMTP/API provider.

---

## Example workflows

- **Market research** — Fill the market research task template in `tasks.yaml` with product details and run it with a Head of Marketing agent to produce a research report.
- **Content creation** — Use `content_creator_social_media` agent to generate social post ideas or captions based on task templates.
- **Campaign planning** — Compose campaign briefs, budget proposals, and ad copy by combining agents and tasks.

---

## Security & best practices

- **Never commit secrets**. Keep `.env` out of version control.
- **Rotate keys** if you accidentally leak them.
- **Limit API usage** while testing to avoid unexpected charges.

---

## Extending the project

- Add more agents to `agents.yaml` with different LLMs or different prompt backstories.
- Add new tasks to `tasks.yaml` for other marketing needs (SEO audit, influencer outreach, analytics reporting).
- Implement connectors in `email_agent_tool.py` for real email APIs (SendGrid, SES) and add authentication/config in a secure way.

---

## Troubleshooting

- If the LLM requests fail, verify `API_KEY` and network access.
- If dependencies are missing, reinstall per the Requirements section.
- Check `pyproject.toml` for package expectations.

---

## License

This repository has no license file included. Add a `LICENSE` file (e.g., MIT) if you want to open-source the project.

---

## Contact / Next steps

If you'd like, I can:
- Create a polished README with badges and usage examples.
- Add CLI scripts to run tasks.
- Convert task templates into a small web UI for easier input.

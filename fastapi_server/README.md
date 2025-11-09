# OpenNexus FastAPI Stub

What this is:
- Minimal FastAPI app that exposes example endpoints compatible with the OpenNexus OpenAPI spec.
- Protects endpoints with X-API-KEY header (env var OPENNEXUS_API_KEY, default "test-key").
- Returns example responses (does not execute shell or Python code).

Run locally:
- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- OPENNEXUS_API_KEY=mykey python main.py

Expose OpenAPI:
- FastAPI serves OpenAPI JSON at /openapi.json and Swagger UI at /docs.
- Use the /openapi.json URL in ChatGPT Custom GPT builder as the API definition URL.

Security note:
- This stub is safe for testing: it does not run arbitrary commands or Python code.
- Replace stubs with safe, audited implementations before production use.

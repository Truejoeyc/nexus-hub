# nexus-hub

This repo contains:
- openapi-expanded.yaml — OpenAPI 3.1 definition for OpenNexus Agent API (used by ChatGPT Custom GPTs).
- fastapi_server/ — minimal FastAPI stub (exposes /openapi.json automatically).
- typescript_client/ — small axios-based client.

Quick start:
1. Push this repo to GitHub: Truejoeyc/nexus-hub (the assistant will commit these files).
2. Deploy the FastAPI app (Cloud Run, Railway, Vercel, or a host). The OpenAPI is available at https://<your-host>/openapi.json.
3. In ChatGPT Custom GPT builder, add a new API tool and point it to the OpenAPI URL (raw GitHub URL or the deployed /openapi.json). Configure the API key header X-API-KEY with your API key.

Notes:
- The server is a safe stub that does not execute arbitrary code.
- Replace stubs with secure implementations before production.

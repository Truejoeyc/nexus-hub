from typing import Optional
import os
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
import uvicorn

API_KEY_NAME = "X-API-KEY"
EXPECTED_API_KEY = os.getenv("OPENNEXUS_API_KEY", "test-key")

app = FastAPI(title="OpenNexus Agent API - FastAPI Stub", version="1.0.0")

def require_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return x_api_key


class CommandRequest(BaseModel):
    command: str


class OutputResponse(BaseModel):
    output: str


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    title: str
    link: str
    snippet: str


class SearchResponse(BaseModel):
    results: list[SearchResult]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tools/bash", response_model=OutputResponse)
def run_bash(req: CommandRequest, api_key: str = Depends(require_api_key)):
    # NOTE: this stub does NOT execute commands (for safety). Return an example response.
    example = f"Simulated run: {req.command}"
    return OutputResponse(output=example)


@app.post("/tools/web_search", response_model=SearchResponse)
def web_search(req: SearchRequest, api_key: str = Depends(require_api_key)):
    # Return a canned example response — replace with real search integration.
    return SearchResponse(
        results=[
            SearchResult(
                title="OpenNexus Home",
                link="https://opennexus.example/docs",
                snippet="OpenNexus is a hypercore-based runtime..."
            )
        ]
    )


@app.post("/tools/python", response_model=OutputResponse)
def run_python_code(payload: dict, api_key: str = Depends(require_api_key)):
    # Very intentionally: do not execute arbitrary code in this stub.
    return OutputResponse(output="Execution disabled in stub; returned example output.")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
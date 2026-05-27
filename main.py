from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Agentic AI Summit 2026 — Sponsor Mockups")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SPONSORS = {
    "platinum": [
        {"name": "Daytona", "url": "https://www.daytona.io/"},
        {"name": "Lambda", "url": "https://lambda.ai/"},
        {"name": "Ema.ai", "url": "https://www.ema.ai/"},
        {"name": "Replit", "url": "https://replit.com/"},
        {"name": "E2B", "url": "https://e2b.dev/"},
        {"name": "SAP", "url": "https://www.sap.com/"},
        {"name": "AMD", "url": "https://www.amd.com/"},
    ],
    "gold": [
        {"name": "Snorkel AI", "url": "https://snorkel.ai/"},
        {"name": "Nebius", "url": "https://nebius.com/"},
        {"name": "Databricks", "url": "https://www.databricks.com/"},
    ],
    "silver": [
        {"name": "Samsung NEXT", "url": "https://www.samsungnext.com/"},
        {"name": "McKinsey", "url": "https://www.mckinsey.com/"},
        {"name": "vijil.ai", "url": "https://vijil.ai/"},
        {"name": "OutSystems", "url": "https://www.outsystems.com/"},
        {"name": "Vessl", "url": "https://vessl.ai/"},
        {"name": "Akash", "url": "https://akash.network/"},
    ],
    "bronze": [
        {"name": "Fastino.ai", "url": "#"},
        {"name": "Linux / PyTorch", "url": "https://pytorch.org/"},
        {"name": "Elastic", "url": "https://www.elastic.co/"},
    ],
}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/option-a", response_class=HTMLResponse)
async def option_a(request: Request):
    return templates.TemplateResponse("option_a.html", {"request": request, "sponsors": SPONSORS})

@app.get("/option-b", response_class=HTMLResponse)
async def option_b(request: Request):
    return templates.TemplateResponse("option_b.html", {"request": request, "sponsors": SPONSORS})

@app.get("/option-c", response_class=HTMLResponse)
async def option_c(request: Request):
    return templates.TemplateResponse("option_c.html", {"request": request, "sponsors": SPONSORS})

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

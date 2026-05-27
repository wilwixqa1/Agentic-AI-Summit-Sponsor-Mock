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
        {"name": "Daytona", "url": "https://www.daytona.io/", "logo": "https://logo.clearbit.com/daytona.io"},
        {"name": "Lambda", "url": "https://lambda.ai/", "logo": "https://logo.clearbit.com/lambdalabs.com"},
        {"name": "Ema.ai", "url": "https://www.ema.ai/", "logo": "https://logo.clearbit.com/ema.ai"},
        {"name": "Replit", "url": "https://replit.com/", "logo": "https://logo.clearbit.com/replit.com"},
        {"name": "E2B", "url": "https://e2b.dev/", "logo": "https://logo.clearbit.com/e2b.dev"},
        {"name": "SAP", "url": "https://www.sap.com/", "logo": "https://logo.clearbit.com/sap.com"},
        {"name": "AMD", "url": "https://www.amd.com/", "logo": "https://logo.clearbit.com/amd.com"},
    ],
    "gold": [
        {"name": "Snorkel AI", "url": "https://snorkel.ai/", "logo": "https://logo.clearbit.com/snorkel.ai"},
        {"name": "Nebius", "url": "https://nebius.com/", "logo": "https://logo.clearbit.com/nebius.com"},
        {"name": "Databricks", "url": "https://www.databricks.com/", "logo": "https://logo.clearbit.com/databricks.com"},
    ],
    "silver": [
        {"name": "Samsung NEXT", "url": "https://www.samsungnext.com/", "logo": "https://logo.clearbit.com/samsungnext.com"},
        {"name": "McKinsey", "url": "https://www.mckinsey.com/", "logo": "https://logo.clearbit.com/mckinsey.com"},
        {"name": "vijil.ai", "url": "https://vijil.ai/", "logo": "https://logo.clearbit.com/vijil.ai"},
        {"name": "OutSystems", "url": "https://www.outsystems.com/", "logo": "https://logo.clearbit.com/outsystems.com"},
        {"name": "Vessl", "url": "https://vessl.ai/", "logo": "https://logo.clearbit.com/vessl.ai"},
        {"name": "Akash", "url": "https://akash.network/", "logo": "https://logo.clearbit.com/akash.network"},
    ],
    "bronze": [
        {"name": "Fastino.ai", "url": "#", "logo": "https://logo.clearbit.com/fastino.ai"},
        {"name": "Linux / PyTorch", "url": "https://pytorch.org/", "logo": "https://logo.clearbit.com/pytorch.org"},
        {"name": "Elastic", "url": "https://www.elastic.co/", "logo": "https://logo.clearbit.com/elastic.co"},
    ],
}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/option-a", response_class=HTMLResponse)
async def option_a(request: Request):
    return templates.TemplateResponse(request=request, name="option_a.html", context={"sponsors": SPONSORS})

@app.get("/option-b", response_class=HTMLResponse)
async def option_b(request: Request):
    return templates.TemplateResponse(request=request, name="option_b.html", context={"sponsors": SPONSORS})

@app.get("/option-c", response_class=HTMLResponse)
async def option_c(request: Request):
    return templates.TemplateResponse(request=request, name="option_c.html", context={"sponsors": SPONSORS})

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

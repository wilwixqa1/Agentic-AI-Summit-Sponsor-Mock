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
        {"name": "Daytona", "url": "https://www.daytona.io/", "logo_dark": "/static/logos/daytona-dark.svg", "logo_light": "/static/logos/daytona-light.svg"},
        {"name": "Lambda", "url": "https://lambda.ai/", "logo_dark": "/static/logos/lambda-dark.png", "logo_light": "/static/logos/lambda-dark.png"},
        {"name": "Ema", "url": "https://www.ema.ai/", "logo_dark": "/static/logos/ema-dark.png", "logo_light": "/static/logos/ema-transparent.png"},
        {"name": "Replit", "url": "https://replit.com/", "logo_dark": "/static/logos/replit-dark.png", "logo_light": "/static/logos/replit-light.png"},
        {"name": "E2B", "url": "https://e2b.dev/", "logo_dark": "/static/logos/e2b-dark.png", "logo_light": "/static/logos/e2b-light.png"},
        {"name": "SAP", "url": "https://www.sap.com/", "logo_dark": "/static/logos/sap-dark.png", "logo_light": "/static/logos/sap-light.png"},
        {"name": "AMD", "url": "https://www.amd.com/", "logo_dark": "/static/logos/amd-dark.png", "logo_light": "/static/logos/amd-dark.png"},
    ],
    "gold": [
        {"name": "Snorkel AI", "url": "https://snorkel.ai/", "logo_dark": "/static/logos/snorkel-dark.png", "logo_light": "/static/logos/snorkel-light.png"},
        {"name": "Nebius", "url": "https://nebius.com/", "logo_dark": "/static/logos/nebius-dark.png", "logo_light": "/static/logos/nebius-light.png"},
        {"name": "Databricks", "url": "https://www.databricks.com/", "logo_dark": "/static/logos/databricks-dark.png", "logo_light": "/static/logos/databricks-light.png"},
    ],
    "silver": [
        {"name": "Samsung NEXT", "url": "https://www.samsungnext.com/", "logo_dark": "/static/logos/samsung-next-dark.png", "logo_light": "/static/logos/samsung-next-light.png"},
        {"name": "McKinsey", "url": "https://www.mckinsey.com/", "logo_dark": "/static/logos/mckinsey-dark.png", "logo_light": "/static/logos/mckinsey-dark.png"},
        {"name": "vijil.ai", "url": "https://vijil.ai/", "logo_dark": "/static/logos/vijil-dark.png", "logo_light": "/static/logos/vijil-dark.png"},
        {"name": "OutSystems", "url": "https://www.outsystems.com/", "logo_dark": "/static/logos/outsystems-dark.svg", "logo_light": "/static/logos/outsystems-light.svg"},
        {"name": "Vessl", "url": "https://vessl.ai/", "logo_dark": "/static/logos/vessl-dark.png", "logo_light": "/static/logos/vessl-light.png"},
        {"name": "Akash", "url": "https://akash.network/", "logo_dark": "/static/logos/akash-dark.png", "logo_light": "/static/logos/akash-light.png"},
    ],
    "bronze": [
        {"name": "Fastino.ai", "url": "#", "logo_dark": "/static/logos/fastino-dark.png", "logo_light": "/static/logos/fastino-light.png"},
        {"name": "Linux / PyTorch", "url": "https://pytorch.org/", "logo_dark": "/static/logos/pytorch-dark.png", "logo_light": "/static/logos/pytorch-dark.png"},
        {"name": "Elastic", "url": "https://www.elastic.co/", "logo_dark": "/static/logos/elastic-dark.png", "logo_light": "/static/logos/elastic-light.png"},
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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

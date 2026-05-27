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
        {"name": "Daytona", "url": "https://www.daytona.io/", "logo": "https://asset.brandfetch.io/idh2aYFtsG/idqJtU4bH1.png"},
        {"name": "Lambda", "url": "https://lambda.ai/", "logo": "https://asset.brandfetch.io/idCxkP0F1L/idExVxJb1E.svg"},
        {"name": "Ema", "url": "https://www.ema.ai/", "logo": "https://asset.brandfetch.io/id2VjIkVnB/idN6PMbfXZ.svg"},
        {"name": "Replit", "url": "https://replit.com/", "logo": "https://asset.brandfetch.io/id1VBvQCJZ/idYGbZzD8i.svg"},
        {"name": "E2B", "url": "https://e2b.dev/", "logo": "https://asset.brandfetch.io/idEVOXjigm/id5aLSdpCi.svg"},
        {"name": "SAP", "url": "https://www.sap.com/", "logo": "https://asset.brandfetch.io/idxyNwHcNp/id-MQtWl9d.svg"},
        {"name": "AMD", "url": "https://www.amd.com/", "logo": "https://asset.brandfetch.io/idTRMciVqn/idD-GbP5bB.svg"},
    ],
    "gold": [
        {"name": "Snorkel AI", "url": "https://snorkel.ai/", "logo": "https://asset.brandfetch.io/id9ixPa1fq/idb2cjLxfZ.png"},
        {"name": "Nebius", "url": "https://nebius.com/", "logo": "https://asset.brandfetch.io/idP1FIKcoL/iddg4P8GiQ.svg"},
        {"name": "Databricks", "url": "https://www.databricks.com/", "logo": "https://asset.brandfetch.io/idSUrLOWbH/idlusPnNFb.svg"},
    ],
    "silver": [
        {"name": "Samsung NEXT", "url": "https://www.samsungnext.com/", "logo": "https://asset.brandfetch.io/idawuE_L2o/idZi3acls5.svg"},
        {"name": "McKinsey", "url": "https://www.mckinsey.com/", "logo": "https://asset.brandfetch.io/idpGZ4e8Mj/idm_yXlvL9.svg"},
        {"name": "vijil.ai", "url": "https://vijil.ai/", "logo": ""},
        {"name": "OutSystems", "url": "https://www.outsystems.com/", "logo": "https://asset.brandfetch.io/idIhOe0VxV/idJYTm9r4Y.svg"},
        {"name": "Vessl", "url": "https://vessl.ai/", "logo": ""},
        {"name": "Akash", "url": "https://akash.network/", "logo": "https://asset.brandfetch.io/id_Yp4LCvT/idJ_jKDjpb.svg"},
    ],
    "bronze": [
        {"name": "Fastino.ai", "url": "#", "logo": ""},
        {"name": "Linux / PyTorch", "url": "https://pytorch.org/", "logo": "https://asset.brandfetch.io/idgMkRm0qR/id0hbgg9C3.svg"},
        {"name": "Elastic", "url": "https://www.elastic.co/", "logo": "https://asset.brandfetch.io/idK2Ey21TY/idK6a7OAHT.svg"},
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

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from .controller import quote_router

app = FastAPI(title="Inspirational Quotes API", version="1.0.0")

app.include_router(quote_router)

static_dir = Path(__file__).parent.parent / "frontend" / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_index():
    static_file = Path(__file__).parent.parent / "frontend" / "index.html"
    if static_file.exists():
        return FileResponse(static_file)
    return {"message": "Welcome to the Inspirational Quotes API", "docs": "/docs"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
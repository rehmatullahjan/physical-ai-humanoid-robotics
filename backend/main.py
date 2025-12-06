from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

genai.configure(api_key=api_key)
gemini_model = genai.GenerativeModel('gemini-2.0-flash')

app = FastAPI(title="Physical AI Backend - Gemini Router", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class QueryRequest(BaseModel):
    query: str
    route: str = "auto"

class RouterResponse(BaseModel):
    response: str
    route: str
    model: str

ROUTES = {
    "content": "You are an expert technical writer. Generate clear educational content.",
    "code": "You are an expert programmer. Generate clean code.",
    "analysis": "You are a researcher. Provide thorough analysis.",
    "summary": "You are a summarizer. Create concise summaries.",
}

@app.get("/")
async def root():
    return {"name": "Physical AI Backend", "version": "1.0.0", "endpoints": {"/api/chat": "POST", "/api/routes": "GET", "/health": "GET"}}

@app.get("/health")
async def health():
    return {"status": "healthy", "model": "gemini-2.0-flash"}

@app.get("/api/routes")
async def get_routes():
    return {"available_routes": list(ROUTES.keys()), "model": "gemini-2.0-flash"}

@app.post("/api/chat", response_model=RouterResponse)
async def chat(req: QueryRequest):
    if req.route == "auto":
        if any(w in req.query.lower() for w in ["code", "python", "function"]):
            route = "code"
        elif any(w in req.query.lower() for w in ["analyze", "compare"]):
            route = "analysis"
        elif any(w in req.query.lower() for w in ["summarize", "brief"]):
            route = "summary"
        else:
            route = "content"
    else:
        route = req.route if req.route in ROUTES else "content"
    
    system_prompt = ROUTES[route]
    full_prompt = f"{system_prompt}\n\n{req.query}"
    
    response = gemini_model.generate_content(full_prompt, generation_config=genai.types.GenerationConfig(max_output_tokens=2048))
    
    return RouterResponse(response=response.text, route=route, model="gemini-2.0-flash")

if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import uvicorn
import os

# Configuration
# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QDRANT_PATH = os.path.join(BASE_DIR, "qdrant_storage")
COLLECTION_NAME = "physical_ai_book"
MODEL_NAME = "all-MiniLM-L6-v2"

app = FastAPI(title="Physical AI RAG API")

# Enable CORS for all origins to allow external access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load resources globally (eager load for faster first request)
print("Loading resources...")
try:
    client = QdrantClient(path=QDRANT_PATH)
    model = SentenceTransformer(MODEL_NAME)
    print("Resources loaded successfully.")
except Exception as e:
    print(f"Error loading resources: {e}")
    client = None
    model = None

class SearchRequest(BaseModel):
    query: str
    limit: int = 5

class SearchResult(BaseModel):
    filename: str
    content: str
    score: float
    title: str = "Unknown"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/search")
def search(request: SearchRequest):
    if not client or not model:
        raise HTTPException(status_code=500, detail="Search engine not initialized")
    
    try:
        vector = model.encode(request.query).tolist()
        
        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=vector,
            limit=request.limit
        )
        
        output = []
        if results and results.points:
            for hit in results.points:
                # Extract clean title from filename or metadata if available
                filename = hit.payload.get('filename', 'Unknown')
                # Try to make a nicer title from the filename
                title = filename.replace('.md', '').replace('-', ' ').title()
                
                output.append(SearchResult(
                    filename=filename,
                    title=title,
                    content=hit.payload.get('content', ''),
                    score=hit.score
                ))
        
        return {"results": output}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Host 0.0.0.0 allows access from other machines on the network
    uvicorn.run(app, host="0.0.0.0", port=8000)

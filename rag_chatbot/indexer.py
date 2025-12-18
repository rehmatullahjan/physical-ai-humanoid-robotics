import os
import glob
import re
import yaml
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer

# Configuration
# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_PATH = os.path.join(BASE_DIR, "../book/docs") # Assuming book is sibling to rag_chatbot
# Normalizing the path
DOCS_PATH = os.path.normpath(DOCS_PATH)
QDRANT_PATH = os.path.join(BASE_DIR, "qdrant_storage")

# QDRANT_HOST = "localhost" # Not used for local path based client
# QDRANT_PORT = 6333
COLLECTION_NAME = "physical_ai_book"
MODEL_NAME = "all-MiniLM-L6-v2"

def get_files():
    return glob.glob(os.path.join(DOCS_PATH, "*.md"))

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split Frontmatter
    parts = re.split(r'^---$', content, flags=re.MULTILINE)
    metadata = {}
    text = content
    
    if len(parts) >= 3:
        try:
            metadata = yaml.safe_load(parts[1])
            text = parts[2]
        except yaml.YAMLError:
            pass
            
    return text.strip(), metadata

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def index_book():
    print("Connecting to local Qdrant (embedded)...")
    # Use local storage path
    client = QdrantClient(path=QDRANT_PATH)
    
    print(f"Loading model {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    print(f"Recreating collection '{COLLECTION_NAME}'...")
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )
    
    files = get_files()
    points = []
    idx = 0
    
    print(f"Indexing {len(files)} files...")
    for file_path in files:
        filename = Path(file_path).name
        text, metadata = parse_markdown(file_path)
        chunks = chunk_text(text)
        
        print(f"  - {filename}: {len(chunks)} chunks")
        
        for chunk in chunks:
            vector = model.encode(chunk).tolist()
            payload = {
                "filename": filename,
                "content": chunk,
                **metadata
            }
            points.append(models.PointStruct(id=idx, vector=vector, payload=payload))
            idx += 1
            
    client.upsert(collection_name=COLLECTION_NAME, points=points)
    print(f"Successfully indexed {len(points)} chunks into '{COLLECTION_NAME}'.")

if __name__ == "__main__":
    index_book()

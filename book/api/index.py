from http.server import BaseHTTPRequestHandler
import json
import os
import google.generativeai as genai
from pathlib import Path

# Initialize Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
else:
    model = None

def get_book_context():
    """Read all markdown docs to build context"""
    context = ""
    # Path relative to api/index.py: we are in book/api, docs are in book/docs
    docs_path = Path(__file__).parent.parent / "docs"
    if docs_path.exists():
        for md_file in docs_path.glob("*.md"):
            try:
                content = md_file.read_text(encoding='utf-8')
                context += f"\n--- DOCUMENT: {md_file.name} ---\n{content}\n"
            except:
                pass
    return context

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            query = data.get('query', '')

            if not model:
                # If no key, try to at least provide a helpful message
                response_data = {"results": [{"title": "System Error", "content": "GEMINI_API_KEY is missing in Vercel Environment Variables.", "score": 0.0}]}
                self.send_response(200) # Send 200 so frontend shows the message
            else:
                try:
                    context = get_book_context()
                    prompt = f"""
                    You are an expert AI Assistant specialized in the "Physical AI: Humanoid Robotics" book.
                    Use the following book content to provide exact, factual answers. 
                    If the answer isn't in the context, say you don't know based on the book.
                    Keep answers concise and well-formatted in markdown.
                    
                    BOOK CONTEXT:
                    {context}
                    
                    USER QUERY: {query}
                    """
                    
                    response = model.generate_content(prompt)
                    
                    response_data = {
                        "results": [
                            {
                                "title": "AI Assistant Response",
                                "content": response.text,
                                "score": 1.0
                            }
                        ]
                    }
                    self.send_response(200)
                except Exception as e:
                    response_data = {"results": [{"title": "API Error", "content": str(e), "score": 0.0}]}
                    self.send_response(200)

            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

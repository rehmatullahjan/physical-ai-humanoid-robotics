#!/usr/bin/env python3
"""
COMPLETE HACKATHON SETUP
Spec-driven book generator + Gemini multi-model router
"""

import os
import json
import yaml
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class HackathonProjectGenerator:
    """Complete end-to-end hackathon project generator"""
    
    def __init__(self):
        api_key = None
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key and Path('.env').exists():
            with open('.env', 'r', encoding='utf-8') as f:
                content = f.read()
                for line in content.split('\n'):
                    line = line.strip()
                    if line.startswith('GEMINI_API_KEY='):
                        api_key = line.replace('GEMINI_API_KEY=', '').strip()
                        break
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        print(f"✅ Gemini initialized (key: {api_key[:10]}...)")
    
    def create_spec_yaml(self):
        """Create spec.yaml"""
        spec = """spec:
  project_name: "physical-ai-humanoid-robotics"
  description: "Complete course on humanoid robotics"

book:
  title: "Physical AI: Humanoid Robotics Course"
  output_dir: "./book"
  chapters:
    - id: intro
      title: "Introduction to Robotics"
    - id: humanoid-basics
      title: "Humanoid Robotics Basics"
    - id: physical-systems
      title: "Physical Systems & Actuators"
    - id: programming-core
      title: "Core Programming for Humanoids"
    - id: robot-ai-integration
      title: "AI Integration & Control"
    - id: movement-dynamics
      title: "Movement & Dynamics"

backend:
  output_dir: "./backend"
  port: 8000

metadata:
  hackathon: "GIAIC Spec-Driven Hackathon 1"
  version: "1.0.0"
"""
        Path('spec.yaml').write_text(spec, encoding='utf-8')
        print("✅ spec.yaml created")
    
    def create_root_env(self):
        """Create root .env file"""
        env = "GEMINI_API_KEY=your-api-key-here\n"
        Path('.env').write_text(env, encoding='utf-8')
        print("✅ .env created")
    
    def generate_docusaurus_book(self):
        """Generate complete Docusaurus book"""
        print("\n📚 Generating Docusaurus book...")
        
        with open('spec.yaml', encoding='utf-8') as f:
            spec = yaml.safe_load(f)
        
        book_dir = Path(spec['book']['output_dir'])
        book_dir.mkdir(exist_ok=True)
        
        (book_dir / 'docs').mkdir(exist_ok=True)
        (book_dir / 'src/css').mkdir(parents=True, exist_ok=True)
        (book_dir / 'src/components').mkdir(parents=True, exist_ok=True)
        (book_dir / 'static').mkdir(exist_ok=True)
        
        chapters = spec['book']['chapters']
        for ch in chapters:
            self._generate_chapter(book_dir, ch)
        
        self._create_docusaurus_config(book_dir, spec)
        self._create_sidebars(book_dir, chapters)
        self._create_package_json(book_dir, spec)
        self._create_custom_css(book_dir)
        
        print(f"✅ Book created at: {book_dir}")
    
    def _generate_chapter(self, book_dir, chapter):
        """Generate single chapter using Gemini"""
        ch_id = chapter['id']
        ch_title = chapter['title']
        
        prompt = f"Write a markdown chapter for: {ch_title}. Include learning objectives, intro, 3-4 sections, code examples, and key takeaways. Use simple ASCII text only."
        
        print(f"  ⏳ Generating: {ch_id}...", end='', flush=True)
        
        resp = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=2000, temperature=0.8)
        )
        
        content = f"---\ntitle: {ch_title}\n---\n\n{resp.text}"
        (book_dir / f'docs/{ch_id}.md').write_text(content, encoding='utf-8')
        print(" ✓")
    
    def _create_docusaurus_config(self, book_dir, spec):
        """Create docusaurus.config.js"""
        config = """module.exports = {
  title: 'Physical AI: Humanoid Robotics',
  tagline: 'Learn humanoid robotics from scratch',
  url: 'https://yourusername.github.io',
  baseUrl: '/physical-ai-humanoid-robotics/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  presets: [
    ['classic', {
      docs: {sidebarPath: require.resolve('./sidebars.js'), routeBasePath: '/'},
      blog: false,
      theme: {customCss: require.resolve('./src/css/custom.css')},
    }],
  ],
  themeConfig: {
    navbar: {
      title: 'Physical AI Robotics',
      logo: {alt: 'Logo', src: 'img/logo.svg'},
      items: [{href: 'http://localhost:8000/docs', label: 'API', position: 'right'}],
    },
    footer: {
      style: 'dark',
      copyright: 'Built for GIAIC Hackathon',
    },
    prism: {theme: require('prism-react-renderer/themes/dracula')},
  },
};
"""
        (book_dir / 'docusaurus.config.js').write_text(config, encoding='utf-8')
    
    def _create_sidebars(self, book_dir, chapters):
        """Create sidebars.js"""
        chapter_ids = ", ".join([f"'{ch['id']}'" for ch in chapters])
        sidebars = f"module.exports = {{'tutorialSidebar': [{chapter_ids}]}};\n"
        (book_dir / 'sidebars.js').write_text(sidebars, encoding='utf-8')
    
    def _create_package_json(self, book_dir, spec):
        """Create package.json for Docusaurus"""
        pkg = {
            "name": spec['spec']['project_name'],
            "version": "1.0.0",
            "private": True,
            "scripts": {
                "start": "docusaurus start",
                "build": "docusaurus build",
                "serve": "docusaurus serve",
            },
            "dependencies": {
                "react": "^18.0.0",
                "react-dom": "^18.0.0",
                "@docusaurus/core": "^3.0.0",
                "@docusaurus/preset-classic": "^3.0.0",
                "clsx": "^1.2.1",
                "prism-react-renderer": "^2.1.0"
            },
            "engines": {"node": ">=18.0"}
        }
        (book_dir / 'package.json').write_text(json.dumps(pkg, indent=2), encoding='utf-8')
    
    def _create_custom_css(self, book_dir):
        """Create custom CSS"""
        css = """html {--ifm-color-primary: #2563eb;--ifm-color-primary-dark: #1d4ed8;}
.navbar {background: linear-gradient(90deg, #1e293b 0%, #334155 100%);}
.markdown h1, .markdown h2, .markdown h3 {color: #1e293b;}
code {background-color: #f1f5f9;padding: 2px 6px;border-radius: 3px;}
"""
        (book_dir / 'src/css/custom.css').write_text(css, encoding='utf-8')
    
    def generate_fastapi_backend(self):
        """Generate FastAPI backend with Gemini router"""
        print("\n🔧 Generating FastAPI backend...")
        
        with open('spec.yaml', encoding='utf-8') as f:
            spec = yaml.safe_load(f)
        
        backend_dir = Path(spec['backend']['output_dir'])
        backend_dir.mkdir(exist_ok=True)
        
        main_py = """from fastapi import FastAPI
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
    full_prompt = f"{system_prompt}\\n\\n{req.query}"
    
    response = gemini_model.generate_content(full_prompt, generation_config=genai.types.GenerationConfig(max_output_tokens=2048))
    
    return RouterResponse(response=response.text, route=route, model="gemini-2.0-flash")

if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
        
        (backend_dir / 'main.py').write_text(main_py, encoding='utf-8')
        (backend_dir / 'requirements.txt').write_text("fastapi==0.104.1\nuvicorn==0.24.0\npydantic==2.5.0\ngoogle-generativeai==0.3.0\npython-dotenv==1.0.0\npyyaml==6.0\n", encoding='utf-8')
        (backend_dir / '.env').write_text("GEMINI_API_KEY=your-api-key-here\n", encoding='utf-8')
        
        print(f"✅ Backend created at: {backend_dir}")
    
    def create_readme(self):
        """Create README"""
        readme = """# Physical AI: Humanoid Robotics Course
GIAIC Spec-Driven Hackathon Project

## Quick Start

### Setup
cd backend
pip install -r requirements.txt

cd book
npm install

### Run

Terminal 1 - Backend:
cd backend
python main.py
Visit: http://localhost:8000/docs

Terminal 2 - Book:
cd book
npm start
Visit: http://localhost:3000

## Project Structure
- book/ - Docusaurus website
- backend/ - FastAPI server
- spec.yaml - Configuration
"""
        Path('README.md').write_text(readme, encoding='utf-8')
        print("✅ README.md created")
    
    def run(self):
        """Run complete setup"""
        print("=" * 60)
        print("HACKATHON PROJECT GENERATOR")
        print("=" * 60)
        
        try:
            self.create_spec_yaml()
            self.create_root_env()
            self.generate_docusaurus_book()
            self.generate_fastapi_backend()
            self.create_readme()
            
            print("\n" + "=" * 60)
            print("PROJECT READY!")
            print("=" * 60)
            print("\nNEXT STEPS:")
            print("1. Edit .env and backend/.env with your API key")
            print("2. cd backend && pip install -r requirements.txt && python main.py")
            print("3. cd book && npm install && npm start")
            print("\nVisit:")
            print("- Book: http://localhost:3000")
            print("- API: http://localhost:8000/docs")
            
        except Exception as e:
            print(f"\nError: {e}")
            raise

if __name__ == "__main__":
    gen = HackathonProjectGenerator()
    gen.run()
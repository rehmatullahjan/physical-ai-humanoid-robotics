# Physical AI: Humanoid Robotics Course & RAG Chatbot

An interactive Docusaurus book integrated with an AI-powered RAG (Retrieval-Augmented Generation) chatbot. This project allows users to read about Humanoid Robotics and ask questions to an AI that answers **strictly** based on the book's content.

## 📁 Project Structure

```
my_book/
├── book/                  # Docusaurus Frontend
│   ├── src/
│   │   ├── components/    # React Components (inc. ChatWidget)
│   │   ├── theme/         # Theme Customizations (Root.js)
│   │   └── ...
│   ├── docusaurus.config.js
│   └── ...
├── rag_chatbot/           # Python Backend & AI
│   ├── api.py             # FastAPI Server
│   ├── indexer.py         # Script to ingest book content into Vector DB
│   ├── requirements.txt   # Python Dependencies
│   └── qdrant_storage/    # Local Vector Database (Qdrant)
├── developer_guide/       # Documentation for Developers
└── run_app.ps1            # Quick Start Script (Windows)
```

## 🚀 Quick Start (Local)

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**

### Option 1: One-Click Run (Windows)
```powershell
.\run_app.ps1
```
This script will:
1. Start the FastAPI Backend on Port `8000`
2. Start the Docusaurus Frontend on Port `3000`

### Option 2: Manual Run

#### 1. Start the Backend (ChatBrain)
Physical AI: Humanoid Robotics Course
GIAIC Spec-Driven Hackathon Project

## 🚀 One-URL Deployment (Vercel)

This project is optimized for a single-url deployment using Vercel. Both the Docusaurus book and the AI assistant are hosted together.

### 🛠️ Setup & Deployment

1.  **Environment Variable**: Add `GEMINI_API_KEY` to your Vercel project settings.
2.  **Root Directory**: Ensure Vercel is set to use the `book` directory as the root.
3.  **Push to GitHub**: Simply push your changes to the `main` branch, and Vercel will handle the rest.

### 📂 Project Structure
- `book/` - Frontend (Docusaurus) + Backend (Vercel API)
- `book/api/` - Serverless AI Assistant (Python)
- `book/docs/` - Book content (Markdown)
- `rag_chatbot/` - (Optional) Legacy local backend/indexer

## 📖 Access the Book
Once deployed, visit your Vercel URL (e.g., `https://physical-ai-humanoid-robotics.vercel.app`) to read the book and chat with the AI!
```bash
cd book
npm install
npm start
```
*The book will open at `http://localhost:3000`*

## 🌐 Deployment & Sharing

### Accessing on Local Network
The backend is configured to listen on `0.0.0.0`, meaning other computers on your Wi-Fi/LAN can access it.
1. Find your computer's IP address (e.g., `ipconfig` -> `192.168.x.x`).
2. Others can view the book at `http://192.168.x.x:3000` (if you expose Node) or you can build the static site.
3. The chatbot will automatically try to connect to the backend relative to the page URL.

### GitHub Pages (Static Hosting)
You can host the **book** on GitHub Pages.
1. Push this code to GitHub.
2. The included GitHub Actions workflow (see `.github/workflows/deploy.yml`) will build and deploy the site.
3. **Note:** For the chatbot to work on the live internet, you must host the Python backend on a cloud server (like Render, Railway, or AWS) and update the API URL in the frontend configuration.

## 🛠 Developer Guide
See the `developer_guide/` folder for more details:
- [API Reference](developer_guide/API_REFERENCE.md)
- [Example Client](developer_guide/example_client.py)

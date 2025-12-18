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
```bash
# Navigate to the chatbot directory
cd rag_chatbot

# Create/Activate Virtual Environment (optional but recommended)
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# (Optional) Re-index the book content if you changed markdown files
python indexer.py

# Run the API Server
python api.py
```
*The server will start at `http://localhost:8000`*

#### 2. Start the Frontend (Book)
Open a new terminal:
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

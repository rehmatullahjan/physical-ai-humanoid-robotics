# Deployment & Networking Guide

This project consists of two parts:
1. **Frontend (Book)**: A static website (HTML/JS/CSS).
2. **Backend (Chatbot)**: A dynamic Python API.

To "make it live" or share it, you have to handle these differently.

## 1. Sharing on Local Wi-Fi (Simplest)
If you want colleagues in the same office/home to see it:

1. **Start the Backend**:
   - Run `python api.py` in `rag_chatbot`.
   - It listens on `0.0.0.0`, so it accepts external connections.
   - Note your IP (e.g., `192.168.1.5`).

2. **Start the Frontend**:
   - Run `npm start --host 0.0.0.0` in `book` folder.
   - Or just build it: `npm run build` and serve the `build` folder using any static server (e.g., `npx serve build`).

3. **Provide Access**:
   Give users the URL: `http://192.168.1.5:3000`.

## 2. Publishing to GitHub Pages (The Book)
You can host the book on GitHub Pages for free.

1. **Push Code**: Push this repo to GitHub.
2. **Settings**: Go to Repo Settings -> Pages -> Source: `GitHub Actions`.
3. **Trigger**: The included `.github/workflows/deploy.yml` will automatically build and deploy the book when you push to `main`.

**Important Limitation**:
The GitHub Pages site is "public internet". It **cannot** talk to `localhost:8000` because "localhost" refers to the *visitor's* computer.
It also cannot talk to `http://192.168.1.5:8000` (your private IP) unless the visitor is on your same WiFi.

## 3. "Real" Live Deployment (Chatbot + Book)
To make the Chatbot work for everyone on the internet:

1. **Deploy Backend**:
   - Use a cloud provider like **Render**, **Railway**, or **AWS**.
   - Upload the `rag_chatbot` folder.
   - Set the Start Command to: `uvicorn api:app --host 0.0.0.0 --port $PORT`.
   - You will get a unique URL (e.g., `https://my-robot-chat.onrender.com`).

2. **Update Frontend**:
   - Open `book/src/components/ChatWidget/index.js`.
   - Change `API_URL` to your new cloud URL:
     ```javascript
     const API_URL = "https://my-robot-chat.onrender.com";
     ```
   - Commit and push. GitHub Pages will update, and now the live book talks to the live backend.

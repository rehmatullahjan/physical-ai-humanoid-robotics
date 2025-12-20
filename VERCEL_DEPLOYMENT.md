# 🚀 Complete Deployment Guide - Vercel + Render.com

## ✅ Prerequisites
- [x] Code pushed to GitHub: `https://github.com/rehmatullahjan/physical-ai-humanoid-robotics`
- [ ] Create Vercel account (https://vercel.com)
- [ ] Create Render.com account (https://render.com)

---

## 📋 Step 1: Deploy Frontend to Vercel (5 minutes)

### 1.1 Connect GitHub to Vercel
1. Go to **https://vercel.com/signup** and click **"Continue with GitHub"**
2. Authorize Vercel to access your repositories
3. Click **"Import Project"** or **"Add New..."** → **"Project"**

### 1.2 Import Your Repository
1. Find `rehmatullahjan/physical-ai-humanoid-robotics` in the list
2. Click **"Import"**
3. **Configure Project:**
   - **Framework Preset**: Other
   - **Root Directory**: Leave blank (`.`)
   - **Build Command**: `cd book && npm install && npm run build`
   - **Output Directory**: `book/build`
   - **Install Command**: `npm install --prefix ./book`

### 1.3 Deploy
1. Click **"Deploy"**
2. Wait 2-3 minutes for the build to complete
3. **🎉 Your frontend URL**: `https://your-project-name.vercel.app`
   - Copy this URL, you'll need it for testing!

---

## 📋 Step 2: Deploy Backend to Render.com (5 minutes)

### 2.1 Create Render Account
1. Go to **https://render.com** and click **"Get Started"**
2. Sign up using **"Sign in with GitHub"**
3. Authorize Render to access your repositories

### 2.2 Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Click **"Connect account"** to link GitHub (if not already)
3. Find and select: `rehmatullahjan/physical-ai-humanoid-robotics`
4. Click **"Connect"**

### 2.3 Configure Service
Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | `physical-ai-backend` (or any name you like) |
| **Region** | Pick closest to you |
| **Branch** | `main` |
| **Root Directory** | Leave blank |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r rag_chatbot/requirements.txt && cd rag_chatbot && python indexer.py` |
| **Start Command** | `cd rag_chatbot && uvicorn api:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` |

### 2.4 Deploy
1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment (it will install dependencies and build the vector database)
3. **🎉 Your backend URL**: `https://physical-ai-backend.onrender.com` (or your chosen name)
   - **IMPORTANT: Copy this exact URL!**

---

## 📋 Step 3: Connect Frontend to Backend (3 minutes)

Now we need to tell the frontend where the backend is.

### 3.1 Update API URL in Code
1. Open: `book/src/components/ChatWidget/index.js`
2. Find **line 27** (it currently says):
   ```javascript
   const API_URL = `http://${typeof window !== 'undefined' ? window.location.hostname : 'localhost'}:8000`;
   ```
3. Replace with your Render backend URL:
   ```javascript
   const API_URL = "https://physical-ai-backend.onrender.com";  // ⚠️ USE YOUR ACTUAL URL
   ```

### 3.2 Commit and Push
```bash
git add book/src/components/ChatWidget/index.js
git commit -m "chore: connect to production backend"
git push origin main
```

### 3.3 Wait for Auto-Deploy
- **Vercel** will automatically detect the push and redeploy (1-2 minutes)
- Check the Vercel dashboard to see deployment progress

---

## 🎉 Step 4: Test Your Live Application!

### 4.1 Open Your Live Book
1. Go to your Vercel URL: `https://yourproject.vercel.app`
2. The book should load perfectly!

### 4.2 Test the Chatbot
1. Click the **chat bubble** (bottom right corner)
2. Try asking: **"What is a humanoid robot?"**
3. The chatbot should respond with exact content from your book!

### 4.3 Verify Backend Health
1. Open: `https://physical-ai-backend.onrender.com/health`
2. You should see: `{"status": "ok"}`

---

## 📱 Sharing Your Project

**Your Live Book URL**: 
```
https://yourproject.vercel.app
```

Share this URL with anyone! They can:
- ✅ Read your Humanoid Robotics book
- ✅ Use the AI chatbot to ask questions
- ✅ Access from any device (phone, tablet, computer)
- ✅ No installation needed!

---

## ⚠️ Important Notes

### Free Tier Limitations
**Render.com Free Tier:**
- Backend "sleeps" after 15 minutes of inactivity
- First request after sleep = 30-60 seconds to wake up (chatbot will show "thinking...")
- Subsequent requests = instant
- **Upgrade to paid ($7/month)** to keep 24/7 awake

**Vercel Free Tier:**
- Unlimited bandwidth
- Always online, no sleep
- Perfect for frontend hosting

### Troubleshooting

**Chatbot doesn't respond?**
1. Check backend is awake: Visit `https://your-backend.onrender.com/health`
2. Wait 60 seconds if it's sleeping (first request wakes it up)
3. Check browser console (F12) for errors
4. Verify you updated the API_URL in ChatWidget correctly

**Build failed on Vercel?**
1. Check the build logs in Vercel dashboard
2. Ensure `book/package.json` has correct dependencies
3. Try redeploying

**Build failed on Render?**
1. Check logs in Render dashboard
2. Ensure `rag_chatbot/requirements.txt` is complete
3. Check that `indexer.py` runs successfully

---

## 🔄 Making Updates Later

### Update Book Content
1. Edit markdown files in `book/docs/`
2. Commit and push to GitHub
3. Vercel auto-redeploys (2 minutes)

### Update Backend Code
1. Edit `rag_chatbot/api.py` or other backend files
2. Commit and push to GitHub
3. Render auto-redeploys (5 minutes)

### Update Book Styling/Components
1. Edit files in `book/src/`
2. Commit and push
3. Vercel auto-redeploys

---

## 📊 Deployment Architecture

```
┌─────────────┐
│   GitHub    │  ← Your Code Repository
└──────┬──────┘
       │
       ├─────────────────┬─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Vercel    │   │ Render.com  │   │   Local     │
│  (Frontend) │   │  (Backend)  │   │ Development │
└─────────────┘   └─────────────┘   └─────────────┘
       │                 │
       │   API Calls     │
       └────────►────────┘
```

---

## 🆘 Need Help?

**Vercel Issues:**
- Dashboard: https://vercel.com/dashboard
- Logs: Click on your project → "Deployments" → Click latest deployment → "Logs"

**Render Issues:**
- Dashboard: https://dashboard.render.com
- Logs: Click on your service → "Logs" tab

**Common Errors:**
- CORS error → Backend CORS is already configured for `*` (all origins)
- 502 Bad Gateway → Backend is sleeping, wait 60 seconds
- Build failed → Check logs for specific error messages

---

## 🎓 What You've Deployed

✅ **Docusaurus Book** (Static Site on Vercel CDN)
✅ **FastAPI Backend** (Python server on Render.com)
✅ **Qdrant Vector Database** (Embedded in backend)
✅ **AI-Powered RAG Chatbot** (Sentence Transformers)
✅ **Fully Functional Web Application**

**Total Cost: $0/month** 🎉

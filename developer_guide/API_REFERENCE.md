# Physical AI Chatbot - API Reference

This project includes a RAG (Retrieval-Augmented Generation) chatbot powered by **FastAPI** and **Qdrant**.
It is designed to be accessible over a local network.

## Base URL

When running locally:
`http://localhost:8000`

When running on a network (accessible to others):
`http://<YOUR_COMPUTER_IP>:8000`

## Endpoints

### 1. Search / Chat
**POST** `/search`

Search the book content for relevant sections.

**Request Body (JSON):**
```json
{
  "query": "What are the sensors used in humanoid robots?",
  "limit": 3
}
```

- `query` (string, required): The question or topic to search for.
- `limit` (int, optional): Number of results to return. Default is 5.

**Response (JSON):**
```json
{
  "results": [
    {
      "filename": "sensors.md",
      "title": "Sensors in Robotics",
      "content": "...text from the book...",
      "score": 0.85
    }
  ]
}
```

### 2. Health Check
**GET** `/health`

Returns `{"status": "ok"}` if the server is running.

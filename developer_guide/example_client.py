import requests
import json

# Configuration
# If running on the same machine:
API_URL = "http://localhost:8000/search"
# If running on a different machine, replace localhost with the IP, e.g.:
# API_URL = "http://192.168.1.5:8000/search"

def ask_chatbot(question):
    print(f"Asking: '{question}'...")
    
    payload = {
        "query": question,
        "limit": 3
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        
        data = response.json()
        results = data.get("results", [])
        
        if not results:
            print("No results found.")
            return

        print(f"\nFound {len(results)} relevant sections:\n")
        for i, res in enumerate(results, 1):
            print(f"--- Result {i}: {res['title']} (Score: {res['score']:.2f}) ---")
            # Print first 200 chars of content
            print(f"{res['content'][:200]}...\n")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Is the backend running?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    ask_chatbot("How do humanoid robots balance?")

import time
import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
# Import the new Google GenAI SDK
from google import genai

app = FastAPI()

# Initialize the Gemini client
# Best practice: Load your key from an environment variable
print("Loading Gemini API key from environment variable...")
#print("##########GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))  # Debugging line to check if the key is loaded
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class AskResponse(BaseModel):
    answer: str
    tokens: int
    latency_ms: float

class AskRequest(BaseModel):
    prompt: str = Field(..., min_length=1)

@app.post("/ask", response_model=AskResponse)
async def ask_gemini(request: AskRequest):
    start_time = time.perf_counter()
    
    # Call the Gemini API
    # gemini-2.0-flash is a fast, popular model choice is shut down.
    # see this https://ai.google.dev/gemini-api/docs/deprecations for details.
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=request.prompt
    )
    
    end_time = time.perf_counter()
    
    latency_ms = (end_time - start_time) * 1000
    
    # Extract data from the Gemini response
    answer = response.text
    # usage_metadata provides token information
    tokens = response.usage_metadata.total_token_count
    
    return AskResponse(
        answer=answer,
        tokens=tokens,
        latency_ms=round(latency_ms, 2)
    )

# To run the app, use: uvicorn FastApi_Gemini_Pydantic:app --reload

# To test, send a POST request to http://localhost:8000/ask with JSON body: {"prompt": "What is the capital of France?"}
# curl.exe -X POST "http://127.0.0.1:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{\"prompt\": \"Who are you?\"}'
# or use browser >>>> http://127.0.0.1:8000/docs#/default/ask_gemini_ask_post
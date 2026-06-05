import time
from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import OpenAI

# Initialize FastAPI and OpenAI client
app = FastAPI()
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# 1. Define the Pydantic response model
class AskResponse(BaseModel):
    answer: str
    tokens: int
    latency_ms: float

# 2. Define the request body model
class AskRequest(BaseModel):
    prompt: str = Field(..., min_length=1)

# 3. Define the POST endpoint
@app.post("/ask", response_model=AskResponse)
async def ask_openai(request: AskRequest):
    start_time = time.perf_counter()
    
    # Call OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": request.prompt}]
    )
    
    end_time = time.perf_counter()
    
    # Calculate metrics
    latency_ms = (end_time - start_time) * 1000
    answer = completion.choices[0].message.content
    tokens = completion.usage.total_tokens
    
    # Return validated Pydantic model
    return AskResponse(
        answer=answer,
        tokens=tokens,
        latency_ms=round(latency_ms, 2)
    )

# Run with: uvicorn filename:app --reload
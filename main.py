from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tweety import generate_sde_tweet, generate_tweet_hashtags, validate_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from tweety"}


@app.get("/generate-tweet")
async def generate_tweet(prompt: str):
    validate_prompt_api(prompt=prompt)
    result = generate_sde_tweet(prompt=prompt)
    tweet = result["answer"]
    return {"tweet": tweet}

@app.get("/generate-hashtags")
async def generate_hashtags(prompt: str):
    validate_prompt_api(prompt=prompt)
    result = generate_tweet_hashtags(prompt=prompt)
    hashtags = result["answer"]
    return {"hashtags": hashtags}

def validate_prompt_api(prompt):
    try:
        if validate_prompt(prompt=prompt) is False:
            raise ValueError("Too long prompt length, keep it to 32 characters or less")
    except ValueError as httperror:
        raise HTTPException(status_code=400, detail=str(httperror))
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
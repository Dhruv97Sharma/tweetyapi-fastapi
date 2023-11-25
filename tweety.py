import requests, os
from dotenv import load_dotenv

load_dotenv()

source_domain = os.environ["API_SOURCE"]
api_key = os.environ["API_KEY"]
url = f"https://{source_domain}/ask"

def validate_prompt(prompt):
    return len(prompt) <= 32

def generate_sde_tweet(prompt):
    if validate_prompt(prompt=prompt):
        query = f"You are an expert software engineer, Generate a highly engaging tweet to start a conversation about {prompt}"
        payload = { "question": query}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": source_domain
        }

        response = requests.post(url, json=payload, headers=headers, verify=False)

        tweet_res_obj = response.json()
        return tweet_res_obj
    else:
        raise ValueError("Invalid length of prompt, make 32 chars or less")
    
def generate_tweet_hashtags(prompt):
    if validate_prompt(prompt=prompt):
        query = f"Generate relevant tweet hashtag keywords on {prompt}"
        payload = { "question": query}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": source_domain
        }

        response = requests.post(url, json=payload, headers=headers, verify=False)

        hashtags = response.json()
        return hashtags
    else:
        raise ValueError("Invalid length of prompt, make 32 chars or less")
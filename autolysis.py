# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
# ]
# ///

import requests
import os
from dotenv import load_dotenv

#api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjEwMDI0NjlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.fi0afXSQetfhBPAgCm1rEeiIoYBlFzQi-t1W4Q12CV0"
api_key = os.environ["AIPROXY_TOKEN"] 
print(api_key)
response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How do I use a proxy with ChatGPT?"},
            ]
        }
    )
result = response.json()
print(result)
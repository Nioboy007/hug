import requests

API_URL = "https://api-inference.huggingface.co/models/succinctly/text2image-prompt-generator"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "a naked girl",
})

print(output)

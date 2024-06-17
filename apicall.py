import json
import requests
import openai
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTM5ZmZhM2EtZGEwYS00ODhkLWI4NmMtMDZiZGJiZGMwYWJkIiwidHlwZSI6ImFwaV90b2tlbiJ9.wGTVOrdTyHeSGiy0tj-rjVKAWkOgvsAdNBog81g-LhQ"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello there tell me a joke...! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "shyam"
}

def first(query):
    payload["text"]=query
    #print(payload)
    response=requests.post(url,json=payload,headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    print(result["openai"]["generated_text"])
first("How are you....")

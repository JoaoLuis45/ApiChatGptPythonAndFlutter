from fastapi import FastAPI
import os
import openai
import dotenv

dotenv.load_dotenv()


openai.organization = "org-sHhTfBhVTYc2lXrKeFyhWhwK"
openai.api_key = "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"

app = FastAPI()

@app.get("/")
def read_root():
    prompt = "conte uma historia"
    response = openai.Completion.create(
    model="text-davinci-003",
    max_tokens=2000,
    prompt=prompt,
    )
    resposta = response.choices[0].text.replace('\n','')
    return {f"resposta": {resposta}}

from fastapi import FastAPI
import os
import openai
import dotenv

dotenv.load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    openai.api_key = "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"
    prompt = "conte uma historia"
    response = openai.Completion.create(
    model="text-davinci-003",
    max_tokens=2000,
    prompt=prompt,
    )
    resposta = response.choices[0].text.replace('\n','')
    return {f"resposta": {resposta}}

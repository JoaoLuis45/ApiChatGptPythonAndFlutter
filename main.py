from fastapi import FastAPI, Form
import os
import openai
import dotenv

dotenv.load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    openai.api_key = os.environ['apiKey']
    prompt = "meu nome é?"
    response = openai.Completion.create(
    model="text-davinci-003",
    max_tokens=2000,
    prompt=prompt,
    )
    resposta = response.choices[0].text.replace('\n','')
    return {f"resposta": {resposta}}

@app.post("/prompt/")
async def post_prompt(pergunta: str = Form()):
    openai.api_key = os.environ['apiKey']
    prompt = pergunta
    response = openai.Completion.create(
    model="text-davinci-003",
    max_tokens=2000,
    prompt=prompt,
    )
    resposta = response.choices[0].text.replace('\n','')
    return {f"resposta": {resposta}}

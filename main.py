import spacy

from fastapi import FastAPI

app = FastAPI()
nlp = spacy.load('ja_ginza')


@app.get('/')
async def index():
    return {'hello': 'world'}


@app.get('/api/annotate')
async def annotate(text: str):
    doc = nlp(text)
    return doc.to_json()

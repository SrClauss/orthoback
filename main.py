from fastapi import FastAPI
from tinydb import TinyDB, Query
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

origins = [
    
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db = TinyDB('db.json')
avaliacao_joelho = db.table('avaliacao-joelho')

@app.post('/avaliacao-joelho')
async def create_avaliacao_joelho(data: dict):
    avaliacao_joelho.insert(data)
    return data


@app.get('/avaliacao-joelho')
async def get_avaliacao_joelho():
    return avaliacao_joelho.all()

@app.get('/avaliacao-joelho/{id}')
async def get_avaliacao_joelho(id: str):
    return avaliacao_joelho.search(Query().id == id)

@app.get('/avaliacao-joelho/{nome}/{data}')
async def get_avaliacao_joelho(nome: str, data: str):
    return avaliacao_joelho.search(Query().nome == nome and Query().data == data)







"""
{
    "pontuacaoLysholm": "20",
    "pontuacaoKujala": "20",
    "torqueExtensorMedioDireito": "25",
    "torqueExtensorMedioEsquerdo": "20",
    "torqueFlexorMedioDireito": "20",
    "torqueFlexorMedioEsquerdo": "20",
    "torqueHipPositionDireito": "12",
    "torqueHipPositionEsquerdo": "30",
    "deficitExtensor": 5,
    "deficitFlexor": 0,
    "deficitHipPosition": 18,
    "nome": "Clausemberg Rodrigues de Oliveira",
    "idade": "40",
    "altura": "25",
    "peso": "30",
    "sexo": "Feminino",
    "lados": [
        "Braço Esquerdo"
    ],
    "membro": "esquerdo",
    "data": "2020-05-20T03:00:00.000Z",
    "hora": "2024-05-27T23:04:00.000Z",
    "queixa": "Qauariasdfjaçlk",
    "hd": "125582",
    "direito": true,
    "esquerdo": false,
    "menorDireito": 4,
    "menorEsquerdo": 6,
    "maiorDireito": 5,
    "maiorEsquerdo": 5,
    "flexaoJoelhoDireito": "20",
    "flexaoJoelhoEsquerdo": "40",
    "extensaoJoelhoDireito": "30",
    "extensaoJoelhoEsquerdo": "40",
    "coxaDireita6cm": 20,
    "coxaEsquerda6cm": 30,
    "coxaDireita15cm": 30,
    "coxaEsquerda15cm": 30,
    "diferencaCoxa6cm": 10,
    "diferencaCoxa15cm": 0,
    "flexores": "20",
    "extensores": "20"
}


"""
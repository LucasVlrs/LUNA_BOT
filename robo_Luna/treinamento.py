from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSAS = [
    "robo_Luna\conversas\capitais.json",
    "robo_Luna\conversas\continentes.json",
    "robo_Luna\conversas\idiomas.json",
    "robo_Luna\conversas\moedas.json",
    "robo_Luna\conversas\populacao.json",
    "robo_Luna\conversas\saudacoes.json"
]


def iniciar():
    robo = ChatBot("Robo Luna")
    treinador = ListTrainer(robo)

    return treinador


def carregar_conversas():
    conversas = []

    for arquivo_conversas in CONVERSAS:
        with open(arquivo_conversas, "r", encoding='utf-8') as arquivo:
            conversas_para_treinamento = json.load(arquivo)
            conversas.append(conversas_para_treinamento["conversas"])

            arquivo.close()

    return conversas


def treinar(treinador, conversas):
    for conversa in conversas:
        for pergunta_resposta in conversa:
            pergunta = pergunta_resposta["pergunta"]
            resposta = pergunta_resposta["resposta"]

            print(f"Treinando >> pergunta: {pergunta}| >>Resposta: {resposta}")
            for mensagem in pergunta:
                treinador.train([mensagem, resposta])


if __name__ == "__main__":
    treinador = iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)

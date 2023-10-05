import unittest
from robo import *


class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def teste_01(self):
        saudacoes = ["oi", "olá"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, sou a robô guia geográfica Luna, o que você deseja saber ?", resposta.text)

    def teste_02(self):
        saudacoes = ["Bom dia"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Bom dia, sou a robô guia geográfica Luna, o que você deseja saber ?", resposta.text)

    def teste_03(self):
        saudacoes = ["Boa tarde"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Boa tarde, sou a robô guia geográfica Luna, o que você deseja saber ?", resposta.text)

    def teste_03(self):
        saudacoes = ["Boa noite"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Boa noite, sou a robô guia geográfica Luna, o que você deseja saber ?", resposta.text)


class TesteFuncoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def teste_01_continente(self):
        saudacoes = ["em que continente está a bolívia?"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A Bolívia está localizada na América do Sul.", resposta.text)

    def teste_02_populacao(self):
        saudacoes = ["qual é a população do uruguai?"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A população do Uruguai é de aproximadamente 3 milhões de pessoas.", resposta.text)

    def teste_03_idioma(self):
        saudacoes = ["qual o idioma falado no paraguai?"]

        for saudacao in saudacoes:
            print(f'z {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O espanhol e o guarani são os idiomas oficiais do Paraguai.", resposta.text)

    def teste_04_capital(self):
        saudacoes = ["qual é a capital da argentina?"]

        for saudacao in saudacoes:
            print(f'Testando: {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A capital da Argentina é Buenos Aires.", resposta.text)

    def teste_05_moeda(self):
        saudacoes = ["qual é a moeda do brasil?",
                     "qual é a moeda oficial do brasil?"]

        for saudacao in saudacoes:
            print(f'Testando: {saudacao}')

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A moeda do Brasil é o real.", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteFuncoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)

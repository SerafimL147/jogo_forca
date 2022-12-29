import random

#criando váriavel de palavras
palavras = ["cachorro", "banana", "melao"]

#selecionando as palavras aleatorias da minha lista
palavras = random.choice(palavras)

#numero de tentativas e chances
tentativas = 0
chanches = 6

#variavel com as letras escolhidas, sem valor
letras_escolhidas = []

#essa variavel vai pegar o tamanho da palavra e multiplicar pelo  '_ '
estado_atual = "_ " * len(palavras)

#Boas vindas
print('*' * 27)
print('Bem vindo ao jogo da forca\nSe divirta e boa sorte!')
print('*' * 27)


import random

#criando váriavel de palavras
palavras = ["cachorro", "banana", "melao"]

#selecionando as palavras aleatorias da minha lista
palavras = random.choice(palavras)

#numero de tentativas e chances
tentativas = 0
chances = 6

#variavel com as letras escolhidas, sem valor
letras_escolhidas = []

#essa variavel vai pegar o tamanho da palavra e multiplicar pelo  '_ '
estado_atual = ["_ "] * len(palavras)

#Boas vindas
print('*' * 27)
print('Bem vindo ao jogo da forca\nSe divirta e boa sorte!')
print('*' * 27)

#Enquanto o número de tentativas for menor do que o de chances
while tentativas < chances:

    letra = input('Digite uma letra: ')
    letras_escolhidas.append(letra)


#se a letra estiver na palavra
    if letra in palavras:
        print('Parabéns! Você acertou a letra.')

#se a letra que eu escolhi estiver na palavra ela vai ser adicionada ao len
        for i in range(len(palavras)):
            if letra == palavras[i]:
                estado_atual[i] = letra

                print(i)


        #estado da palavra
        print(estado_atual)
    else:
        print('Que pena, você errou!')
        tentativas += 1 #Se errou o numero de tentativas vai diminuindo, até chegar 6


        #quantas tentativas
        print(f'Você ainda tem {tentativas} tentativas')


        #estado da palavra
        print(estado_atual)

        #letras escolhidas
        print(letras_escolhidas)

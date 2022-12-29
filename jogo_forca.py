import random
import sys

#criando váriavel de palavras
palavras = ['cachorro', 'banana', 'melao', 'abacaxi', 'pipa', 'manga']


#selecionando as palavras aleatorias da minha lista
palavras = random.choice(palavras).upper()

#numero de tentativas e chances
tentativas = 0
chances = 6

#variavel com as letras escolhidas, sem valor
letras_escolhidas = []

#essa variavel vai pegar o tamanho da palavra e multiplicar pelo  '_ '
estado_atual = ["_"] * len(palavras)


#Boas vindas
print('*' * 27)
print('Bem vindo ao jogo da forca\nSe divirta e boa sorte!')
print('*' * 27)

#Enquanto o número de tentativas for menor do que o de chances e 'and' enquanto eu não acertar a palavra
#se estourar o numero de tentativas o jogo acaba e se descobrir a palavra o jogo acaba
print(f'Vamos começar, sua palavra tem {estado_atual}'  + str(len(estado_atual)), 'letras.')
while tentativas < chances and ''.join(estado_atual) != palavras: #.join vai fazer com que uma lista de letras vire uma palavra

    letra = input('\n\nDigite uma letra: ').upper()

    while letra in letras_escolhidas:
        print('Você já escolheu essa letra')
        letra = str(input('Digite outra letra: ').upper())

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
        print(f'\n\nVocê ainda tem {tentativas}/6 tentativas')


        #estado da palavra
        print(estado_atual)

        #letras escolhidas
        print(letras_escolhidas)

#
if tentativas == chances:
    print(f'\n\nInfelizmente você perdeu! A palavra era {palavras}.')
else:
    print(f'Você acertou a palavra, parabéns! Sua palavra era {palavras}')






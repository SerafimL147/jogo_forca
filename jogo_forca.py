palavra_secreta = 'banana'.upper()

acertos = 0
erros = 0



while acertos != len(palavra_secreta) and erros != 6:
    letra = input('Digite a letra: ').upper()
    if letra in palavra_secreta:
        print('Você acertou a letra')
        acertos += 1
    else:
        print('Errou')
        erros += 1

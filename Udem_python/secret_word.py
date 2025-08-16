word = 'palavra-secreta'
secret_word = '*'*len(word)
tries = 0

while word != secret_word:
    letter = input("Digite uma letra: ")
    tries += 1

    if len(letter) > 1:
        print('Digite apenas uma letra')
        continue

    new_secret_word = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_secret_word += letter
        else:
            new_secret_word += secret_word[i]
    secret_word = new_secret_word

    print(secret_word)

print('PARABENS VOCE GANHOU!!!')
print(f'tentativas: {tries}')
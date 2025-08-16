import random

NUM_BATALHAS = 1000

while True:
    a = list(map(int, input().split()))
    vampLife1, vampLife2, attack, damage = a

    if max(a) == 0 and min(a) == 0:
        break

    vitorias_vamp1 = 0

    for _ in range(NUM_BATALHAS):
        vida1 = vampLife1
        vida2 = vampLife2

        while vida1 > 0 and vida2 > 0:
            dado = random.randint(1, 6)
            if dado <= attack:
                vida1 += damage
                vida2 -= damage
            else:
                vida1 -= damage
                vida2 += damage
            
            if vida2 <= 0:
                vitorias_vamp1 += 1

    probabilidade = (vitorias_vamp1 / NUM_BATALHAS) * 100
    print(f'{probabilidade:.2f}')
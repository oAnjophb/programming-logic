
cases = int(input())

for _ in range(cases):

    dinner = ''
    isCheater = False

    foods = input()    
    breakfast = input()
    lunch = input()

    f = [x for x in foods]
    b = [x for x in breakfast]
    l = [x for x in lunch]

    for char in f:
        if char not in b and char not in l:
            dinner += char

    for char in b + l:
        if char not in f:
            isCheater = True

    if isCheater:
        dinner = 'CHEATER'
    else:
        dinner = sorted(dinner)

    print(''.join(dinner))
import math

while True:
    try:
        D, VF, VG = map(int, input().split())

        tf = 12 / VF
        tg = math.sqrt(144 + D**2) / VG

        if tg <= tf:
            print("S")
        else:
            print("N")
    except EOFError:
        break
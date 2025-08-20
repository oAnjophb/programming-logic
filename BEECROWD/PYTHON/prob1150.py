
def count_consec(x, y, soma=0, cont=0):
    if soma > y:
        return cont
    return count_consec(x + 1, y, soma + x, cont + 1)

x = int(input())
y = int(input())

while y <= x:
    y = int(input())

print(count_consec(x, y))
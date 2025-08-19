x, y = map(int, input().split())

for i in range(1, y+1, x):
    line = range(i, min(i + x, y + 1))
    print(' '.join(map(str, line)))
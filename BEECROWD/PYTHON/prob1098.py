# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# .....
# I=2 J=?
# I=2 J=?
# I=2 J=?

x = 0
while x <= 2:
    for j in range(1, 4):
        print(f'I={round(x,1)} J={round(j + x,1)}')
    x += 0.2
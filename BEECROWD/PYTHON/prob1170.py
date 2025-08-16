for _ in range(int(input())):
    foodWeight = float(input())
    qty_days = 0

    while foodWeight > 1:
        qty_days += 1
        foodWeight /= 2

    print(f'{qty_days} dias')
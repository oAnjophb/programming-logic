
for _ in range(int(input())):
    numbers = input()
    qty_leds = 0

    for i in numbers:
        if i == '1':
            qty_leds += 2
        elif i == '2' or i == '3' or i == '5':
            qty_leds += 5
        elif i == '4':
            qty_leds += 4
        elif i == '7':
            qty_leds += 3
        elif i == '8':
            qty_leds += 7
        else:
            qty_leds += 6
    
    print(f'{qty_leds} leds')
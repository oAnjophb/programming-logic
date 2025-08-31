while True:
    number = input()
    if '0x' in number:
        value = int(number, 16)
    else:
        value = int(value)

    if value < 0:
        break

    if number.startswith('0x'):
        print(value)
    else:
        print(hex(value)) 
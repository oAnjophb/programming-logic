
while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break

    count = 0
    carry = 0
    
    while x > 0 or y > 0:
        digit_x = x % 10
        digit_y = y % 10
        
        if digit_x + digit_y + carry >= 10:
            carry = 1
            count += 1
        else:
            carry = 0
        
        x //= 10
        y //= 10
    
    if count == 0:
        print("No carry operation.")
    else:
        print(f"{count} carry operations.")
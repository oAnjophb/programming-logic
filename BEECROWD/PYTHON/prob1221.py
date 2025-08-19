import math

for _ in range(int(input())):
    entry = int(input())
    is_prime = True
    
    if entry < 2:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(entry)) + 1):
            if entry % i == 0:
                is_prime = False
                break
    
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

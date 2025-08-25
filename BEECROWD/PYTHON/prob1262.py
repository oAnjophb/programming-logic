while True:
    try:
        s = input().strip()
        P = int(input().strip())
        
        ciclos = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == 'R':
                countR = 0
                while i < n and s[i] == 'R':
                    countR += 1
                    i += 1
                ciclos += (countR + P - 1) // P
            else:
                while i < n and s[i] == 'W':
                    ciclos += 1
                    i += 1
        
        print(ciclos)
        
    except EOFError:
        break

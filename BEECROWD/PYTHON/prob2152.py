for _ in range(int(input())):
    H, M, O = map(int, input().split())
    
    hour_format = f"{H:02d}"
    min_format = f"{M:02d}"
    
    if O == 1:
        print(f"{hour_format}:{min_format} - A porta abriu!")
    else:
        print(f"{hour_format}:{min_format} - A porta fechou!")

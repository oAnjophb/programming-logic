while True:
    try:
        qty_slug = int(input())
        velocities = input().split()

        for index in range(0, len(velocities)):
            velocities[index] = int(velocities[index])

        if max(velocities) < 10:
            print(1)
        elif max(velocities) >= 10 and max(velocities) < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break
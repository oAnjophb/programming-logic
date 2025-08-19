def count_digits(n):
    if n < 0:
        return [0]*10
    count = [0]*10
    i = 1
    while i <= n:
        high = n // (i*10)
        cur = (n // i) % 10
        low = n % i

        for d in range(10):
            count[d] += high * i

        for d in range(cur):
            count[d] += i

        count[cur] += low + 1

        count[0] -= i
        i *= 10
    return count

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    res = [count_digits(b)[d] - count_digits(a-1)[d] for d in range(10)]
    print(*res)

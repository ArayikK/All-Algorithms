def optimal_floor(N):  # N - շենքի հարկերի քանակ
    n = 1
    while True:
        if ((n / 2) * (1 + n) >= N):
            return n
        else:
            n += 1

print(optimal_floor(106))

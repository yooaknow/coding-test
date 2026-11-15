T = int(input())

for t in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    b = 0
    c = 0

    for i in range(N - 1, -1, -1):
        if a[i] > b:
            b = a[i]
        else:
            c += b - a[i]

    print(f"#{t} {c}")
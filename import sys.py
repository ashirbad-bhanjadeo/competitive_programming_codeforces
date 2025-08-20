import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # Build prefix sum of rainy days
    rain_prefix = [0] * (n + 1)
    for i in range(n):
        rain_prefix[i+1] = rain_prefix[i] + a[i]

    count = 0
    i = 0
    while i + k <= n:
        # Check if window [i, i+k-1] has all zeros
        if rain_prefix[i+k] - rain_prefix[i] == 0:
            count += 1
            i += k + 1   # hike days + 1 rest
        else:
            i += 1
    print(count)
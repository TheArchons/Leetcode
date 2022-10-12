def rotateLeft(d: int, arr: list) -> list:
    return arr[d:] + arr[:d]

# read input
n, d = map(int, input().split())
arr = list(map(int, input().split()))

print(*rotateLeft(d, arr))
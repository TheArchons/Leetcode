def arrayManipulation(n: int, queries: list) -> int:
    arr = [0] * (n + 1)

    for i in queries:
        arr[i[0] - 1] += i[2]
        arr[i[1]] -= i[2]
    
    max = 0
    sum = 0

    for i in arr:
        sum += i
        if sum > max:
            max = sum
    
    return max
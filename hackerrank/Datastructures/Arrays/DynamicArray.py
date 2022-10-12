def dynamicArray(n: int, queries: list) -> list:
    arr = []
    for i in range(n):
        arr.append([])

    lastAnswer = 0
    answers = []

    for query in queries:
        idx = (query[1] ^ lastAnswer) % n
        if query[0] == 1:
            arr[idx].append(query[2])
        else:
            lastAnswer = arr[idx][query[2] % len(arr[idx])]
            answers.append(lastAnswer)
    
    return answers


n, q = [int(x) for x in input().split()]
queries = []
for i in range(q):
    queries.append([int(x) for x in input().split()])

print(dynamicArray(n, queries))
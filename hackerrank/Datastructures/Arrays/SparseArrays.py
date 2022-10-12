def matchingStrings(stringList: list, queries: list) -> list:
    counts = {}
    for i in stringList:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for index, i in enumerate(queries):
        if i in counts:
            queries[index] = counts[i]
        else:
            queries[index] = 0

    return queries
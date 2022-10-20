def checkInclusion(s1: str, s2: str):
    if (len(s1) > len(s2)):
        return False
    c1Counts = {}
    #count s1 and add to c1Counts
    for c in s1:
        if c in c1Counts:
            c1Counts[c] += 1
        else:
            c1Counts[c] = 1
    curr = max = 0
    c1Clones = c1Counts.copy()
    for c in s2:
        if c in c1Counts and c1Counts[c] > 0:
            curr += 1
            if curr > max:
                max = curr
            c1Counts[c] -= 1
        else:
            curr = 0
            c1Counts = c1Clones.copy()
    for i in range(len(s1)):
        if s2[i] in c1Counts and c1Counts[s2[i]] > 0:
            curr += 1
            if curr > max:
                max = curr
            c1Counts[s2[i]] -= 1
        else:
            curr = 0
            c1Counts = c1Clones.copy()
    return (max == len(s1))



s1 = input()
s2 = input()
print(checkInclusion(s1, s2))
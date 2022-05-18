def check(numList):
    if sorted(set(numList)) == numList:
        return "increasing"
    if sorted(set(numList), reverse=True) == numList:
        return "decreasing"
    return "neither"


print(check([1, 2, 3]))

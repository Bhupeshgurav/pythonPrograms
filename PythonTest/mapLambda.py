result = list(map(lambda a, b: a**b, [1, 2, 3, 4, 5], [2, 6, 5, 4, 7]))
print(result)


"""
lst1 = [-1,-2,1,2,-5,5,-6,-66,1,2,3,10]
o/p
result = [1,2,1,2,5,5,6,66,1,2,3,10]
"""

lst1 = [-1, -2, 1, 2, -5, 5, -6, -66, 1, 2, 3, 10]
result = list(map(lambda x: int((x**2)**0.5), lst1))
print(result)

lst1 = [-1, -2, 1, 2, -5, 5, -6, -66, 1, 2, 3, 10]


# sol2
result = list(map(abs, lst1))
print(result)

# q3

country = ["mumbai", "pune", "delhi", "goa", "nashik"]
# output  [['m', 'u', 'm', 'b', 'a', 'i'], ['p', 'u', 'n', 'e'], ['d',
# 'e', 'l', 'h', 'i'], ['g', 'o', 'a'], ['n', 'a', 's', 'h', 'i', 'k']]


def inner(a):
    b = []
    for i in a:
        b.append(i)
    return b


result = list(map(inner, country))
print(result)

# ages = [10,15,41]
# age>18

result = list(filter(lambda x: True if x > 18 else False, ages))
print(result)

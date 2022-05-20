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

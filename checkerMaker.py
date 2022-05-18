def checker(my_list):
    length = len(my_list)
    h1 = my_list[:length//2]
    h2 = my_list[length//2:]
    sum1 = sum(h1)
    sum2 = sum(h2)
    if sum1 > sum2:
        return h1+h2
    if sum1 < sum2:
        return h2+h2
    else:
        return h1+h2


# as half value is same as other half it outputs the same array
print(checker([0, 5, 5, 6, 3, 1]))

def divisible_by_left(n):
    temp = n

    while(n):
        k = n % 10

        if(temp % k == 0):
            return "True"

        n /= 10

    return "False"


print(divisible_by_left(73312))

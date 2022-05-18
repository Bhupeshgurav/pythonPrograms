from re import S


def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)


n = 12345
print(getSum(n))


a = "Python"
b = "is"
c = "easy"

print(a+b+c)


def my_function(list):
    print("The youngest child is "+list[2])


list = ['bhu', 'ter', 'aff']
my_function(list)

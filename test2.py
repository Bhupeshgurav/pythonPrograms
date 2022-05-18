count = 0
while (count < 9):
    count = count + 1
    print("The count is:", count)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('current fruit:', fruit)

print("Good bye!")

i = 0
while(i < 10):
    i = i+1
    print(i)


for x in range(1, 4):
    for y in range(1, 3):
        print("Hello World")


# else in loop

for x in range(5):
    print(x)
else:
    print("Else block in loop")
print("Out of loop")

# break keyword

num = 0
while(num < 5):
    num = num+1
    print(num)
    if num == 3:
        break
print("Out of loop")

# continue keyword

for num in range(1, 6):
    if num == 3:
        continue
    print(num)
print("Out of loop")


# pass keyword

for num in range(1, 6):
    if num == 3:
        pass
    else:
        print(num)

# tuples
myTuple = ("apple", "banana")
print(myTuple)

print(f"tuple values are: {myTuple}")


# write mean of three umbers

num1 = 3
num2 = 4
num3 = 5
mean = (num1+num2+num3)/3
print(f"The mean of the three numbers are{mean}")

# input 4 digit number and print sum of its digit

number = 1234
sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)

print(sum_of_digits)

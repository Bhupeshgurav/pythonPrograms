from tkinter import E


inches = 20


feet = int(inches / 12)

remainder = inches % 12
print(feet, remainder)

# school program
a = 75
b = 75
c = 75
d = 75
e = 75

marks = a+b+c+d + e
percentage = (marks/500)*100
print(marks)
print(percentage)
if(marks >= 75):
    print("1st class")
elif(marks >= 60 & marks < 75):
    print("2nd class")
elif(marks >= 50 & marks < 60):
    print("3rd class")
else:
    print("Fail")

#
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = []
for i in list1:
    x = int(input())
    list2.append(x)
marks = sum(list2)
per = (marks/500)*100
if per >= 75:
    print("pass")
elif 75 > per > 60:
    print('2nd class')
elif 60 > per > 50:
    print("3rd class")
else:
    print("1st class")

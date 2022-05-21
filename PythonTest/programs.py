#Q1:- {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

# we will use map function
# magic replace

from re import S


class Magic:
    def replace_str(self, original, find, rep):
        original.replace(find, rep)

    def str_length(self, string):
        return len(string)

    def trim(self, string):
        return " ".join(string.split())

    def list_slice(lst, tple):
        if len(lst) == 0:
            return -1
        else:
            return lst[tple[0]-1:tple[1]]


print()

'''
Q2:- student_data  = 
 [('Alberto Franco','15/05/2002','35kg'), 
 ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), 
 ('Eesha Hinton','25/09/1998', '35kg')]

'''


def names(a):
    return a[0]


def dob(b):
    return b[1]


def weight(c):
    return c[2][:-2]


student_data = [('Alberto Franco', '15/05/2002', '35kg'),
                ('Gino Mcneill', '17/05/2002',
                 '37kg'), ('Ryan Parkes', '16/02/1999', '39kg'),
                ('Eesha Hinton', '25/09/1998', '35kg')]

stu_name = list(map(names, student_data))
print(stu_name)

stu_dob = list(map(dob, student_data))
print(stu_dob)
stu_weight = list(map(weight, student_data))
print(stu_weight)

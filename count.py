# class User:
#     count_numb = 0

#     def __init__(self, name):
#         self.name = name
#         User.count_numb += 1
#         self.my_count = User.count_numb


# u1 = User("A")
# u2 = User("B")
# u3 = User("C")

# print(u2.user_count())


class demo:
    def __init__(self, f_name):
        self.f_name = f_name
        print("Good morning")

    def show(self):
        print("Good morning", self.f_name)


ob1 = demo("Harry")  # constructor is always called when a obj is created
ob1.show()

class student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_age(self, age):
        return self.__age

    def validate_age(self):
        return self.__age > 20

    def validate_marks(self):
        return 0 >= self.__marks <= 100

    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks >= 65

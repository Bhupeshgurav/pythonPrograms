class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__experience = None
        self.__avg_feedback = None
        self.__technology_skill = None

    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def get_instructor_name(self):
        return self.__instructor_name

    def set_experience(self, experience):
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def set_technology_skill(self, technology):
        self.__technology_skill = technology

    def get_technology_skill(self):
        return self.__technology_skill

    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        else:
            return False

    def allocate_course(self, technology):
        if((technology == self.__technology_skill) or (technology == "C++")):
            return True
        else:
            return False

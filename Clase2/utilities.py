import numpy as np


class Student():
    def __init__(self,name,last_name,major):
        self.name= name
        self.last_name= last_name
        self.major= major
        self.grades= []


    def add_grade(self,grade):
        self.grades.append(grade)
        print("A grade of {} was added to de student {} {}".format(grade,self.name,self.last_name))


    def get_average(self):
        return np.mean(self.grades)


    rod = Student("Rodrigo","Beceiro","IQ")
    print(rod.major)
    print(rod.grades)
    rod.add_grades (95)
    print (rod.grades)

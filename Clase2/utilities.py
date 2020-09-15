class Student():
    def _init_(self,name,last_name,major):
        self.name= name
        self.last_name= last_name
        self.major= major
        self.grades= []
    def add_grades(self,grades):
        self.grades.append(grade)
        print("A grade of {} was added to de student {} {}".format(grade,self.name,self.last_name))
rod= Student("Rodrigo","Aviles","IQ")
print(rod.major)
print(rod.grades)
rod add_grades (95)
print (rod.grades)

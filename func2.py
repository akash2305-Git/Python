class Student:
    def __init__(self,n='.',m=0):
        self.name = n
        self.marks = m

        def display(self):
            print('hi',self.name)
            print('your name',self.marks)

s = Student()
s.display()
print('')

s1 = Student('Ak',880)
s1.display()

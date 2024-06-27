class Student:
    def __init__(self, name):
        self.name = name
        self.H = 0
        self.M = 0
        self.F = 0
        self.grade = ''

    def get_sum(self):
        return(self.H+self.M+self.F)

    def get_grade(self):
        sum = self.get_sum()
        if (sum < 50):
            self.grade = 'F'
        elif ((sum >= 50))and(sum < 60):
            self.grade = 'D'
        elif ((sum >= 60))and(sum < 70):
            self.grade = 'C'
        elif ((sum >= 70))and(sum < 80):
            self.grade = 'B'
        else:
            self.grade = 'A'
        return self.grade
    
    def __str__(self):
        return(str(self.name)+ " has a score of = "+ str(self.get_sum()) + " Therefore he gets ")

st1 = Student("Tee")
st1.H = 18
st1.M = 37
st1.F = 30

st2 = Student("Pui")
st2.H = 15
st2.M = 34
st2.F = 25

print(st1)
print(st1.get_grade())
print(st2)
print(st2.get_grade())

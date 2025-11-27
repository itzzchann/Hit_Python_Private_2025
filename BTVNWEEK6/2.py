class Person:
    def __init__(self,name,yob):
        self.name=name
        self.yob=yob
    def describe(self):
        return f"Name:{self.name}-YoB:{self.yob}"
class Student(Person):
    def __init__(self, name, yob,grade):
        super().__init__(name, yob)
        self.grade=grade
    def describe(self):
        print(f"Student-{super().describe()}-Grade:{self.grade}") 
class Teacher(Person):
    def __init__(self, name, yob,subject):
        super().__init__(name, yob)
        self.subject=subject
    def describe(self):
        print(f"Teacher-{super().describe()}-Subject:{self.subject}") 
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor-{super().describe()} - Specialist: {self.specialist}")
class Ward:
    def __init__(self,name):
        self.name=name
        self.people=[]
    def addPerson(self,person):
        self.people.append(person)
    def describe(self):
        print(f"Ward name:{self.name}")
        for person in self.people:
            person.describe()
    def countDoctor(self):
        count=0
        for person in self.people:
            if(isinstance(person,Doctor)):
                count+=1
        return count
    def sortAge(self):
        self.people.sort(key=lambda x:x.yob,reverse=True)
    def aveTeacher(self):
        count_teacher=0
        tmp=0
        for person in self.people:
            if(isinstance(person,Teacher)):
                tmp+=person.yob
                count_teacher+=1
        if count_teacher==0:
            return 0
        return tmp / count_teacher

ward1=Ward("Anh Tu")
ward1.addPerson(Student("Dang Phuong Anh", 2006, "12"))
ward1.addPerson(Teacher("Nguyen Van An", 1998, "Math"))
ward1.addPerson(Teacher("Tran Phung Anh", 1996, "Literature"))
ward1.addPerson(Doctor("Le Thanh Long", 1991, "Surgery"))
ward1.addPerson(Doctor("Hoang Thi Giang", 1994, "Internal medicine"))
ward1.describe()
print(f"The number of doctor in {ward1.name} is {ward1.countDoctor()}")
ward1.sortAge()
ward1.describe()
print(f"\nAverage teacher yob: {ward1.aveTeacher()}")
    
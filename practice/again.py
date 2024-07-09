class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def info(self):
        if self.age > 21:
            print("ok", self.age)
        else:
            print(f"ok,{self.age}")

    def set_age(self,age):
        self.age = age

stud = Student(name="joel",age=12,sex="Male")
stud.set_age(22)
stud.info()



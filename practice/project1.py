

 remark = "With highest honor"
 age = 18
 gwa = 1.20

 stud =f"age is {age} with a gwa of \"wag kayo maniniwala dyan\" {gwa} \nand a remark of {remark}"
 print(stud)
 


 print("I will \"assert dominance\" \nmaster \npython")

# LIST
 cars = ["chevrolet", "Dodge", "Mustang", "Ram", "corvette","Corvette"]


# ## TUPLE
 engine = ("v8", "v6", "v6", "v6", "v8")

 cars[3:] = ["Toyota","Mazda","Mitsubishi"]
 cars[-4:-5] = ["Nissan","Honda"]
 cars.insert(-7, "Isuzu")

 print(cars[0])
 print(cars[-5])
 cars.insert(3, "Ford")
 print(cars)

speed = [s.upper() for s in cars
          if "z" in s]

 numbers = {1,2,3,4,5,6,7,8,9,10}
 numero = {15,14,13,12}

 print(numbers.isdisjoint(numero))

 while e < len(engine):
     print(engine[e] + " Engine")
     e = e + 1

 for e in engine:
     print(e)

 stud1 = {
     "student1" :  {
         "name" : "Jared Manansala",
         "age" : "21",
         " year" : "2003"
     },
     "student2" : {
        "name" : "Trisha Brondial",
         "age" : ""
     },
     "student3" : {
         "name" : "Albert Blanca",
         "age" : "222"
     }
 }


 Teacher = {
     "Name": "Inspector Singh",
     "Age": "46",
     "Occupation": "Professor"
     }
 Student = {
         "Name": "Pravaniv Phavagrem",
         "Age": 23,
         "Occupation": "Spider-man"
         }

 car = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
 }

 car.setdefault("manufacturer", "Ford Maxmillian")
 car.setdefault("Color", "Silver Bullet ")


 students = [
     ["BSIT",["Jared","Trisha","Jayjay","Cyrel","AC","Aloysius","Lyan","David","Ben","Arkie"]],
     ["BSCS",["Jomar","Milan","Ralph","Jolein","Dennis","Franklin","Lidia","Carl"]]]

 for s in students:
     print(s[0])
     for st in s[1]:
         print("-" + st)
     print()


 courses = {
     "course" : ["BSIT","BSCS","BSCMS"],

 }

 courses["year"] = ["2001","2003","2002"]
 print(courses.get("year"))

 def myshit(**parts):
     price = 800
     print(parts["gpu"] ,f"cost {price} dollars in the US")

 myshit(gpu = "RTX 4090",GPU = "GT 730")

 def argumento(x):
     print(x)

 argumento("behind you" )


 age = int(input("Enter age : "))

 while age < 18:
     print("young " + str(age))
     age = age + 1
     age = int(input("Enter age : "))
 else:
     print("access granted " + str(age))


 username = ["Jared","Trisha","Jayjay"]
 password = ["Amogas","UWU123","Dante"]


 user = input("Enter username : ")
 passy = input("Enter password : ")

 for a in range(len(username)):
     if user == username[a] and passy == password[a]:
         print("Welcome ", username[a])
         break
 else:
     print("Account does not exist")

 def add(num1,num2):
     print(num1 * num2)

 add(5,2)

 KWARGS// KEYWORD ARGUMENTS
 def legalage(**age):
     print(f"you are", age["age"] , "years old")

 (legalage(age =18))

 def square(num1= 212,num2= 51):
     print(num1 * num2)

 square()

 def add(num1, num2):
     return num1, num2

 num = int(input("Enter number : "))
 Num = int(input("Enter number : "))
 add(num, Num)
 print(num + Num)

 def sayhello(**names):
     print("EMPLOYEE")
     print(names["emp_id"])
     print(names["emp_name"])
     print(names["emp_age"])
     print(names["emp_sex"])

 sayhello(emp_sex="Male", emp_id="1", emp_name="jared", emp_age=21)


 def sayhi(*names):
     print("Good morning my name is " + names[0])

 sayhi("Jared","Trisha","Jay-jay")


 previous_num = 0

 for i in range(1,11):
     sum = previous_num + i
     print("current ",i, "prev",previous_num, "sum", sum)
     previous_num = i


 class Showname:
     def __init__(self,name):
         self.name = name


 class Showinfo(Showname):
     def __init__(self,name, age):
         super().__init__(name)
         self.age = age

     @staticmethod
     def info():
         print(SH.name, SH.age)


 S = Showname("Jared")
 SH = Showinfo("Trisha","21")
 Showinfo.info()


 for k in range(10, 0, - 1):
     for L in range(k):
         print('ඞ', end=" ")
     print('')

 fruits = ["banana","apple","cherry","grapes","mangosteen"]

 (yellow, red, maroon, *purple) = fruits
 print(yellow)
 print(red)
 print(maroon)
 print(purple)

if __name__ == '__main__':

    try:
        a = int(input("num: "))
        b = int(input("num: "))
        sum = a + b
        sub = a - b
        prod = a * b
        if sum:
            print(sum)
        if sub:
            print(sub)
        if prod:
            print(prod)
    except ValueError:
        print("error")






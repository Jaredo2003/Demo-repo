# #
# # previous_num = 0
# # #
# for i in range(1,11):
#     sum = previous_num + i
#     print("current number ",i , "+ ", previous_num, "sum = ", sum)
#     previous_num = i

# def multiply_sum(num1, num2):
#     product = num1 * num2
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2
#
# total = multiply_sum(69, 30)
# print("total is " + str(total))
#
# total = multiply_sum(20, 10)
# print("total is " + str(total))
# # #
# #
#
# number = [1,2,3,4,5,6,7,8,9]
# n = 0
#
# while n < len(number):
#     if(number[n] % 2 == 0):
#         print("even number : " + str(number[n]))
#     else:
#         print("odd number : " + str(number[n]))
#     n = n + 1

# for i in range(2,101,2):
#     print(i, end=" ")
#     if i == 20:
#         break

# i = 0
# while i < 6:
#   i = i + 1
#   if i == 5:
#     continue
#   print(i)
#
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i = i + 1

# names = ["Jimmy","Rose","Max","Nina","Phillip"]
#
# def name_length(names):
#     for name in names:
#         print(name)
#         if name == "Max":
#             break
#
#
# name_length(names)
#
# count = 0
# while count < 10:
#     count = count + 1
#     if count == 5:
#         break
#     print(count)
#
# cars = ["mazda","toyota","mitsubishi","honda"]
#
# for c in cars:
#     print(c)
#     if c == "toyota":
#         break

# With default value/keyword arguments
# def say_greeting_with_default(**info):
#     print("Hello" + info["emp"])
#
# say_greeting_with_default(emp="Jared", id=1)

# def say_greeting_only_args(hello,hi,/,*,name,surname):
#     print(hello + name)
#
# say_greeting_only_args("Hello","hi",name="Jared",surname="Manansala")

#
# sum = lambda x,y: x + y
# subtract = lambda x,y: x - y
# multiply = lambda x,y: x * y
# division = lambda x,y: x / y
#
#
# a = int(input("Input 1st number: "))
# operator = input("Choose an operator: ")
# b = int(input("Input 2nd number: "))
#
# if operator == "+":
#     print("The answer is:", end=" ")
#     print(sum(a, b))
# elif operator == "-":
#     print("The answer is:", end=" ")
#     print(subtract(a, b))
# elif operator == "*":
#     print("The answer is:", end=" ")
#     print(multiply(a, b))
# elif operator == "/":
#     print("The answer is:",end=" ")
#     print(division(a, b))
# else:
#     print("Invalid Operator!")

# def myfunc(n):
#     return lambda a: a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))


# class Add:
#     def __init__(self, name):
#         self.name = name
#
#     def get_my_name(self, var):
#         return self
#
#     def set_name(self, name):
#         self.name = name
#
#
# a = Add("Timothy")
# a.set_name("Lori")
# print(a.name)
#

# class Traveler:
#     def __init__(self, player, atk, hp):
#         self.player = player
#         self.atk = atk
#         self.hp = hp
#
#     def show(self):
#         print(f"player: {self.player}")
#         print(f"attack: {self.atk}")
#         print(f"health: {self.hp}")
#
#
# adv = Traveler("Swordmaster", 20, 100)
#
# class Products:
#     def __init__(self, product, prod_id: int, prod_name, price: int, quantity):
#         self.product = product
#         self.prod_id = prod_id
#         self.prod_name = prod_name
#         self.price = price
#         self.quantity = quantity
#         assert price >= 0, "price cant be less than zero"
#
#     def discount(self):
#         if self.price >= 12000:
#             print("with discount + free msi jacket\n")
#         else:
#             print("No discount\n")
#
#
# class Arrival(Products):
#     def __init__(self, product, prod_id, prod_name, price, quantity, name, date, mop, address):
#         super().__init__(product, prod_id, prod_name, price, quantity)
#         self.name = name
#         self.date = date
#         self.mop = mop
#         self.address = address
#
#     def get_add(self):
#         print(self.price)
#
#     def total(self, prc):
#         self.price = prc
#
#     def set_addr(self, addr):
#         self.address = addr
#
#     def get_addr(self):
#         print(self.address)
#
#
# # Derived Class/ Child
# a = Arrival("PSU", 2001, "MSI MAG", 2899, 30, "Jared", "June 14", "Cash on delivery", "bulacan")
# a.set_addr("blk 57 lot 13")
# a.get_addr()
#
# # Parent Class
# item = Products("Graphics Card", 1001, "RX 6600", 12151, 13)
# item1 = Products("Graphics Card", 1002, "GTX 1650 Ti", 11999, 10)
# item3 = Products("RAM", 1003, "Battle Axe 16GB", 15022, 40)
#
# print(item3.price)
# item3.discount()

# class Dad:
#     def __init__(self,name,lname,money):
#         self.name = name
#         self.lname = lname
#         self.money = money
#
#     def inheritance(self):
#         return self.money
#
#
# class Son1(Dad):
#     def __init__(self,name, lname, money):
#         super().__init__(name, lname, money)
#
#     def hello(self):
#         print(f"{self.name}{self.lname}")
#
#     @staticmethod
#     def inherits():
#         return d.money // 3
#
#     def check_savings(self):
#         svngs = d.money
#         if svngs -=
#
#
# class Son2(Dad):
#     def __init__(self,name,lname,money):
#         super().__init__(name,lname,money)
#
#
# # Parent Class
# d = Dad("Jared","Manansala",155212)
# d.inheritance()
# print("-Father-")
# print(d.name, d.lname)
# print("savings: ", d.money,"\n")
#
# # Derived Class
# s = Son1("Natasha ","Manansala", 4214)
# print("-Daughter-")
# s.hello()
# print("savings: ", s.money)
# print("inherits:", s.inherits())

#
# class Parent:
#     def __init__(self, savings):
#         self.savings = savings
#
#     def distribute_inheritance(self):
#         return self.savings // 3
#
#
# class Child1(Parent):
#     def __init__(self, savings):
#         super().__init__(savings)
#         self.inheritance = self.distribute_inheritance()
#
#
# class Child2(Parent):
#     def __init__(self, savings):
#         super().__init__(savings)
#         self.inheritance = self.distribute_inheritance()
#
#
# class Child3(Parent):
#     def __init__(self, savings):
#         super().__init__(savings)
#         self.inheritance = self.distribute_inheritance()
#
#
# class Child4(Parent):
#     def __init__(self, savings):
#         super().__init__(savings)
#         self.inheritance = self.distribute_inheritance()
#
#
# # Example usage:
# total_saving = 1042951
# parent = Parent(total_saving)
# child1 = Child1(total_saving)
# child2 = Child2(total_saving)
# child3 = Child3(total_saving)
# child4 = Child4(total_saving)
#
# print("Parent's savings:", parent.savings)
# print("Child 1's inheritance:", child1.inheritance)
# print("Child 2's inheritance:", child2.inheritance)
# print("Child 3's inheritance:", child3.inheritance)
# print("Child 4's inheritance:", child4.inheritance)
#


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         print(x)
#
# my_class = MyNumbers()
# my_iter = iter(my_class)
#
# next(my_iter)
# next(my_iter)
#
# #
class Friends:
    def __init__(self, firstname, lastname, likescount, friendname):
        self.firstname = firstname
        self.lastname = lastname
        self.likescount = likescount
        self.friendsName = friendname

    def introduce(self):
        print(f"Hi i am {self.firstname} {self.lastname}")

    def full_profile(self):
        print(f"Full name: {self.firstname} {self.lastname}"f""
              f" \nLikes: {self.likescount}\nFriends")
        for ff in f.friendsName:
            print('-', ff)


class Crush(Friends):
    def __init__(self,firstname,lastname,likescount,gender,friendname,):
        super().__init__(firstname,lastname,likescount,friendname)
        self.gender = gender

    def full_profile(self):
        for fc in c.friendsName:
            if "J" in fc:
                print(f"Sus\n-{f.firstname}")
                print(f"Bayots")
            elif "Cyrel" <= fc:
                print(f"-{fc}")


f = Friends("Jared","Manansala ",33,["Jayjay Luciano","Cyrel Villanueva",
"Trisha Brondial(gf)","David Marquez","Kurt Venus","etc..."])
c = Crush("Trisha","Brondial",42,'F',["Jared Manansala","Cyrel","David","beN"])
f.full_profile()
c.full_profile()
#


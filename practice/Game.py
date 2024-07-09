print("Welcome to my game ! ")
score = 0


choose = input("Do you want to play? : ")
if choose.casefold() != "yes":
    print("ok sure i dont need your bitch ass taking my quiz")
    quit()
else:
    print("Sure lets play")

# START OF QUIZ #
answer = int(input("What is 5 x 5? "))
if answer == 25:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer = int(input("What is 10 x 5? "))
if answer == 50:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer = str(input("Is python interpreted or compiled? "))
if answer.casefold() == "interpreted":
    print("Correct")
    score += 1
else:
    print("Incorrect")

if score == 3:
    print("YOU GOT A PERFECT SCORE " + str(score))
elif score == 2:
    print("GOOD JOB " + str(score))
elif score == 1:
    print("Try harder " + str(score))
else:
    print("You got " + str(score), "points")





print("Choose operation")
print("1 : Addition")
print("2 : Subtraction")
print("3 : Product")
print("4 : Division")


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def product(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 // num2

ops = [1,2,3,4]

select = int(input("Select operation : "))

if select in ops:
    numone = int(input("First number : "))
    numtwo = int(input("Second number : "))

if select == 1:
    print(f"{numone} + {numtwo} =", addition(numone, numtwo))
elif select == 2:
    if subtraction(numone, numtwo) < 0:
        print("value cannot be negative")
    else:
        print(f"{numone} - {numtwo} =", subtraction(numone, numtwo))
elif select == 3:
    print(f"{numone} * {numtwo} =", product(numone, numtwo))
elif select == 4:
    print(f"{numone} // {numtwo} =", division(numone, numtwo))
else:
    print("Choose one in the 4 operations")



class Register:
    def __init__(self, name: str, course: str, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print("Name: ", self.name)
        print("Course: ", self.course)
        print("Year: ", self.year)
        print("Section: ", self.section)

registered = []

while True:
    names = input("Enter name: ")
    courses = input("Enter course: ")
    years = input("Enter years: ")
    sections = input("Enter sections : ")
    print()
    r = Register(names, courses, years, sections)
    registered.append(r)
    press = input("Register again [Y/N]? ")
    if press.casefold() == 'y':
        pass
    else:
        break

i = 1
print("Registered students")
for r in registered:
    print("Student #", i)
    r.introduce()
    i += 1
    print()

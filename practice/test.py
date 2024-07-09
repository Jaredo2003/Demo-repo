# tries = 3
# guesses = [1,2,3,4,5,6,7,8,9,10]
# try:
#     while tries > 0:
#         guess = int(input("guess an even number: "))
#         if guess in guesses and guess % 2 == 1:
#             print("You guessed an even number! Nice")
#             break
#         elif guess not in guesses:
#             print("number exceeded")
#         else:
#             print("Thats not an even number")
#         tries = tries - 1
# except ValueError:
#     print("Thats not a number")

# i = 0
# while i < 6:
#     i += 1
#     if i == 2:
#         continue
#     print(i)


# for i in range(1,6):
#     if i == 5:
#         break
#     print(i)
#
# for i in range(1,7):
#     if i == 6:
#         continue
#     print(i)


# print("Magpapasok ba si colegio?")
#
# while True:
#     sagot = input("OO o hinde? : ")
#     if sagot == "OO":
#         print("Tama")
#         break
#     else:
#         print("Hinde")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = 0
#
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print("even : " + str(numbers[i]))
#     else:
#         print("odd : " + str(numbers[i]))
#     i += 1


# lives = 3
# correct_answer = "Smoke"
# while lives > 0:
#     sagot = input("Anong type si omen ? : ")
#     if sagot == correct_answer:
#         print("Tama")
#         break
#     else:
#         lives = lives - 1
# else:
#     print("tanga")

# numbers = 50
#
# while numbers < 100:
#     print(numbers)
#     numbers = numbers + 1

#
# age = int(input("Enter age : "))
# age = int(input("Enter age : "))

# age = 0
#
# while age < 18:
#     print(str(age) + " is Access denied")
#     age = age + 1
# else:
#     print(str(age) + " Access granted")


# def cars():
#     car = {
#         "car": "corvette",
#         "brand": "chevrolet",
#         "year": "2006"
#     }
#     for c in car.items():
#         print(c)
#
# cars()
#
# cars = ["Geely","Mao zedong","Chevrolet","Mazda","Toyota","Ford","Suzuki","Adolf Kitler"]
# leaders = [l.upper() for l in cars if "z" in l]
#
# print(leaders)

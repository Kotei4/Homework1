print("Hello New File")

git commit -m "08.09.23"
git add .
git push


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = None

# if first <= second:
#     gcd = first
# else:
#     gcd = second
# print(gcd)
    
# # while True: #gcd != 0:
#     # if ((first % gcd == 0.0) and (second % gcd == 0.0)):
#     #     print(gcd)
#     #     gcd = gcd - 1


# a=3750
# b=575000000

# for i in range(1, b):
#     if ((a%i)==0) and ((b%i)==0):
#         print(i)
#         #pass

# import math

# print(math.gcd(375, 575))

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# if first < second:
#     gcd = first
# else:
#     gcd = second

# while gcd != 0:
#     if (first % gcd == 0) and (second % gcd == 0):
#         gcd -= 1
#         break

# num = int(input("Введіть число (0 для виходу): "))

# while num != 0:
#     repeat = int(input("Скільки разів помножити число на 2? "))
#     for i in range(repeat):
#         num = num * 2
#     print(num)
#     num = int(input("Введіть число (0 для виходу): "))

    #repeat = int(input("Скільки разів помножити число на 2? "))
    #for i in range(num + 1):

#Завдання номер 10 здається

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     for i in range(num + 1):
#         sum = sum + i
#         print(sum)
#     num = int(input("Enter integer (0 for output): "))


#Завдання №13 правильне 

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        is_upper = ch.isupper()
        ch = ch.lower()
        pos = ord(ch) - ord('a')
        new_pos = (pos + offset) % 26
        new_ch = chr(new_pos + ord('a'))
        if is_upper:
            new_ch = new_ch.upper()
        encoded_message += new_ch
    else:
        encoded_message += ch
print(encoded_message)

#Завдання №13 моє вирішення поки що неправильне
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         char = ord(ch)
#         ch_char = char - ord("a")
#         ch_char = (ch_char + offset) % 26 
#         new_char = (ch_char + ord("a"))
#         encoded_message += chr(new_char)
#     else:
#         encoded_message += ch
# print(encoded_message)
    

# print("Hello World")
# a = input()
# print(a)

# name = input("Як тебе звати ? ")
# print(f"Привіт, {name}, як справи")

# age = input("Hello how old are you? ")
# if int(age) >= 18:
    # print("You already hahe a passport")
# else:
    # print("You is so young for passport")
    
# a = input("print a number: ")
# a = int(a)
# if a < 0:
#     print ("The number is less than Zero")
# elif a == 0:
#     print("The Number is Zero")
# else:
#     print("The Number is more than Zero")

# a = input ('How many Money do you have? ')
# a = int(a)
# # money = 0
# if a:
#     print(f"You have {a} on your bank account")
# else:
#     print("You have no money and no debts")


a = 2 ** (3+1) 
print(a)


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = None

# if first <= second:
#     gcd = first
# else:
#     gcd = second
# print(gcd)
    
# # while True: #gcd != 0:
#     # if ((first % gcd == 0.0) and (second % gcd == 0.0)):
#     #     print(gcd)
a#     #     gcd = gcd - 1


# a=3750
# b=575000000

# for i in range(1, b):
#     if ((a%i)==0) and ((b%i)==0):
#         print(i)
#         #pass

# import math

# print(math.gcd(375, 575))

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# if first < second:
#     gcd = first
# else:
#     gcd = second

# while gcd != 0:
#     if (first % gcd == 0) and (second % gcd == 0):
#         gcd -= 1
#         break

# num = int(input("Введіть число (0 для виходу): "))

# while num != 0:
#     repeat = int(input("Скільки разів помножити число на 2? "))
#     for i in range(repeat):
#         num = num * 2
#     print(num)
#     num = int(input("Введіть число (0 для виходу): "))

    #repeat = int(input("Скільки разів помножити число на 2? "))
    #for i in range(num + 1):

#Завдання номер 10 здається

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     for i in range(num + 1):
#         sum = sum + i
#         print(sum)
#     num = int(input("Enter integer (0 for output): "))


#Завдання №13 правильне 

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        is_upper = ch.isupper()
        ch = ch.lower()
        pos = ord(ch) - ord('a')
        new_pos = (pos + offset) % 26
        new_ch = chr(new_pos + ord('a'))
        if is_upper:
            new_ch = new_ch.upper()
        encoded_message += new_ch
    else:
        encoded_message += ch
print(encoded_message)

#Завдання №13 моє вирішення поки що неправильне
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         char = ord(ch)
#         ch_char = char - ord("a")
#         ch_char = (ch_char + offset) % 26 
#         new_char = (ch_char + ord("a"))
#         encoded_message += chr(new_char)
#     else:
#         encoded_message += ch
# print(encoded_message)
    
print("Hello New File")

print("Hello New Changes")
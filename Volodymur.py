#!!3
# while True:
#     number = int(input('Enter a number: '))
#     if number < 10:
#         continue
#     elif number > 100:
#         break
#     else:
#         print(number)


#!!4#1
# sum = 0
# number = 0
# while True:
#     number = int(input('Enter a number: '))
#     if number != 0:
#         sum = sum + number
#     else:
#         print(sum)
#         break

#!!4#2
# sum = 0
# number = 0
# while True:
#     number = int(input('Enter a number: '))
#     if number != 0:
#         sum = sum + number
#     else:
#         print(sum)
#         break

#!!5
#min_value = a if a < b else b
# a = int(input('Biology team: '))
# b = int(input('IT team: '))
# d=1
# while True:
#     if d%a == 0 and d%b == 0:
#         break
#     else:
#         d += 1
# print(d)

#6
# a = int(input('Enter number first number:'))
# b = int(input('Enter number last number:'))
# my_list = [number for number in range(a, b+1)]
# print(my_list)
# my_new_list = [element for element in my_list if element % 3 == 0]
# print(my_new_list)
#print(my_list)

# for element in my_list:
    # if element % 3 == 0:
#         result = [x for x in my_list if x % 3 == 0]
#     else:
#         continue
# print(new_element)

# if a < b:
#     my_list = [a,b]
# else:
#     my_list = [b,a]
# print(type(my_list))
# for i in my_list:
#     print(i)

'''Task 1: Print Numbers
Write a Python program that uses a for loop to print the numbers from 1 to 10.

for i in range(1, 11):
    print(i)
'''

'''Task 2: Calculate Sum
Write a Python program that uses a for loop to calculate the sum of 
all even numbers from 1 to 20.
#result = i for i in range(1,21) if i % 2 ==0 else: continue
# summa=0
# for i in range(1, 21):
#     if i % 2 == 0:
#         summa += i
#     else:
#         continue
# print(summa)

another variant

summa = 0
for i in range(2,21,2):
    summa += i
print(summa)
'''

'''
Task 3: Count Characters
Write a Python program that counts the number of occurrences of a specific character in a given string using a for loop.
string='programming'
count = 0
for i in string:
    if i == 'g':
        count += 1
print(count)
'''
'''
Task 4: Print a Pattern
Write a Python program that uses a for loop to print the following pattern:

markdown
Copy code
*
**
***
****
*****

Task 6: Find Prime Numbers
Write a Python program that finds and prints all prime numbers between 1 and 50 using a for loop.

Task 7: Nested Loop
Write a Python program that uses nested for loops to print a multiplication table for numbers from 1 to 10.

Task 8: Reverse a String
Write a Python program that reverses a given string using a for loop.

Task 9: Calculate Factorial
Write a Python program that calculates the factorial of a given number using a for loop.

Task 10: Iterate Over Dictionary
Write a Python program that iterates over a dictionary and prints both keys and values using a for loop.

Feel free to try these tasks and let me know if you need any help or solutions for any specific task.
'''

'''
Task 4.1 
string = '*****'
rows = ''
for i in string:
    rows += i
    print(rows)
    
Task 4.2
for i in range(1,6):
    print('*'*i)    
'''

'''
Task 5: List Sum
Write a Python program that calculates the sum of all the elements in a list using a for loop.
'''
# summma = 0
# count =0
# a = int(input('Type thee first number: '))
# b = int(input('Type thee second number: '))
#
# for x in range(a,b+1):
#     if x % 3 == 0:
#         count += 1
#         summma += x
# result = summma/count
# print(f'Summa vsih numbers that divided by 3: {summma}')
# print(f' Serednye Aryfmety4ne:{result}')
# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in my_list:
#         count += 1
#         summma += i


"""first = 958
second = 354

if first < second:
    gcd = first
elif second < first:
    gcd = second

while (first % gcd) or (second % gcd):
    gcd -= 1
print(gcd)
"""
'''a="125"
new_string =    'the first string'\
                'the second string'\
                'and even the third string'
print((new_string))
new_string_2 =    'the first string'                'the second string'               'and even the third string'
print((new_string_2))'''

a = 'hello world'
result = 0
operand = None
operator = None
wait_for_number = True
have_first_number = False

while True:
    char = input(">>>")

    if char == "=":
        print(f"Result: {result}")
        break

    elif wait_for_number:













    # elif wait_for_number:
    #     try:
    #         operand = int(char)
    #         print(operand)
    #         print(result)
    #         wait_for_number = False
    #         if have_first_number == False:
    #             result = operand
    #             have_first_number = True
    #     except ValueError:
    #         print(f"{input} is not a number")
    #         continue
    # else:
    #     if char not in ("+", "-", "/", "*"):
    #         print(f"{char} i not + - / *")
    #         continue
    #     operator =char
    #     wait_for_number = True
    #     if operator == "+":
    #         result += operand
    #     elif operator == "-":
    #         result -= operand
    #     elif operator == "*":
    #         result *= operand
    #     elif operator == "/":
    #         if operand == 0:
    #             print("Division by zero is not allowed.")
    #             continue
    #         result /= operand
            
        







    # elif char in ("+", "-", "/", "*"):
    #     operator = ""
    #     operator = char
    #     print(operator)
    #     # break
    #     operand += operator
    #     print(operand)

    # elif char in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):

    #     digit = float(char)
    #     print(digit)
    #     operand += digit
    #     print(operand)
    #     # break


    


    # if operator in ("+", "-","*", "/"):

    #     operand = wwod
    #     operand = float(operand)

    # elif type(wait_for_number) == int or type(wait_for_number) == float:

    #     operator = wait_for_number

    #     print(operator)
    #     print(type(operator))
    
    # else:
    #     break
    
        # if operand == "+":
        #     result += result
        
        # elif operand == "-":
        #     result -= result

        # elif operand == "*":
        #     result *= result

        # elif operand == "/":
        #     result /= result

        # print(result)
    



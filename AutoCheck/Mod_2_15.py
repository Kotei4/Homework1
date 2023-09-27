result = None
operand = None
operator = None
wait_for_number = True

while True:
    char = input(">>>")

    if char == "=":

        print(f"Result: {result}")
        break

    elif wait_for_number:
        
        try:
            operand = int(char)
            if result == None:
                result = operand

        except ValueError:
            print(f"Type a number please")
        wait_for_number = False
        #result = operand
        continue

    elif wait_for_number == False:

        if char in ("-", "+", "/", "*"):
            operator = char
            wait_for_number = True
            
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "/":
                result /= operand
            elif operator == "*":
                result *= operand
            continue
    #print(f"{operand} {operator}")
print(result)

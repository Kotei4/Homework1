result = None
wait_for_number = True
operand = None
operator = None

while True:
    char = input(">>> ")

    if char == "=":
        print(f"Result: {result}")
        break

    if wait_for_number:

        try:
            operand = float(char)
            wait_for_number = False

        except ValueError:
            print(f'{char} is not a number. Try again')
            continue

        if result == None:
            result = operand

        else:
            if operator == '+':
                result += operand
            if operator == '-':
                result -= operand
            if operator == '/':
                result /= operand
            if operator == '*':
                result *= operand
            
        #print(f'Now result = {result}')

    else:

        if char in (f'{operand} is not \'+\' or \'-\' or \'/\' or \'*\'. Try again'):
            operator = char
            
        else:
            operator = None

        if operator is None:
            print(f'{char} Must be \'+\', \'-\', \'/\', \'*\'')
            
        else:
            wait_for_number = True
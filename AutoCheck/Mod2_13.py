message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for i in message:
    
    if ord(i) > 96 and ord(i) < 123:
        pos = (ord(i) - 97)
        pos = (pos + offset) % 26
        new_char = chr(pos + 97)
        encoded_message += new_char
        
    elif ord(i) > 64 and ord(i) < 91:
        pos = (ord(i) - 64)
        pos = (pos + offset) % 26
        new_char = chr(pos + 64)
        encoded_message += new_char
    elif ord(i) == 32:
        new_char = chr(32)
        encoded_message += new_char
        
    elif ord(i) == 33:
        new_char = chr(33)
        encoded_message += new_char
print(encoded_message)
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Encode and decode (combined function)
def ceaser(process, og_text, shift_num):
    output_lst = []

    for letter in og_text:        
        # If the message contains symbols or numbers then print it as it is
        if letter not in alphabets:
            output_lst.append(letter)

        indx = alphabets.index(letter)
        
        if process == "encode":
            num = shift_num + indx
            #For index out of range
            while num >= 26:
                num -= 26
        elif process == "decode":
            # % 26 is for index out of range
            num = (indx - shift_num) % 26
        else:
            print("Type either 'encrypt' or 'decrypt': ")
            break


        output_lst.append(alphabets[num])

    print(f"The {process}d message: {"".join(output_lst)}")


go_again = True
while go_again:
    # User input
    process = input("Encode or Decode: ").lower()
    msg = input("Message: ").lower()
    shift = int(input("Shift Number: "))

    # Main function and working
    ceaser(process, msg, shift)

    # Restart again the program again?
    print("Do you want to restart?")
    yes_or_no = input("Yes or No: ").lower()
    if yes_or_no == "no":
        go_again = False
        break

print("Come back again!")

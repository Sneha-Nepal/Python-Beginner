alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

process = input("Encode or Decode: ").lower()
msg = input("Message: ").lower()
shift = int(input("Shift Number: "))

def encrypt(og_text, shift_num):
    lst = []
    for letter in og_text:
        indx = alphabets.index(letter)
        num = shift_num + indx
        while num >= 26:
            num -= 26

        lst.append(alphabets[num])
    
    print("".join(lst))

def decrypt():
    pass

if process == "encode" or process == "e":
    encrypt(msg, shift)
elif process == "decode" or process == "d":
    decrypt()
else:
    print("Type either 'encrypt' or 'decrypt'. Also, either 'e' or 'd': ")

def cipher(str):
    word = input("Enter a word to " + str + " : ")
    shift = int(input("Enter the shift number: "))
    cipherText = ""

    for letter in word:
        position = chars.index(letter)
        if (str == "encrypt"):
            position += shift
        else:
            position -= shift

        cipherText += chars[position]
    print("The "+str+"ed"+" text is:\n" + cipherText)

chars = list("abcdefghijklmnopqrstuvwxyz")

encDec = input("Press 'e' to encrypt and 'd' to decrypt: ")

if ("en" in encDec.lower()):
    cipher("encrypt")

else:
    cipher("decrypt")
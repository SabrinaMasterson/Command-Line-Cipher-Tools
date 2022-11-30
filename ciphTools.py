#Sabrina Masterson
import base64

#Cesar Cipher:
#Code comes from a GeeksforGeeks Tutorial:
#https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
def encryptCaesar(text, s):
    result=""

    if (str(s).isdigit() == False):
        result = "Please input a number for shift"
        return result
    #Move through text
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((ord(char) + s-97) % 26 +97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma
    return result

def decryptCaesar(text, s):
    s = 26-s
    result=""
    if (str(s).isdigit() == False):
        result = "Please input a number for shift"
        return result
    #Move through text
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((ord(char) + s-97) % 26 +97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma

    return result


#Affine Cipher:
#code comes from GeeksforGeeks Tutorial:
#https://www.geeksforgeeks.org/implementation-affine-cipher/
def encryptAffine(text, a, b):
    result=""
    if (str(a).isdigit() == False or str(b).isdigit() == False):
        result = "Please input a number for shift or multiplier"
        return result
    elif (is_coprime(int(a), 26) == False):
        result = "Please input a coprime of 26 for multiplier"
        return result

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((a*ord(char) +b-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((a*ord(char) +b-97) % 26 + 97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma
    return result

def decryptAffine(text, a, b):
    result=""
    if (str(a).isdigit() == False or str(b).isdigit() == False):
        result = "Please input a number for shift or multiplier"
        return result
    elif (is_coprime(int(a), 26) == False):
        result = "Please input a coprime of 26 for multiplier"
        return result

    b = 26-b
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((a*ord(char) +b-65) % 26 + 65)
        #for uppercase
        elif (char.islower()):
            result += chr((a*ord(char) +b-97) % 26 + 97)
        #upper and lowercase letters have different ASCII numbers
        else:
            result += char
        #else, it's likely just a character like a period or comma
    return result

#check for coprime
#From w3resource, because the GeeksforGeeks explanation,
#of seeking an inverse modular made no sense
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


#atbash cipher
#has to use a lookup array, but theirs only has uppercase letters
#no key is needed, simple to implement, but I kept the names/systems from other ciphers
#https://www.geeksforgeeks.org/implementing-atbash-cipher/

def encryptAtbash(text):
    lookup_table_upper= {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
    lookup_table_lower= {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'}
    result=""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += lookup_table_upper[char]
        elif (char.islower()):
            result += lookup_table_lower[char]
        else:
            result += char
    return result

def decryptAtbash(text):
    lookup_table_upper = {'Z' : 'A', 'Y' : 'B', 'X' : 'C', 'W' : 'D', 'V' : 'E',
        'U' : 'F', 'T' : 'G', 'S' : 'H', 'R' : 'I', 'Q' : 'J',
        'P' : 'K', 'O' : 'L', 'N' : 'M', 'M' : 'N', 'L' : 'O',
        'K' : 'P', 'J' : 'Q', 'I' : 'R', 'H' : 'S', 'G' : 'T',
        'F' : 'U', 'E' : 'V', 'D' : 'W', 'C' : 'X', 'B' : 'Y', 'A' : 'Z'}
    lookup_table_lower = {'z' : 'a', 'y' : 'b', 'x' : 'c', 'w' : 'd', 'v' : 'e',
        'u' : 'f', 't' : 'g', 's' : 'h', 'r' : 'i', 'q' : 'j',
        'p' : 'k', 'o' : 'l', 'n' : 'm', 'm' : 'n', 'l' : 'o',
        'k' : 'p', 'j' : 'q', 'i' : 'r', 'h' : 's', 'g' : 't',
        'f' : 'u', 'e' : 'v', 'd' : 'w', 'c' : 'x', 'b' : 'y', 'a' : 'z'}
    result=""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += lookup_table_upper[char]
        elif (char.islower()):
            result += lookup_table_lower[char]
        else:
            result += char
    return result

#While I still got this from GeeksforGeeks,
#This can all be done with the base64 library, so that's nice
#here's the GeeksforGeeks and the Python3 documentation for it
#https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
#https://docs.python.org/3/library/base64.html
def encryptBase64(text, type):
    result = ""
    result_bytes = ""
    if (type.isdigit() == False):
        result = "Please input a number for type"
        return result
    elif (type != '64' or type != '32' or type != '16'):
        result = "Type can only be '64', '32', or '16' "
        return result

    result_bytes = text.encode('ascii')
    if (type == 64):
        result = base64.b64encode(result_bytes)
    elif (type == 32):
        result = base64.b32encode(result_bytes)
    elif (type == 16):
        result = base64.b16encode(result_bytes)
    else:
        print("Error in type choice, number must be either 64, 32, or 16")
    result = result.decode('ascii')
    return result

def decryptBase64(text, type):
    result = ""
    result_bytes = ""
    if (type.isdigit() == False):
        result = "Please input a number for type"
        return result
    elif (type != '64' or type != '32' or type != '16'):
        result = "Type can only be '64', '32', or '16' "
        return result

    result_bytes = text.encode('ascii')
    if (type == 64):
        result_bytes = base64.b64decode(result_bytes)
    elif (type == 32):
        result_bytes = base64.b32decode(result_bytes)
    elif (type == 16):
        result_bytes = base64.b16decode(result_bytes)
    else:
        print("Error in type choice, number must be either 64, 32, or 16")
    result = result_bytes.decode('ascii')
    return result

#The baconian cipher is very similar to the atbash cipher in encryption
#https://www.geeksforgeeks.org/baconian-cipher/
def encryptBaconian(text):
    lookup_upper = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
    lookup_lower = {'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
          'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
          'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
          'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
          'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa', 'z': 'bbaab'}
    result=""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += lookup_upper[char]
        elif (char.islower()):
            result += lookup_lower[char]
        else:
            result += char
    return result

def decryptBaconian(text):
    lookup_lower = {'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
          'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
          'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
          'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
          'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa', 'z': 'bbaab'}
    result=""
    i = 0
    while True:
        if (i < len(text)-4):
            substr = text[i:i + 5]
            if (substr[0] != ' '):
                result += list(lookup_lower.keys()
                                 )[list(lookup_lower.values()).index(substr)]
                i += 5
            else :
                result += ' '
                i += 1
        else :
            break
    return result

def combine_ciphs(text, eord, ciph1, ciph2, shift, mult, type):
    res_one = ""
    res_two = ""
    res_error = "An error occurred"
    if (eord == "Encrypt" or eord == "encrypt" or eord == "e"):
        if (ciph1 == "Caesar" or ciph1 == "caesar" or ciph1 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return res_error
            else:
                res_one = encryptCaesar(text, int(shift))
        elif (ciph1 == "Affine" or ciph1 == "affine" or ciph1 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return res_error
            else:
                res_one = encryptAffine(text, int(mult), int(shift))
        elif (ciph1 == "Base64" or ciph1 == "base64" or ciph1 == "base"):
            return res_error
        elif (ciph1 == "Baconian" or ciph1 == "baconian" or ciph1 == "bacon"):
            res_one = encryptBaconian(text)
        elif (ciph1 == "Atbash" or ciph1 == "atbash" or ciph1 == "at"):
            res_one = encryptAtbash(text)
        else:
            return res_error

        if (ciph2 == "Caesar" or ciph2 == "caesar" or ciph2 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return res_error
            else:
                res_two = encryptCaesar(res_one, int(shift))
        elif (ciph2 == "Affine" or ciph2 == "affine" or ciph2 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return res_error
            else:
                res_two = encryptAffine(res_one, int(mult), int(shift))
        elif (ciph2 == "Base64" or ciph2 == "base64" or ciph2 == "base"):
            if (type == '64' or type == '32' or type == '16'):
                res_two = encryptBase64(res_one, int(type))
            else:
                return res_error
        elif (ciph2 == "Baconian" or ciph2 == "baconian" or ciph2 == "bacon"):
            res_two = encryptBaconian(res_one)
        elif (ciph2 == "Atbash" or ciph2 == "atbash" or ciph2 == "at"):
            res_two = encryptAtbash(res_one)
        else:
            return res_error
        return res_two
        #end of encrypt

    elif (eord == "Decrypt" or eord == "decrypt" or eord == "d"):
        if (ciph1 == "Caesar" or ciph1 == "caesar" or ciph1 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return res_error
            else:
                res_one = decryptCaesar(text, int(shift))
        elif (ciph1 == "Affine" or ciph1 == "affine" or ciph1 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return res_error
            else:
                res_one = decryptAffine(text, int(mult), int(shift))
        elif (ciph1 == "Base64" or ciph1 == "base64" or ciph1 == "base"):
            if (type == '64' or type == '32' or type == '16'):
                res_one = decryptBase64(text, int(type))
            else:
                return res_error
        elif (ciph1 == "Baconian" or ciph1 == "baconian" or ciph1 == "bacon"):
            res_one = decryptBaconian(text)
        elif (ciph1 == "Atbash" or ciph1 == "atbash" or ciph1 == "at"):
            res_one = decryptAtbash(text)
        else:
            return res_error

        if (ciph2 == "Caesar" or ciph2 == "caesar" or ciph2 == "c"):
            if (shift == 0 or shift.isdigit() == False):
                return res_error
            else:
                res_two = decryptCaesar(res_one, int(shift))
        elif (ciph2 == "Affine" or ciph2 == "affine" or ciph2 == "af"):
            if (shift == 0 or mult == 0 or shift.isdigit() == False or mult.isdigit() == False or is_coprime(int(mult), 26) == False):
                return res_error
            else:
                res_two = decryptAffine(res_one, int(mult), int(shift))
        elif (ciph2 == "Base64" or ciph2 == "base64" or ciph2 == "base"):
            return res_error
        elif (ciph2 == "Baconian" or ciph2 == "baconian" or ciph2 == "bacon"):
            res_two = decryptBaconian(res_one)
        elif (ciph2 == "Atbash" or ciph2 == "atbash" or ciph2 == "at"):
            res_two = decryptAtbash(res_one)
        else:
            return res_error
        return res_two
        #end of decrypt
    else:
        return res_error
    #end of combine_ciphs

def main():
    done = False
    print("Welcome to Sabrina's Cipher Tools!\n "
     + "This is a test program for my capstone project. Eventually added to my website. \n"
     + "But for testing and demos, here's a command-line version. \n"
     + "You can type 'quit' or 'q' to end the program, or 'n' to leave a cipher loop. \n"
     + "You can also combine two ciphers together, like Atbash and Base64 or Caesar and Baconian. \n"
     + "As a note, the loop might reset if you input incorrect numbers in shift or base keys. ")
     #intro

     #main loop BEGIN
    while done == False:
        print("Current ciphers available: Caesar, Affine, Atbash, Base64, and Baconian. \n"
        + "You can use uppercase or lowercase calls, as well as 'c', 'af', 'at', 'base' and 'bacon' for shorthand "
        + "(the the order of the above list). \n"
        + "You can also combine with the 'Combine' or 'combine' calls. Make sure you don't use Base64 as the first cipher when encoding. \n"
        + "What cipher would you like to use? ")
        type = input("Cipher: ")
        #Determine cipher type
        if (type == "Caesar" or type == "caesar" or type == "c"):
        #BEGIN CESEAR
            doneCesear = False
            print("Caesar cipher chosen. Here's some information about the Caesar cipher: \n"
            + "The Caesar cipher (famous for use by Julius Caesar)"
            + " is a cipher that shifts the input text's letters in the alphabet by a number (the same for each letter). "
            + "A shift in 3 is most common. Here's an Example: \n"
            + "Using a shift of 3 for the word 'apple' encodes the word as 'dssoh'. "
            + "The A moves over right by three in the alphabet to become 'D', 'P' to 'S', and so on. "
            + "This makes it easy to encode, so much so that it's easy to by hand. "
            + "Sadly, this makes it easy to decode too. \n" )
            while doneCesear == False:
                print("What shift would you like to use? ")
                cShift = input("Shift: ")
                if (cShift == 'n'):
                    print("Exiting cipher now.\n")
                    doneCesear = True
                    break
                    #ends loop
                elif (cShift == 'q' or cShift == 'quit'):
                    print("Exiting program now.\n")
                    doneCesear = True
                    done = True
                    break
                    #ends main loop
                elif (cShift.isdigit() == False):
                    print("Please input a number.")
                    #incorrect input
                else:
                    print("Shift accepted. "
                    + "Would you like to encode or decode? You can type encrypt or decrypt, or just e or d for ease.")
                    cEORD = input("e or d? ")
                    if (cEORD == 'n'):
                        print("Exiting cipher now.\n")
                        doneCesear = True
                        break
                        #ends loop
                    elif (cEORD == 'q' or cEORD == 'quit'):
                        print("Exiting program now.\n")
                        doneCesear = True
                        done = True
                        break
                        #ends main loop
                    elif (cEORD == 'e' or cEORD == 'encrypt' or cEORD == 'Encrypt'):
                        print("Encryption chosen. Please input the text you wish to encode.")
                        cInput = input("Text: ")
                        cOutput = encryptCaesar(cInput, int(cShift))
                        print(cOutput + "\n")
                    elif (cEORD == 'd' or cEORD == 'decrypt' or cEORD == 'Decrypt'):
                        print("Decryption chosen. Please input the text you wish to decode.")
                        cInput = input("Text: ")
                        cOutput = decryptCaesar(cInput, int(cShift))
                        print(cOutput + "\n")
                    else:
                        print("Input had an error, please try again.\n")
                        #if there's an error
        #END CESEAR
        elif (type == "Affine" or type == "affine" or type == "af"):
        #BEGIN AFFINE
            doneAffine = False
            print("Affine cipher chosen. Here's some information about the Affine cipher: \n"
            + "This is very similar to the Caesar cipher, as it shifts over letters in the alphabet with a number, but with a twist: "
            + "Affine also adds a multiplier, this multiples the letter to change it even further. "
            + "The catch is that the multiplier must be a coprime of 26, the number of letters in the alphabet. "
            + "Otherwise, it would go past this number, and there is no 27th letter in our language. \n"
            + "Here are some example coprimes of 26 for you to input: \n"
            + "1, 3, 5, 7, 9 11, 15, 17, 19, 21, 23, and 25. \n"
            + "Here's an example of Affine: \n"
            + "Encoding the word 'apple' with a shift of 3 and a multiplier of 3 transform the word into 'dwwkp'. "
            + "The mathematical equation is e(x) = (ax + b)mod 26 \n"
            + "Naturally this makes decoding and cracking a little harder, but it's really just doing the encoding in reverse. "
            + "Here's the mathematical equation to decode: e(x) = a^-1 (x-b)mod 26 \n")
            while doneAffine == False:
                print("What multiplier and shift would you like to use? ")
                afMult = input("Multiplier: ")
                if (afMult == 'n'):
                    print("Exiting cipher now.\n")
                    doneAffine = True
                    break
                    #ends loop
                elif (afMult == 'q' or afMult == 'quit'):
                    print("Exiting program now.\n")
                    doneAffine = True
                    done = True
                    break
                    #ends main loop
                elif (afMult.isdigit() == False):
                    print("Please input a number.")
                    #incorrect input
                elif (is_coprime(int(afMult), 26) == False):
                    print("Please choose a number that is a coprime of 26")
                    #incorrect coprime number
                else:
                    afShift = input("Shift: ")
                    if (afShift == 'n'):
                        print("Exiting cipher now.\n")
                        doneAffine = True
                        break
                        #ends loop
                    elif ( afShift == 'q' or afShift == 'quit'):
                        print("Exiting program now.\n")
                        doneAffine = True
                        done = True
                        break
                        #ends main loop
                    elif (afShift.isdigit() == False):
                        print("Please input a number.")
                        #incorrect input
                    else:
                        print("Shift accepted. "
                        + "Would you like to encode or decode? You can type encrypt or decrypt, or just e or d for ease.")
                        afEORD = input("e or d? ")
                        if (afEORD == 'n'):
                            print("Exiting cipher now.\n")
                            doneAffine = True
                            break
                            #ends loop
                        elif (afEORD == 'q' or afEORD == 'quit'):
                            print("Exiting program now.\n")
                            doneAffine = True
                            done = True
                            break
                            #ends main loop
                        elif (afEORD == 'e' or afEORD == 'encrypt' or afEORD == 'Encrypt'):
                            print("Encryption chosen. Please input the text you wish to encode.")
                            afInput = input("Text: ")
                            afOutput = encryptAffine(afInput, int(afMult), int(afShift))
                            print(afOutput + "\n")
                        elif (afEORD == 'd' or afEORD == 'decrypt' or afEORD == 'Decrypt'):
                            print("Decryption chosen. Please input the text you wish to decode.")
                            afInput = input("Text: ")
                            afOutput = decryptAffine(afInput, int(afMult), int(afShift))
                            print(afOutput + "\n")
                        else:
                            print("Input had an error, please try again.\n")
                            #if there's an error
        #END AFFINE
        elif (type == "Atbash" or type == "atbash" or type == "at"):
        #BEGIN ATBASH
            doneAtbash = False
            print("Atbash cipher chosen. Here's some information ahout the Atbash cipher: \n"
            + "Like the other shifting ciphers, this cipher encodes by taking a letter, and choosing it's letter on the "
            + "opposite side of the alphabet. So A becomes Z and B becomes Y, and so on. \n"
            + "No shift number is needed. This makes encoding easy, but decoding easily so. Here's and example: \n"
            + "Encoding the word 'apple' shifts it into 'zkkov'. \n")
            while doneAtbash == False:
                print("Would you like to encode or decode? You can type encrypt or decrypt, or just e or d for ease. ")
                atEORD = input("e or d? ")
                if (atEORD == 'n'):
                    print("Exiting cipher now.\n")
                    doneAtbash = True
                    break
                    #ends loop
                elif (atEORD == 'q' or atEORD == 'quit'):
                    print("Exiting program now.\n")
                    doneAtbash = True
                    done = True
                    break
                    #ends main loop
                elif (atEORD == 'e' or atEORD == 'encrypt' or atEORD == 'Encrypt'):
                    print("Encryption chosen. Please input the text you wish to encode.")
                    atInput = input("Text: ")
                    atOutput = encryptAtbash(atInput)
                    print(atOutput + "\n")
                elif (atEORD == 'd' or atEORD == 'decrypt' or atEORD == 'Decrypt'):
                    print("Decryption chosen. Please input the text you wish to decode.")
                    atInput = input("Text: ")
                    atOutput = decryptAtbash(atInput)
                    print(atOutput + "\n")
                else:
                    print("Input had an error, please try again.\n")
                    #if there's an error
        #END ATBASH
        elif (type == "Base64" or type == "base64" or type == "base"):
        #BEGIN BASE64
            doneBase = False
            print("Base64 cipher chosen. Unlike the other shift ciphers, this doesn't use a shift, "
            + "instead it transforms letters from their ASCHII format to a 64-base representation. "
            + "This means that instead of A-Z, it uses uppercase, lowercase, numbers from 0-9, and special charcters to define it's 'language'. "
            + "There are additional bases as well, such as base32 and base16, which you can encode and decode with this cipher."
            + "Here's and example of base64: \n"
            + "Encoding the word 'apple' creates 'YXBwbGU=', which just appears like a lot of nonsense. "
            + "Like with the Baconian cipher, it makes the encoded text hard to read, but cryptologists would recognize this as "
            + "a Base64 or other variant, and could use a similar cipher decoder to uncover it easily. \n")
            while doneBase == False:
                print("Would you like to use Base 64, 32, or 16?")
                baseType = input("Type: ")
                if (baseType == 'n'):
                    print("Exiting cipher now.\n")
                    doneBase = True
                    break
                    #ends loop
                elif (baseType == 'q' or baseType == 'quit'):
                    print("Exiting program now.\n")
                    doneBase = True
                    done = True
                    break
                    #ends main loop
                elif (baseType == '64' or baseType == '32' or baseType == '16'):
                    print("Base chosen. Would you like to encode or decode? You can type encrypt or decrypt, or just e or d for ease. ")
                    baseEORD = input("e or d? ")
                    if (baseEORD == 'n'):
                        print("Exiting cipher now.\n")
                        doneBase = True
                        break
                        #ends loop
                    elif (baseEORD == 'q' or baseEORD == 'quit'):
                        print("Exiting program now.\n")
                        doneBase = True
                        done = True
                        break
                        #ends main loop
                    elif (baseEORD == 'e' or baseEORD == 'encrypt' or baseEORD == 'Encrypt'):
                        print("Encryption chosen. Please input the text you wish to encode.")
                        baseInput = input("Text: ")
                        baseOutput = encryptBase64(baseInput, int(baseType))
                        print(baseOutput + "\n")
                    elif (baseEORD == 'd' or baseEORD == 'decrypt' or baseEORD == 'Decrypt'):
                        print("Decryption chosen. Please input the text you wish to decode.")
                        baseInput = input("Text: ")
                        baseOutput = decryptBase64(baseInput, int(baseType))
                        print(baseOutput + "\n")
                    else:
                        print("Input had an error, please try again.\n")
                        #if there's an error
                else:
                    print("Please input a number.\n")
                    #for incorrect input
        #END BASE64
        elif (type == "Baconian" or type == "baconian" or type == "bacon"):
        #BEGIN BACONIAN
            doneBacon = False
            print("Baconian cipher chosen. Unlike the other shift ciphers, this one replaces a letter with a series of five letters. "
            + "These letters are a combination of a and b, and are set. so A will always equal 'aaaaa' and B will always equal 'aaaab'. "
            + "It's essentially trading one alphabet for another, each with 26 'letters'. "
            + "As a note: for this cipher, each letter is a different 5-letter combination of a or b, but there is another version that"
            + " I and J, and U and V have the same 5-letter combinations, making a 24 alphabet for the encoding instead of 26. \n"
            + "In terms of security, it is a lot harder to read, but it's easy to identify if you have basic cryptography knowledge. "
            + "Additionally, I find it quite tiresome to use without some sort of digital/automatic version, it's five time the "
            + "length to hide the original word. Here's an example: \n"
            + "The encoding of 'apple' leads to 'aaaaaabbbbabbbbababbaabaa', which is quite long. \n"
            + "Note: due to how the decryption works, all letters will be in lowercase and no special characters will be registered.")
            while doneBacon == False:
                print("Would you like to encode or decode? You can type encrypt or decrypt, or just e or d for ease. ")
                baconEORD = input("e or d? ")
                if (baconEORD == 'n'):
                    print("Exiting cipher now.\n")
                    doneBacon = True
                    break
                    #ends loop
                elif (baconEORD == 'q' or baconEORD == 'quit'):
                    print("Exiting program now.\n")
                    doneBacon = True
                    done = True
                    break
                    #ends main loop
                elif (baconEORD == 'e' or baconEORD == 'encrypt' or baconEORD == 'Encrypt'):
                    print("Encryption chosen. Please input the text you wish to encode.")
                    baconInput = input("Text: ")
                    baconOutput = encryptBaconian(baconInput)
                    print(baconOutput + "\n")
                elif (baconEORD == 'd' or baconEORD == 'decrypt' or baconEORD == 'Decrypt'):
                    print("Decryption chosen. Please input the text you wish to decode.")
                    baconInput = input("Text: ")
                    baconOutput = decryptBaconian(baconInput)
                    print(baconOutput + "\n")
                else:
                    print("Input had an error, please try again.\n")
                    #if there's an error
        #END BACONIAN
        elif (type == "Combine" or type == "combine"):
        #BEGIN COMBINE
            combShift = '0'
            combMult = '0'
            combType = '0'
            doneCombine = False
            print("Combination ciphers chosen. This allows you to combine two ciphers together"
            + "However, there are limitations: You can't use Base64 before the shift ciphers. "
            + "This is because the non-shift ciphers read only the letters of the text, they can't encrypt special characters. "
            + "Additionally, the shift ciphers do not alter special characters."
            + "Here's an example: \n If I wanted to encode the phrase 'base' in Base 64, then encode it further into a Caesar shift; "
            + "then 'base' would then be encoded into 'YmFzZQ=='. After that, if I wished to encode this into "
            + "Caesar with a shift of 5, it would result in: 'DrKeEV=='. This can't be decrypted. \n"
            + "As for decryption, you need to input the second cipher used in encryption first, then the first cipher for encryption second. "
            + "This is because you have to peel back the layers in the order applied. \n"
            + "You will first input the encryption or decryption, text, the first cipher and related values (like a shift or type), and the same for the second cipher."
            )
            while doneCombine == False:
                combText = input("Please input the text you wish to combine: ")
                combEORD = input("Would you like to encrypt or decrypt? ")
                if (combEORD == "n"):
                    print("Exiting cipher now.\n")
                    doneCombine = True
                    break
                    #ends loop
                elif (combEORD == 'q' or combEORD == 'quit'):
                    print("Exiting program now.\n")
                    doneCombine = True
                    done = True
                    break
                    #ends main loop
                elif (combEORD == "Encrypt" or combEORD == "encrypt" or combEORD == "e"
                or combEORD == "Decrypt" or combEORD == "decrypt" or combEORD == "d"):
                    comb1 = input("Please input the first cipher you want to use: ")
                    if (comb1 == "n"):
                        print("Exiting cipher now.\n")
                        doneCombine = True
                        break
                        #ends loop
                    elif (comb1 == 'q' or comb1 == 'quit'):
                        print("Exiting program now.\n")
                        doneCombine = True
                        done = True
                        break
                        #ends main loop
                    elif (comb1 == "Base64" or comb1 == "base64" or comb1 == "base"):
                        if (combEORD == "Encrypt" or combEORD == "encrypt" or combEORD == "e"):
                            print("Base64 cannot be the first encryption")
                        else:
                            combType = input("Please enter which type you want to use (64, 32, and 16 only): ")
                            if (combType == "n"):
                                print("Exiting cipher now.\n")
                                doneCombine = True
                                break
                                #ends loop
                            elif (combType == 'q' or combType == 'quit'):
                                print("Exiting program now.\n")
                                doneCombine = True
                                done = True
                                break
                                #ends main loop
                            elif (combType == '64' or combType == '32' or combType == '16'):
                                print("Type confirmed.")
                            else:
                                print("Please choose a number that is either '64', '32', or '16'. ")
                    elif (comb1 == "Caesar" or comb1 == "caesar" or comb1 == "c"):
                        combShift = input("Please input a number for the shift: ")
                        if (combShift == "n"):
                            print("Exiting cipher now.\n")
                            doneCombine = True
                            break
                            #ends loop
                        elif (combShift == 'q' or combShift == 'quit'):
                            print("Exiting program now.\n")
                            doneCombine = True
                            done = True
                            break
                            #ends main loop
                        else:
                            print("Shift chosen.")
                    elif (comb1 == "Affine" or comb1 == "affine" or comb1 == "af"):
                        combShift = input("Please input a number for the shift: ")
                        if (combShift == "n"):
                            print("Exiting cipher now.\n")
                            doneCombine = True
                            break
                            #ends loop
                        elif (combShift == 'q' or combShift == 'quit'):
                            print("Exiting program now.\n")
                            doneCombine = True
                            done = True
                            break
                            #ends main loop
                            print("Shift chosen.")
                        combMult = input("Please input a number for multiplication (must be a coprime of 26): ")
                        if (combMult == "n"):
                            print("Exiting cipher now.\n")
                            doneCombine = True
                            break
                            #ends loop
                        elif (combMult == 'q' or combMult == 'quit'):
                            print("Exiting program now.\n")
                            doneCombine = True
                            done = True
                            break
                            #ends main loop
                    else:
                        print("Cipher chosen.")
                    #end comb1
                    comb2 = input("Please input the second cipher you want to use: ")
                    if (comb1 == "n"):
                        print("Exiting cipher now.\n")
                        doneCombine = True
                        break
                        #ends loop
                    elif (comb1 == 'q' or comb1 == 'quit'):
                        print("Exiting program now.\n")
                        doneCombine = True
                        done = True
                        break
                        #ends main loop
                    elif (comb2 == "Base64" or comb2 == "base64" or comb2 == "base"):
                        if (combEORD == "Decrypt" or combEORD == "decrypt" or combEORD == "d"):
                            print("Base64 cannot be the second decryption")
                        else:
                            combType = input("Please enter which type you want to use (64, 32, and 16 only): ")
                            if (combType == "n"):
                                print("Exiting cipher now.\n")
                                doneCombine = True
                                break
                                #ends loop
                            elif (combType == 'q' or combType == 'quit'):
                                print("Exiting program now.\n")
                                doneCombine = True
                                done = True
                                break
                                #ends main loop
                            elif (combType == '64' or combType == '32' or combType == '16'):
                                print("Type confirmed.")
                            else:
                                print("Please choose a number that is either '64', '32', or '16'. ")
                    elif (comb2 == "Caesar" or comb2 == "caesar" or comb2 == "c"):
                        combShift = input("Please input a number for the shift: ")
                        if (combShift == "n"):
                            print("Exiting cipher now.\n")
                            doneCombine = True
                            break
                            #ends loop
                        elif (combShift == 'q' or combShift == 'quit'):
                            print("Exiting program now.\n")
                            doneCombine = True
                            done = True
                            break
                            #ends main loop
                        else:
                            print("Shift chosen.")
                    elif (comb2 == "Affine" or comb2 == "affine" or comb2 == "af"):
                        combShift = input("Please input a number for the shift: ")
                        if (combShift == "n"):
                            print("Exiting cipher now.\n")
                            doneCombine = True
                            break
                            #ends loop
                        elif (combShift == 'q' or combShift == 'quit'):
                            print("Exiting program now.\n")
                            doneCombine = True
                            done = True
                            break
                            #ends main loop
                            print("Shift chosen.")
                        combMult = input("Please input a number for multiplication (must be a coprime of 26): ")
                        if (combMult == "n"):
                            print("Exiting cipher now.\n")
                            doneCombine = True
                            break
                            #ends loop
                        elif (combMult == 'q' or combMult == 'quit'):
                            print("Exiting program now.\n")
                            doneCombine = True
                            done = True
                            break
                            #ends main loop
                    else:
                        print("Cipher chosen.")
                    #end comb2
                else:
                    print("You must enter either an encryption or decryption confirmation.")

                print("Compiling cipher combinaiton...\n")
                if (combShift.isdigit() == False):
                    combShift = '0'
                if (combMult.isdigit() == False or is_coprime(int(combMult), 26) == False):
                    combMult = '0'
                if (combType != '64' or combType != '32' or combType != '16'):
                    combType = '0'
                #print("text is: " + combText + ", eord is: " + combEORD + ", cipher1 is: " + comb1
                #+ ", cipher2 is: " + comb2 + ", shift is: " + combShift + ", multiplier is: "
                #+ combMult + ", type is: " + combType)
                combResults = combine_ciphs(combText, combEORD, comb1, comb2, combShift, combMult, combType)
                print(combResults)
        #END COMBINE

        elif (type == "quit" or type == "q"):
            print ("Exiting program now.")
            done = True
            #end the loop
        else:
            print("Input had an error, please try again.\n")

#END OF MAIN

main()

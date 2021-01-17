class Caesar:
    # Note this class is here just to avoid the use of global variables.
    Maj = ["A", "B", "C", "D",
           "E", "F", "G", "H",
           "I", "J", "K", "L",
           "M", "N", "O", "P",
           "Q", "R", "S", "T",
           "U", "V", "W", "X",
           "Y", "Z"]
    Min = ["a", "b", "c", "d",
           "e", "f", "g", "h",
           "i", "j", "k", "l",
           "m", "n", "o", "p",
           "q", "r", "s", "t",
           "u", "v", "w", "x",
           "y", "z"]
    Try = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    Truth = 42 # Yes I know this have nothing to do here.


def cipher(v=0, phrase="", cipkey=0):
    if v == 0:
        print("Warning! This program can cipher 50 characters at maximum")
        phrase = str(input("Sentence to cipher: "))
        if len(phrase) > 50:
            print("Thing to cipher is too big!")
            raise Exception  # "Thing to cipher is too big!"
        cipkey = int(input("Cipher Key: "))
        if type(cipkey) != int:
            print("Invalid Cipher Key")
            raise Exception  # "Invalid Cipher Key"
        outfor = str(input("upper letter output? Y/N: "))
        if outfor == "Y" or outfor == "y":
            dico = Caesar.Maj
            phrase = phrase.upper()
        else:
            dico = Caesar.Min
            phrase = phrase.lower()
    else:
        dico = Caesar.Maj
        phrase = phrase.upper()
    output = str()
    for i in range(len(phrase)):
        if phrase[i] == " ":
            output = output + " "
        else:
            temp = dico.index(phrase[i])
            temp = temp + cipkey
            tmp2 = temp % 25
            tmp3 = dico[tmp2]
            output = output + tmp3
    print(output)
    return None
def decipher(v=0, phrase="", cipkey=0):
    if v == 0:
        print("Warning! This program can decipher 50 characters at maximum")
        phrase = str(input("Sentence to decipher: "))
        if len(phrase) > 50:
            print("Thing to decipher is too big!")
            raise Exception  # "Thing to cipher is too big!"
        cipkey = int(input("Decipher Key: "))
        if type(cipkey) != int:
            print("Invalid Decipher Key")
            raise Exception  # "Invalid Cipher Key"
        outfor = str(input("upper letter output? Y/N: "))
        if outfor == "Y" or outfor == "y":
            dico = Caesar.Maj
            phrase = phrase.upper()
        else:
            dico = Caesar.Min
            phrase = phrase.lower()
    else:
        dico = Caesar.Maj
        phrase = phrase.upper()
    output = str()
    for i in range(len(phrase)):
        if phrase[i] == " ":
            output = output + " "
        else:
            temp = dico.index(phrase[i])
            temp = temp - cipkey
            if temp < 0:
                temp = temp * -1
            tmp2 = temp % 25 + 1
            tmp3 = dico[tmp2]
            output = output + tmp3
    print(output)
    return None


def bruteforce():
    phr = str(input("Sentence to bruteforce: "))
    for num in range(26):
        decipher(1, phr, num)
    return None

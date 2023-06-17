import string
import random


class CreatePassword():
    """
    Generates a password that includes all uppercase letters, lowercase letters, special characters and numbers 
    by entering a value for the number of password digits to be generated.
    """
    def __init__(self):
        self.self = self

    def chars_source(self):
        chars = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
        return chars

    def set_units(self):
        while 1:
            a = input("---\nEnter the number of password digits to generate : ")
            if not a.isnumeric():
                print("---\nEnter again")
                continue
            else:
                rangenum=int(a)
                if rangenum < 4:
                    print("---\nEnter 4 or more")
                    continue
                break
        return rangenum

    def create_password(self):
        units = self.set_units()
        while 1:
            pw=str()

            for i in range(units):
                pw += random.choice(self.chars_source())

            upper = 0
            lower = 0
            digits = 0
            punctuation = 0

            # Check for uppercase, lowercase, numbers and special characters
            for i in pw:
                if i in string.ascii_uppercase:
                    upper += 1
                elif i in string.ascii_lowercase:
                    lower += 1
                elif i in string.digits:
                    digits += 1
                else:
                    punctuation +=1
            
            # escape if have all
            if upper*lower*digits*punctuation > 0:
                print("password : ",pw)
                break


if __name__== "__main__":
    pw = CreatePassword()
    pw.create_password()
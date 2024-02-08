import random
import string

def complex_password(size):
    comcharacters = string.ascii_letters + string.digits + string.punctuation +string.octdigits
    compassword = ''.join(random.choice(comcharacters) for _ in range(size))
    return compassword

def generate_password(size):
    characters = string.ascii_letters+string.digits
    password = ''.join(random.choice(characters) for _ in range(size))
    return password

size = int(input("Enter the size of the password: "))
print("Complex Password(1) and Simple Password(2)")
Pass_type = input("Choose your Password Type : ")

if Pass_type=="1":
    Your_complex_pass = complex_password(size)
    print("Generated Password :", Your_complex_pass)
else:
    Your_simple_pass = generate_password(size)
    print("Generated Password :",Your_simple_pass)

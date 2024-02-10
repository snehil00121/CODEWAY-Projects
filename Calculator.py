def add(a, b):
    answer = a + b
    print("Output : "+str(a) + "+" + str(b) + "= "  +str(answer))

def sub(a, b):
    answer = a - b
    print("Output : "+str(a) + "-" + str(b) + "= "  +str(answer))

def mult(a, b):
    answer = a * b
    print("Output : "+str(a) + "*" + str(b) + "= "  +str(answer))

def div(a, b):
    answer = a / b
    print("Output : "+str(a) + "/" + str(b) + "= "  +str(answer))


print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
print("E.Exit")

choice = input("Input your choices : ")
if choice=="a" or choice=="A":
    print("Addition")
    a=int(input("First Number : "))
    b=int(input("Second Number : "))
    add(a,b)

elif choice =="b" or choice=="B":
    print("Subtraction")
    a=int(input("First Number : "))
    b=int(input("Second Number : "))
    sub(a,b)

elif choice =="c" or choice=="C":
    print("Mutiplication")
    a=int(input("First Number : "))
    b=int(input("Second Number : "))
    mult(a,b)

elif choice =="d" or choice=="D":
    print("Division")
    a=int(input("First Number : "))
    b=int(input("Second Number : "))
    div(a,b)

elif choice =="e" or choice=="E":
    print("Programe Ended") 
    quit()
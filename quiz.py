import math
print("                                Welcome to python quiz Game                                 ")
print("Rules: +1 mark will be rewarded for every correct answer and -0.25 will be deducted for every incorrect answer. ")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
print("Choose the correct option and write to option 'a' or 'b' or 'c' or 'd' ")
score = 0
correct = 0
Incorrect = 0

answer1 = input("1.Which of the following is NOT a prime number? \n (a).17 \n (b).21 \n (c).29 \n (d).37 \n >> ")
if answer1.title() == "B":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : 21")
    score -=0.25
    Incorrect +=1

answer2 = input("2.In which year did Isaac Newton publish his groundbreaking work Philosophiæ Naturalis Principia Mathematica?  \n (a).1687 \n (b).1652 \n (c).1756 \n (d).1605 \n >>  ")
if answer2.title() == "A":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : 1687")
    score -=0.25
    Incorrect +=1

answer3 = input("3.Which chemical element has the highest melting point?  \n (a).Carbon(C) \n (b).Tungsten(W) \n (c).Titanium(Ti) \n (d).Platinum(Pt) \n >>  ")
if answer3.title() == "B":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : Tungsten")
    score -=0.25
    Incorrect +=1

answer4 = input("4.Who was the first woman to win a Nobel Prize?  \n (a).Marie Curie \n (b).Rosalind Franklin \n (c).Ada Lovelace \n (d).Barbara McClintock \n >>  ")
if answer4.title() == "A":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : Marie Curie")
    score -=0.25
    Incorrect +=1

answer5 = input("5.What is the capital city of Australia?  \n (a).Melbourne \n (b).Sydney \n (c).Canberra \n (d).Brisbane \n >>  ")
if answer5.title() == "C":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : Canberra")
    score -=0.25
    Incorrect +=1

answer6 = input("6.Which literary work begins with the famous line, \"It was the best of times, it was the worst of times\"?  \n (a).Pride and Prejudice \n (b).Moby Dick \n (c).A Tale of Two Cities \n (d).The Great Gatsby \n >>  ")

if answer6.title() == "C":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : A Tale of two Cities")
    score -=0.25
    Incorrect +=1

answer7 = input("7.Who painted the famous artwork \"Starry Night\"?  \n (a). Pablo Picasso \n (b).Vincent van Gogh \n (c).Leonardo da Vinci \n (d).Claude Monet \n >>  ")
if answer7.title() == "B":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : Vincent van Gogh")
    score -=0.25
    Incorrect +=1

answer8 = input("8.Which planet in our solar system has the shortest day?  \n (a).Venus \n (b).Earth \n (c).Jupiter \n (d).Mercury \n >>  ")
if answer8.title() == "D":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : Mercury")
    score -=0.25
    Incorrect +=1

answer9 = input("9.What is the chemical symbol for gold?  \n (a).Au \n (b).Ag \n (c).Gd \n (d).Gr \n >>  ")
if answer9.title() == "A":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : Au")
    score -=0.25
    Incorrect +=1

answer10 = input("10.Who wrote the famous play \"Hamlet\"?  \n (a).William Shakespeare \n (b).Christopher Marlowe \n (c).John Milton \n (d).Geoffrey Chaucer \n >>  ")
if answer10.title() == "A":
    print("Correct :)")
    score +=1
    correct += 1
else:
    print("Opps you're Incorrect !")
    print("Correct answer : William Shakespeare")
    score -=0.25
    Incorrect +=1

print("Your Total score is : " + str(score))
print("Total Number of correct answer are : " + str(correct) )
print("Total Number of incorrect answer are : " + str(Incorrect) )
if 0<=score<=5:
    print("You can improve !!")
else:
    print("Well Played :)")
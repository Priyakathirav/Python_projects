print("Welcome to my Quizgame Challenge!")
game=input("What do you want to play? ")
if game.lower()!="yes":

    quit()
print("Let's play the game :)")
score=0
answer=input("Who is the developer of python? ")
if answer.lower()=="guido van rossum":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("In which year was the Python language developed? ")
if answer.lower()=="1989":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("In which language is Python written? ")
if answer=="C":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("Which one of the following is the correct extension of the Python file? ")
if answer.lower()==".py":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("What do we use to define a block of code in Python language? ")
if answer.lower()=="indentation":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("Which character is used in Python to make a single line comment? ")
if answer.lower()=="#":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("What is the method inside the class in python language? ")
if answer.lower()=="function":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("Which keyword is used for function in Python language? ")
if answer.lower()=="def":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("What does pip stand for python? ")
if answer.lower()=="preferred installer program":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("Which of the following is the truncation division operator in Python? ")
if answer.lower()=="//":
    print("Correct!")
    score+=1
else:
    print("Incorrect")
print("you got " +  str(score)  + " questions correct!")
print("you got " +  str((score/4)*100)  + " %")
print("End of the Quizgame Challenge")


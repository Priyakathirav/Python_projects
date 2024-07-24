import random
range=input("Type a number: ")
if range.isdigit():
    range=int(range)
    if range<=0:
            print("Please type a number larger than 0 next time")
            quit()
else:
    print("Please type a number next time")
    quit()

random_number=random.randint(0,range)
guesses=0

while True:
     guesses+=1
     user_guess=input("Make a guess:")
     if user_guess.isdigit():
        user_guess=int(user_guess)
        
     else:
        print("Please type a number next time")
        continue

     if user_guess==random_number:
          print("You got it :)")
          break
     elif user_guess>random_number:
          print("You were above the numbrer :(")
     else:
          print("You were below the number :(")

print("You got it in "+str(guesses)+" Guesses")

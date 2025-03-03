import random 
print ("Welcome to island 42! You might be wondering why you are here? If you can complete all the challenges you get... 42.000 USA DOLLARS! Good luck...")
name = input ("Enter your name:")
age = int(input("Enter your age:"))
print (f"Hello! Nice to meet you {name}!Oh wow you are {age}")

print ("The first challenge is at the restaurant")
option = int(input(" You found sweeties on the floor, do you 1, eat them or 2 walk to the restaurant?"))
if option > 1:
    print ("You made it to the challenge!")

elif option < 2: 
    print ("You got sick and vomited! But you still made it to the challenge")

print ("Here is your first challenge! It's easy! just get this question correct!")
answerrr = input ("True or false, Stockholm is Sweden's capital city?:")

if answerrr == True:
    print ("Yes exactly") 
elif answerrr == False:
    print ("No, but i'll let you go ")

print ("Here is your second challenge!")
math = int(input("What is 8*7?:"))

if math == 56:
     print ("Correct!")
else:
     print ("Incorrect")
print ("The last challenge is guess the number from 1 - 10, you have 3 chances!! Win to move on to the next challenge!")

random_number = random.randint(1 , 10)
print("I have though of a number... guess it!")
guess_num = int(input("Guess the number 1 - 10:"))
if guess_num == random_number:
        print ("You did it! now you can move onto the next challenge at the beach!")

else:
    print ("Oops it was incorrect!")

    print("I have though of a number... guess it!")
guess_num = int(input("Guess the number 1 - 10:"))
if guess_num == random_number:
        print ("You did it! now you can move onto the next challenge at the beach!")

else:
    print ("Oops it was incorrect!")
    
    print("I have though of a number... guess it!")
guess_num = int(input("Guess the number 1 - 10:"))
if guess_num == random_number:
        print ("You did it! now you can move onto the next challenge at the beach!")

else:
    print ("You died!Thanks for playing")
    
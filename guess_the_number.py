import random
print("Welcomet to the Guess the Number Game!")
is_ready=input("Are you ready? (yes/no): ")
if is_ready!="yes": 
    print("Maybe next time!")
    quit()
else:
    print("Let's start the game!")
    r=random.randint(0,11) 
    user_input=-1
    while user_input!=r:
        user_input=int(input("Guess a number between 1 and 10: "))
        if user_input<r:
            print("Too Low!")
        elif user_input>r:
            print("Too High!")
        else:
            print("Congratulations? You guessed it right!")
            break
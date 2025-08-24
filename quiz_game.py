print("Welcome to the Quiz Game!") 
score=0 
answer=input("Would you like to play? (yes/no): ")
if answer != "yes":
    print("Maybe next time!")
    quit() 
else:
    print("Great! Let's start the quiz.") 
    answer=input("CPU stands for? ")
    if answer=="central processing unit":
        print("Correct!")
        score+=1
    else:
        print("Incorrect! The correct answer is 'central processing unit'.") 
        if score>0:
            score-=1 

    answer=input("what is the capital of India? ")
    if answer=="New Delhi":
        print("Correct!")
        score+=1 
    else:
        print("Incorrect! The correct answer is 'New Delhi'.")
        if score>0:
            score-=1 

    answer=input("what is color of Sun? ")
    if answer=="White":
        print("Correct!")
        score+=1 
    else:
        print("Incorrect! The correct answer is 'White'.")
        if score>0:
            score-=1  

    answer=input("what is the GUI? ")
    if answer=="Graphical User Interface":
        print("Correct?")
        score+=1 
    else:
        print("Incorrect! The correct answer is 'Graphical User Interface'.")
        if score>0:
            score-=1 

    answer=input("what is the color of Blood? ")
    if answer=="Red":
        print("Correct?")
        score+=1 
    else:
        print("Incorrect! The correct answer is 'Red'.") 
        if score>0:
            score-=1  
    
    print("Your final score is: " + str(score) + "/5")
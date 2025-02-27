'''
rock paper scissors
where rock beats scissors, paper beats rock, scissors beats paper
1: 
i will take user's input as r,p,s
i will assing r = 1 p = -1 and s = 0 for mathemathecal reson 
then with the help of random module computer will choose randomly three of them 
i set them with using dictionary that tells me r = rock and more
then with the help of conditioanal statement i will check who wins
BONUS IDEA: After finising base program user and computer will have compete 
of 10 times that will check who wins more
'''
####lets setting up the base
from random import *
def main():
    i = 1
    you_won = 0
    computer_won = 0
    while i != 10:
        computer = choice([1,-1,0])
        list0 = ["r","p","s"]
        user = input("Enter your choice(r,p,s): ").lower()
        if user not in list0:
            print("Please enter a right choice!")
            you_won -= 1 # ruduceing one point
            continue
        dict1 = {"r":1,
                "p":-1,
                "s":0}
        dict2 = {    #dict2 have reversed values
                1: "rock",
                -1: "paper",
                0: "scissors"
            }
        main_user = dict1[user] # gets mathemethecal value like computer have
        #printing what we chosed
        print(f"You chosed: {dict2[main_user]}\nComputer chosed: {dict2[computer]}")
        # setting conditions     
        if (computer == 1 and main_user == -1) or (computer == -1 and main_user == 0) or (computer == 0 and main_user == 1):
            print("You win!")
            you_won += 1
        elif computer == main_user:
            print("Its a draw!")
            you_won += 1 
            computer_won += 1
        else:
            print("You lose!")
            computer_won += 1    
  
        i += 1
    if you_won > computer_won:
        print(f"You won: {you_won}\nComputer won: {computer_won}")
    elif computer_won > you_won:
        print(f"Computer won: {computer_won}\nYou won {you_won}")               

    
    
    
if __name__ == "__main__":
    main()
    

'''
steps:
1:
user input
compter generate random number
2: 
I need to tell user number is low or high 
I need to count the number of guesses
thats all 
'''
from random import *
def main():
    count = 0
    try:    
        user = int(input("Enter your guess(1-100): "))
    except ValueError:
        print("Enter a valid number!")
        return 0
    computer = randint(1,100)
    while user != computer:
        count += 1
        if user > computer:
            print("Too High!")
        elif user < computer:
            print("Too Low!")
        user = int(input("Enter your guess(1-100): "))
    print(f"Perfect Guess!\nTotal Guess: {count}")            
if __name__ == "__main__":
    main()        
    
        
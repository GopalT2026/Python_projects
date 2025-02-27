#My project will be user will enter his chosen times of number
#And I have to find out the largest one of those numbers
# without using a max function
'''
My steps:
input zone:
1st- I have input how many number user want
taking all input according do user's chosen number
processing zone:
2nd- I will need a list to store all numbers
3rd- using loop I will store the maximum value
output zone:
4th- I have to show output with greetings to the user
'''
numbers = []
user = int(input("How many number you want: "))
for i in range(user):
    num = int(input(f"Enter a number({i+1}): "))
    numbers.append(num)
max_ = 1
for i in numbers:
    if i > max_:
        max_ = i
        
print(f"All numbers are: {numbers}\nMaximum number is: {max_}\nHave a nice Day Mate!")  
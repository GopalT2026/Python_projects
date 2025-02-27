#example of some classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old!")    
        
gopal = Person("Gopal Mahato",19)
gopal.greet()
dibyendu = Person("Dibyendu Garai",19)
dibyendu.greet()        

class Dog:
    def __init__(self, name,owner,sound,owner_address):
        self.name = name
        self.owner = owner
        self.sound = sound
        self.owner_address = owner_address
        
    def info(self):
        print(f"Dog Name: {self.name}\nDog Sound: {self.sound}\nDog Owner: {self.owner}\nDog Owner Address: {self.owner_address}")
        
dog1 = Dog("Puppy","Gopal Mahato","Bhow! Bhow!","L.A.,USA")
dog1.info()
dog2  = Dog("Jones","Mr. Engineer","bhook! bhook","Manchester,U.K.")
dog2.info()            

### gemini suggest me some basic class practece
## Exercise1: Student class
class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    # methods are Display student information and Update student grade
    def std_info(self):
        print(f"Student Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}")
        
    def update_grade(self, g):
        self.grade = g
        print(f"Your upgrade is: {self.grade}")
gopal = Student("Gopal Mahato","19","A+")
gopal.std_info()
gopal.update_grade("AA")      

#### Exercise2: Bank Account class
# attributes are: account_number and balance
# include methods to: Deposite money, withdrawal money, Display account balance
class Bank_account:
    def __init__(self, ac_num, balance):
        self.ac_num = ac_num
        self.balance = balance
        
    def display_balance(self):
        print(f"Account number of xxxxxxxx{self.ac_num}\nYour current balance is: {self.balance}") 
        
    def with_draw(self,ammunt):
        if self.balance < ammunt:
            print("Insufficeint Funds!")
        else:    
            self.balance -= ammunt
            print(f"{ammunt} is successfully withdrawn!\nYour current balance is: {self.balance}")
    def deposite(self, ammunt):
        if ammunt <= 0:
            print("Enter some valid ammunt!")
        else:
            self.balance += ammunt
        print(f"{ammunt} is deposite successfully!\nYour current balance is: {self.balance}")
gopal = Bank_account("2342",5000)
gopal.display_balance()
gopal.deposite(5000)
gopal.with_draw(1000)   
#### exersies3 book class
# attributes are: title, author, pages
#includes methods to: Display book information, Update book author

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    # here is two methods    
    def book_info(self):
        print(f"Book Title: {self.title}\nAuthor Name: {self.author}\nTotal Pages: {self.pages}") 
        
    def update_book_author(self,name):
        self.author = name
        print(f"Updated Author: {self.author}")
book1 = Book("Think and Grow Rich","Napoleon Hill","226")
book1.book_info()
book1.update_book_author("NEPOLEON HILL")  
# this program is working smoothly! I am proud of Myself!
 ### Exercise 4:ractangle class
# attributes are: width and height
# incude methods to: calculate ractangle area, calculate ractangle perimeter
class Ractangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area_ract(self):
        print(f"Area of this ractangle (w={self.width} and h={self.height}) is: {self.width*self.height}") 
        
    def peri_ract(self):
        print(f"Perimeter if this ractangle (w={self.width} and h={self.height}) is:{2*(self.width+self.height)}")
        
ract1 = Ractangle(7,10)
ract1.area_ract()
ract1.peri_ract()    
### Exercise 5: Employee class
#attributes are: name, age, salary
#include methods to display employee information, Update employee salary
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def info(self):
        print(f"Employee Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}")
        
    def update_salary(self, ammout):
        self.salary = ammout
        print(f"Your updated salary: {self.salary}")                      
gopal = Employee("Gopal Mahato",21,4000000)
gopal.info()
gopal.update_salary(5000000)
           
       
                     
        
                         
        
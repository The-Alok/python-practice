#Exercise 1: Print Numbers 1 to 10
i=1
while i<=10:
    print(i)
    i+=1
# Exercise 2: Count Down
n=int(input("Enter a number: "))
while n>0:
    print(n)
    n-=1
#Exercise 3: Password Retry
correct_password = "python123"
password= input("Enter password: ")
while(password!=correct_password):
    print("Wrong password.")
    password= str(input("Enter password: "))
print("Access Granted")
#Exercise 4: Number Guessing Game
secret_number = 7
guess = int(input("Guess the number: "))
while guess!=secret_number:
    if guess<secret_number:
        print("Too Low !")
    elif guess>secret_number:
        print("Too High !")
    guess = int(input("Guess the number: "))
print("Correct !")
#Exercise 5: Multiplication Table
count = 1
m = int(input("Enter number: "))
while count<=10:
    print(f"{m} x {count} = {m * count}")
    count+=1
#Mini Project: Calculator
while True:
    choice = int(input("\nCalculator:\n""1-Add\n""2. Subtract\n""3. Multiply\n""4. Divide\n""5. Exit\n""Choice: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 5:
        print("Calculator closed")
        break
    elif choice == 2:
        sub = a-b
        print(sub)
    elif choice == 3:
        mul = a*b
        print(mul)
    elif choice == 4:
        div = a/b
        print(div)
    elif choice == 1:
        add = a+b 
        print(add)
    else:
         continue
#Exercise 6:Dragon Game
while True:    
    print("\nYou see a dragon !\n 1. Fight\n 2. Run\n")
    choice = int(input("Enter choice : "))
    if  choice == 1:
            weapon = int(input("\nChoose your weapon:\n""1. Sword\n""2. Stick\n""3. Magic Spell\n""Enter choice: "))
            if weapon == 1:
                print("\nYou killed the dragon.\n Victory !.")
            elif weapon == 2:
                print("\nThe dragon roasted you.\n Game Over.")
            elif weapon == 3:
                print("Dragon becomes your friend")
            else:
                print("Invalid weapon")
    elif choice == 2:
            print("\nYou escaped safely.\n Victory!")
    else:
            print("\nInvalid choice.")
    restart = int(input("\n 1. Yes \n 2. No \n Play Again ? "))
    if restart == 1:
        continue
    else:
        break
a = int(input("Enter a number : "))
if a%2==0:
    print("\nEven number.\n")
else:
    print("\nOdd number\n")
password = "python123"
b=input("\nEnter password : ")
if password==b:
        print("Access granted\n")
else:
        print("Access Denied\n")
print("\nYou see a dragon !\n 1. Fight\n 2. Run\n")
choice = int(input("Enter choice : "))
if  choice == 1:
        print("\nThe dragon roasted you.\n Game Over.")
elif choice == 2:
        print("\nYou escaped safely.\n Victory!")
else:
        print("\nInvalid choice.")        
print("\nYou see a dragon !\n 1. Fight\n 2. Run\n")
choice = int(input("Enter choice : "))
if  choice == 1:
        weapon = int(input("\nChoose your weapon:\n""1. Sword\n""2. Stick\n""3. Magic Spell\n""Enter choice: "))
        if weapon == 1:
            print("\nYou killed the dragon.\n Victory !.")
        elif weapon == 2:
            print("\nThe dragon roasted you.\n Game Over.")
        else:
            print("\n Dragon becomes your friend 🐉")
elif choice == 2:
        print("\nYou escaped safely.\n Victory!")
else:
        print("\nInvalid choice.")
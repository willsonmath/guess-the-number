import random
def game(mode):
    print()
    print("Guess the number (1 - ", mode, ")")
    print()
    number = random.randint(1,mode)
    guess = int(input("guess : "))
    attempts = 1
    while guess != number:
        if guess > mode or guess < 1:
            print("Please enter a number between 1 and ", mode)
            print()
            guess = int(input("guess : "))
        elif guess > number:
            print("too high")
            print()
            attempts += 1
            guess = int(input("guess : "))
        else:
            print("too low")
            print()
            attempts += 1
            guess = int(input("guess : "))
    if guess == number:
        print("\n" + "Correct!!")
        print("Your attempt(s) : " , attempts)
        print()
        again = input("Play again?(yes/no) : ").lower()
        while again != "yes" and again != "no":
            print()      
            print("Please select the available one")
            print()
            again = input("Play again?(yes/no) : ").lower()
        if again == "yes":
            print()
            level = input("Select level(easy/medium/hard) : ").lower()
            while level != "easy" and level != "medium" and level != "hard":
                print()
                print("Please select the available one")
                print()
                level = input("Select level(easy/medium/hard): ").lower()
            if level == "easy":
                game(10)
            elif level == "medium":
                game(100)
            elif level == "hard":
                game(1000)
            
        elif again == "no":
                print()
                print("Thanks for your participate ;)")
        
print("Guess The Number")
print("=" * 20)
print("Level;")
print("easy = 1 - 10")
print("medium = 1 - 100")
print("hard = 1 - 1000")
print("=" * 20)
level = input("Select level(easy/medium/hard): ").lower()
while level != "easy" and level != "medium" and level != "hard":
    print()
    print("Please select the available one")
    print()
    level = input("Select level(easy/medium/hard): ").lower()
if level == "easy":
    game(10)
elif level == "medium":
    game(100)
elif level == "hard":
    game(1000)
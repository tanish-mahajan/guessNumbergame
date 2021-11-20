import random
print("Hello What's your name?")
name = input()
print("\nHello", name,",","Welcome to guess the number game...","\nGuess a number between 1 and 20\nYou will be getting 6 guesses only\nLet's Start!!")
secretNumber = random.randint(1, 20)


for guesstaken in range(1,7):
    print("Take a guess...")
    guess = int(input())
    if guess<secretNumber:
        print("Your guess is too low")
    elif guess>secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print("Congratulations!! You won the game")
else:
    print("YOU LOSE")

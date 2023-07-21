import random

x = int(input("Please, tell us a number maximum: "))

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
  
    while guess != random_number:
      guess = int(input(f"Guess a number beetwen 1 and {x}: "))
      
      if guess < random_number:
        print("Sorry, guess again too low")
      elif guess > random_number:
        print("Sorry, guess again too higth")
      
    print(f"Congratulation, you guess the number {random_number}")

guess(x)
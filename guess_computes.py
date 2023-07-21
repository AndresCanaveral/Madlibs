### gues number (computer)
import random

def guess_computer (x):
  print(f"Select a number between 1 and {x}: ")

  limit_i = 1
  limit_s = x
  
  answer = ''
  while answer != "c":
    # Generate predition
    if limit_i != limit_s:
      predition = random.randint(limit_i, limit_s) # Could also be the limit_s
    else:
      predition = limit_i
    answer = int(input(f"My predition is: {predition}. If you predition is higth say (A), if you predition is low say (B), but if you predition is Correct say (C)")).lower()

    if answer == 'a':
      limit_s = predition - 1
    elif answer == 'b':
      limit_i = predition + 1

  print(f"Congratulation, the computer guessed the number {predition}, correctly")
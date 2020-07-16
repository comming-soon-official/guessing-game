import random
import os

print("If you are Win your day Was Awesome")
print("Try Your Best buddy..!")
print("You Have 5 chance only.")
num = random.randint(1,10)

for _ in range(0,5):

  user_num = int(input("Guess Number B/W 1 to 10 : "))
  if user_num == num:
      print("You Are Win.!")
      break
  elif user_num > num:
      print("too high try again")
  elif user_num < num:
      print("too low try again")

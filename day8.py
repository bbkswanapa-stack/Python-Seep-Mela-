import random

# print(random.random())

# print(random.randint(1,10))

# a = ["hello","test","namaste","okay"]
# print(random.choice(a))

# print("--------------------------"*20)


# Random number guess question
# random_num = random.randint(10,20)
# print("this is random num",random_num)
# count = 0
# while True:
#    user_input = int(input("guess the no. between 10 to 20:"))
#    count += 1

#    if user_input == str(random_num):
#       print(f"Number Matched in {count} times")
#       play_again = input("Do you want to play again? (y/n): ").lower()
#       if play_again == "y":
#         random_num = random.randint(10,20)
#         count = 0
#       else:
#         print("Thanks for playing")
#         break
       
#    else:
#       print("Try Again!!")

guess_attempt = 5
random_num = random.randint(10,20)
print("this is random num",random_num)
count = 0
while (count < guess_attempt):
   user_input = int(input("guess the no. between 10 to 20:"))
   count += 1

   if user_input == random_num:
      print(f"Number Matched in {count} times, ")
      play_again = input("Do you want to play again? (y/n): ").lower()
      if play_again == "y":
        random_num = random.randint(10,20)
        count = 0
      else:
        print("Thanks for playing")
        break
       
   else:
      print("Try Again!!")



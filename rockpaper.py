import random

games_data = ["r", "p", "s"]
data = random.choice(games_data)
print(data)

while True:
    user_data = input("Enter , r , p , s:")
    if user_data not in games_data:
        print("invalid choice")
        continue
    print('correct input')

    if data == user_data:
        print ("Game Draw")

    elif (
        user_data == "r"
        and data == "s"
        or user_data == "s"
        and data == "p"
        or user_data == "p"
        and data == "r"
    ):
        print ("You won!!")
        break
    else:
        print("You lose!")
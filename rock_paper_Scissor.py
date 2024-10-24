import random
possible_action=["rock","paper","scissor"]
while True:
    player_action=input("Enter your choice (rock,paper,scissor):")
    comupter_action=random.choice(possible_action)
    print(f"your action {player_action} and computer action is {comupter_action}.\n")
    if player_action==comupter_action:
        print(f"Both of you choosed {player_action}. Its tie")
    elif player_action=="rock":
        if comupter_action=="scissor":
            print("rock smashed scissor You win!")
        else:
            print("paper cover rock You lose")
    elif player_action=="paper":
        if comupter_action=="rock":
            print("paper covers rock You win!")
        else:
            print("scissor cuts paper You lose")
    elif player_action=="scissor":
        if comupter_action=="paper":
            print("scissor cuts paper You win!")
        else:
            print("rock smashed scissor You lose")
    else:
        print("Invalid choice, Choose rock or paper or scissor ")

import os
def auction_winner (info) :
    winner_name=""
    winner_bid=0
    for i in info :
        if (info[i]>winner_bid) :
            winner_bid=info[i]
            winner_name=i
    return winner_name,winner_bid
def message():
    bidder=input("What's your name? ")
    bid=int(input("What is your bid? "))
    info[bidder]=bid
    choice=input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    yes_no(choice)
def yes_no(choice):
    if choice=='yes' :
        os.system("cls")
        message()
    elif choice=="no" :
        name,money=auction_winner(info)
        print(f"The winner is {name} with a bid of {money}.")
    else:
        print("Invalid input!Please try again")
info={}
message()

import random
def repeat():
  choice=input("Do you wanna continue ?(yes/no) : ").lower()
  if (choice=="yes") :
    return True
  elif (choice=="no") :
    return False
  else :
    print("Invalid choice!\nPlease re-enter your choice ")
    return repeat()
def user_choice_(options) :
  user_choice=input("\nEnter your choice : Rock,Paper,Scissors ?? : ").lower()
  if(user_choice in options ):
    return user_choice
  else :
    print("Invalid choice!\nPlease re-enter your choice ")
    return user_choice_(options)
options=["rock","paper","scissors"]
print("***\t\t\t\t\tWELCOME TO ROCK,PAPER,SCISSORS!!!\t\t\t\t\t***")
user_won=tot=comp_won=user_lost=0
continue_=True
while (continue_) :
  tot+=1
  print("\n"+"\t"*8+f"*ROUND {tot}*")
  comp_choice=random.choice(options)
  user_choice=user_choice_(options)
  print(f"Computer choose : {comp_choice}")
  if(comp_choice!=user_choice) :
    if( (comp_choice==options[0] and user_choice==options[2]) or (comp_choice==options[2] and user_choice==options[1]) or (comp_choice==options[1] and user_choice==options[0])) :
      print("\nYou lost !")
      user_lost+=1
      comp_won+=1
    else :
      print("\nYou won !!")
      user_won+=1
  elif(comp_choice==user_choice) :
    print(f"\nIt's a draw 🤝,Both chose {comp_choice}")
  print(f"\nSCORE           :  YOU - {user_won}       |  COMPUTER - {comp_won}")
  continue_=repeat()
winning_per=int(user_won*100/tot)
print("\n\n*****      GAME SUMMARY     *****")
print(f"Total rounds            : {tot} ")
print(f"Total rounds you won    : {user_won}")
print(f"Total rounds you lost   : {user_lost}")
print(f"Winning percentage      : {winning_per}%")
if(winning_per==100):
  print("UNDEFEATED 🔥")
elif(winning_per>=50) :
  print("Nice game!")
else :
  print("Comeback stronger 💪")

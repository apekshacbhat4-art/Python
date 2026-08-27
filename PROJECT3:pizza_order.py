#PIZZA ORDER PROGRAM
print("\t\t***PIZZA ORDER PROGRAM***\n")
print("\t\t\tMENU \n\n")
print("                     PIZZA                   |    AMOUNT ")
print("1) Small Pizza                               |    100 Rs")
print("2) Medium Pizza                              |    200 Rs")
print("3) Large Pizza                               |    300 Rs")
print("4) Pepperoni Pizza for Small Pizza           |    30 Rs")
print("5) Pepperoni Pizza for Medium /Large Pizza   |    50 Rs")
print("6) Extra Cheese for any size                 |    20 Rs")
choice,tot=1,0
while (choice):
  print("\n\n\n\nTaking order ......\n")
  print("Enter the size of pizza :\n1) Small \t2) Medium \t3) Large")
  size=int(input("Enter option- 1,2,3 : "))
  if (size == 1):
    tot+=100
  elif (size == 2):
    tot+=200
  elif (size == 3):
    tot+=300
  else:
    print("Error in choice")
    break
  is_pepperoni=input("\nDo you wanna add pepperoni ? (yes/no)")
  if (is_pepperoni.lower()=="yes"):
    if (size==1):
      tot+=30
    elif (size==2 or size==3):
      tot+=50
  is_cheese=input("\nDo you wanna add extra cheese ? (yes/no)")
  if(is_cheese.lower()=="yes"):
    tot+=20
  add_order=input("\nDo you wanna add anything to your order ? (yes/no)")
  if (add_order.lower()=="yes"):
    choice=1
  elif (add_order.lower()=="no"):
    choice=0
  else :
    print("\nError in choice")
    choice=0
  if (choice==0):
    final_choice=input("\nDo you wanna finalise your order ? (yes/no)")
    if (final_choice.lower()=="yes"):
      print("\nThank you for ordering!")
      print(f"\n\nYour final bill is {tot} Rs.")
      input("\nHow will you pay ? Cash or Card ? ")
      print("\n\nBill paying .......\n")
      is_rating=input("\nWould you like to rate our service and quality of our food ? (yes/no)")
      if (is_rating.lower()=="yes"):
        is_rating=float(input("\nEnter your rating out of 10 :"))
        if (is_rating >=7):
          print("\nThank you ... for your appreciation!!")
        elif (is_rating >=5 and is_rating<7):
          feedback=input("Would you like to give us some feedback so that we can improve ?")
          if (feedback.lower()=="yes"):
            input()
            print("Thank you for your feedback!")
          else:
            print("We will definetly try to improve !")
        elif (is_rating<5):
          print("Sorry for not meeting your expectations!!")
      print("\n\nThank you! Have a great day." )
    elif (final_choice.lower()=="no"):
      choice=1
    else :
      print("Error in choice")
      choice=0


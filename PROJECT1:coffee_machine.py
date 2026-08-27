import os
import time
import random
water = random.randint(1000,5000)
milk = random.randint(600,1300)
coffee = random.randint(200,600)
money = 0
def coffee_(choice) :
    coffee_items = { "espresso":
                         {"water" :50,
                          "milk" :0,
                          "coffee" : 18,
                          "money" :50} ,
                     "latte" :
                         {"water" :200,
                          "milk" :150,
                          "coffee" :24,
                          "money" :70},


                     "cappuccino" :
                         {"water" :250,
                          "milk" :100,
                          "coffee" : 24,
                          "money" :90
                         }
                   }
    global money
    global milk
    global water
    global coffee
    isorder=True
    os.system("cls")
    print("\t\t\t*** ORDER MENU ***")
    if milk < coffee_items[choice]["milk"] :
        print("Sorry there is not enough milk.")
        user_inputs()
    if water < coffee_items[choice]["water"] :
        print("Sorry there is not enough water.")
        user_inputs()
    if  coffee < coffee_items[choice]["coffee"] :
        print("Sorry there is not enough coffee.")
        user_inputs()
    print("\nPlease insert coins: ")
    five_rs=int(input("How many 5Rs. coins : "))
    ten_rs=int(input("How many 10Rs. coins : "))
    twenty_rs=int(input("How many 20Rs. coins : "))
    user_money= 5  * five_rs + 10  * ten_rs + 20  * twenty_rs
    milk-=coffee_items[choice]["milk"]
    water-=coffee_items[choice]["water"]
    coffee-=coffee_items[choice]["coffee"]
    if user_money == coffee_items[choice]["money"] :
        money+=user_money
    elif user_money > coffee_items[choice]["money"] :
        change = user_money - coffee_items[choice]["money"]
        money+=coffee_items[choice]["money"]
        print(f"Here is your Rs.{change} in change")
    else :
        print("Sorry that's not enough money. Money refunded.")
        user_inputs()
    print(f"Here is your {choice}.\nEnjoy!!")
    user_inputs()
def report() :
    print("\t\t*** REPORT ***")
    print(f"Water = {water}mL")
    print(f"Milk = {milk}mL")
    print(f"Coffee = {coffee}g")
    print(f"Money = Rs.{money}")
def user_inputs():
    print("\nWhat would you like to have ? espresso / latte / cappuccino\n\nYou can also type:\nreport → to see machine resources\noff → to turn off the machine\nmenu → to display menu card")
    choice=input().lower()
    if choice in ["espresso" ,"latte" ,"cappuccino"]:
        coffee_(choice)
    elif choice == "menu" :
        menu()
    elif choice == "report" :
        report()
    elif choice == "off" :
        print("Thank you for using the Coffee Machine. Have a great day!  ")
        exit()
    else :
        print("Invalid entry!")
    user_inputs()
def st_menu() :
    start=input("\nType 'menu' to view the menu card: ").lower()
    if start == "menu" :
        menu()
    print("Invalid entry!")
    st_menu()
def menu_order():
    time.sleep(10)
    ask=input("Would you like to order now? (yes/no) : ").lower()
    if ask=='yes' :
        os.system("cls")
        print("Great! Let's place your order. \n")
        user_inputs()
    elif ask=='no' :
        print("No problem Take your time.\nWe'll ask again shortly...")
        menu_order()
    else :
        print("Invalid entry!")
        menu_order()
def menu():
    os.system("cls")
    print("================= ☕  COFFEE MENU ☕ =================\n\nDrink         Water      Milk      Coffee      Price")
    print("----------------------------------------------------")
    print("Espresso      50 ml      0 ml      18 g        Rs.50")
    print("Latte         200 ml     150 ml    24 g        Rs.70")
    print("Cappuccino    250 ml     100 ml    24 g        Rs.90")
    print("----------------------------------------------------")
    print("\nPayment Mode:\nCoins accepted:")
    print("Rs.5   Rs.10   Rs.20")
    print("\nCommands:")
    print("menu   → Display menu card")
    print("report → Show machine resources")
    print("off    → Turn off the machine")
    print("====================================================")
    menu_order()
print("☕  Welcome to the Coffee Machine!\n\nThis machine can prepare:\n• Espresso\n• Latte\n• Cappuccino")
st_menu()

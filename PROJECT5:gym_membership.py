class gym :
    def __init__(self,name,type,month):
        self.name=name
        self.type=type
        self.month=month
        if self.month==0 :
            self.status="Expired"
        else :
            self.status="Active"
    def display(self):
        print(f"Name             : {self.name}")
        print(f"Membership       : {self.type}")
        print(f"Months Remaining : {self.month}")
        print(f"Status           : {self.status}")
        print("---------------------------------")
    def renew(self):
        if self.month==0:
            self.month+=int(input("Enter months to add : "))
            print(f"{self.name}'s membership renewed! Months remaining : {self.month}")
        else :
            print(f"{self.name}'s membership is still active!")
            print(f"Months remaining : {self.month}")
            print(f"Please renew after {self.month} months.")


n=int(input("Enter number of members : "))
members=list()
for i in range(n) :
    print(f"\n--- Member {i+1} ---")
    name=input("Enter name : ")
    type=input("Enter membership type (yearly/monthly) : ").lower()
    month=int(input("Enter months remaining : "))
    members.append(gym(name,type,month))
print("\n======= GYM MANAGEMENT =======")
print("1. Display all members")
print("2. Renew membership")
print("3. Check expired members")
print("4. Exit")
print("===============================")
choice =1
while choice in [1,2,3,4] :
    choice=int(input("\nEnter choice : "))
    if choice not in [1,2,3,4] :
        print("Invalid choice!")
        choice=1
    elif choice==1 :
        print()
        print("========== GYM MEMBERS ==========")
        for i in range (n) :
            print(i+1)
            members[i].display()
    elif choice == 2 :
        exist=0
        renew_name=input("Enter member name to renew : ")
        for m in members :
            if m.name == renew_name:
                exist=1
                m.renew()
                break
        if exist==0 :
            print("No such member exist in gym")
    elif choice == 3 :
        exp=0
        print("Expired members :")
        for i in range (n) :
            if members[i].month==0 :
                print(members[i].name)
                exp=1
        if exp==0:
            print("None! All members are active.")
    else :
        print("Thank you. Goodbye!")
        break

def ask(num) :
    ch= input(f"Enter 'y' to continue calculation with {num} or 'n' to start new calculation or 'x' to exit : ").lower()
    if ch not in ['n','y','x'] :
        print("Invalid choice!!")
        return ask(num)
    return ch
def operations (a,op) :
    if op == '+' :
        b = float(input(f"Enter next number to add with {a} : "))
        return b,a+b
    elif op == '-' :
        b = float(input(f"Enter next number to subtract with {a} : "))
        return b,a-b
    elif op == '*' :
        b = float(input(f"Enter next number to multiply with {a} : "))
        return b,a*b
    else :
        b = float(input(f"Enter next number to divide with {a} : "))
        if b!=0 :
            return b,a/b
        else :
            return False,False
def calc (choice , ans =0) :
    if choice == 'x' :
        return
    elif choice == 'n' :
        a = float(input("Enter first number : "))
        op = input("Pick one operation [ +,-,/,* ] : ")
        if op not in ['+','-','*','/'] :
            print("Invalid operator! ")
            return
        b , ans = operations(a,op)
        ans=round(ans,4)
        print(f"{a} {op} {b} = {ans}")
    else :
        op = input("Pick one operation [ +,-,/,*] : ")
        ans1=ans
        if op not in ['+','-','*','/'] :
            print("Invalid operator! ")
            return
        b ,ans  = operations(ans1,op)
        ans=round(ans,4)
        if b == ans and b== False :
            print("Error! cannot be divided by zero")
            return
        print(f"{ans1} {op} {b} = {ans}")
    choice= ask(ans)
    calc(choice,ans)
calc('n')

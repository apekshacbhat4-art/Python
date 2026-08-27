import time
import os
import random
nums = random.sample (range(1,100),5)

print("Memorize this:")
print(nums)

time.sleep(3)

# move cursor up and erase the numbers
os.system('cls')
print("Now type the numbers : ")
num=[]
for i in range (5) :
    num.append(int(input()))
if num==nums :
    print("You have GOOD memory!")
else :
    print("You have BAD memory!!")
    print(f"Actual numbers were :{nums}")

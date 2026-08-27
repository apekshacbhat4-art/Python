def binary_search(n,low,high,key) :
    if low>high :
        return False
    mid=(low+high)//2
    if key==n[mid]:
        return mid
    elif key>n[mid] :
        low=mid+1
    else:
        high=mid-1
    return binary_search(n,low,high,key)
n=list(map(int,input("Enter numbers : ").split()))
key=int(input("Enter key element : "))
n.sort()
print(f"Sorted list :{n}")
'''low,high=0,len(n)-1
while low<=high :
    mid=(low+high)//2
    if key==n[mid] :
        print(f"{key} element found at index {mid} in sorted list")
        break
    elif key > n[mid] :
        low=mid+1
    else :
        high=mid-1
else :
    print(f"{key} element not found in list")'''
value=binary_search(n,0,len(n)-1,key)
if value==False:
    print(f"{key} not found in sorted list")
else :
    print(f"{key} found at index {value} in sorted list")

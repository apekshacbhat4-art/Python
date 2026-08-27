n=[]
for i in range(6) :
    n.append(int(input()))
first_max=float('-inf')
second_max=float('-inf')
third_max=float('-inf')
for i in n:
    if (i!=first_max and i!=second_max and i!=third_max ):
        if (i>first_max) :
            third_max=second_max
            second_max=first_max
            first_max=i
        elif (first_max > i > second_max) :
            third_max=second_max
            second_max=i
        elif(first_max > i and second_max> i and third_max<i):
            third_max=i
if (third_max==float('-inf')) :
    print(first_max)
else:
    print(third_max)

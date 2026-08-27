def invert(n):
  if (n==False):
    return 1
  else:
    return 0
print("****TRUTH TABLE FOR LOGIC GATES FOR 2 INPUTS****\n")
c=1
while(c!=0):
  print("\nEnter the type of gate:\n1)Basic gates\t2)Universal gates\t3)Other gates\nSelect any option -1,2,3")
  type_gate=int(input())
  if(type_gate==1):
    gate=int(input("Enter the type of Basic gate:\n1)AND\t2)OR\t3)NOT\nSelect any option -1,2,3\n"))
    if(gate==1):
      print("A\t|B\t|Y=A.B")
      for i in range(0,2,1):
        for j in range(0,2,1):
          print(f"{i}\t|{j}\t|{i and j}")
    elif (gate==2):
      print("A\t|B\t|Y=A+B")
      for i in range(0,2,1):
        for j in range(0,2,1):
          print(f"{i}\t|{j}\t|{i or j}")
    elif (gate==3):
      print("A\t|Y=A'")
      for i in range (0,2,1):
        print(f"{i}\t|{invert(i)}")
  elif(type_gate==2):
    gate=int(input("Enter the type of Universal gate:\n1)NAND\t2)NOR\nSelect any option -1,2\n"))
    if(gate==1):
      print("A\t|B\t|Y=(A.B)'")
      for i in range (0,2,1):
        for j in range (0,2,1):
          print(f"{i}\t|{j}\t|{invert(i and j)}")
    elif(gate==2):
      print("A\t|B\t|Y=(A+B)'")
      for i in range (0,2,1):
        for j in range (0,2,1):
          print(f"{i}\t|{j}\t|{invert(i or j)}")
  elif(type_gate==3):
    gate=int(input("Enter the type of Other gates:\n1)XOR\t2)X-NOR\nSelect any option -1,2\n"))
    if(gate==1):
      print("A\t|B\t|Y=A⊕B")
      for i in range (0,2,1):
        for j in range (0,2,1):
          print(f"{i}\t|{j}\t|{(i and (invert(j)))or((invert(i) and j))}")
    elif(gate==2):
      print("A\t|B\t|Y=A⊙B")
      for i in range (0,2,1):
        for j in range (0,2,1):
          print(f"{i}\t|{j}\t|{(invert(i) and invert(j)) or (i and j)}")
  c=int(input("Do you want to continue?"))

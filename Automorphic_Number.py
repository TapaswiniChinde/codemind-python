num=int(input())
flag=0
square=num*num
while num>0:
    if num%10!=square%10:
        print("Not an Automorphic Number")
        flag=1
        break
    num=num//10
    square=square//10
if(flag==0):
    print("Automorphic Number")
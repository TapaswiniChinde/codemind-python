n=int(input())
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end="");
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(1,n+1):
        if j==n:
            print("0",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
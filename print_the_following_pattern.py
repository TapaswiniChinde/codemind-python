n=int(input())
for i in range(1,n+1):
    for j in range(1,n-1):
        print(j,end="")
    for j in range(n-2,1,-1):
        print(j-1,end="")
    print()
n= int(input())
A=[]

for i in range(n):
    temp=[]
    for j in range(n):
        inp=input()
        dist=0
        if inp == "INF":
            dist=float('inf')
        else:
            dist=int(inp)
        temp.append(dist)
    A.append(temp)
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j]=min(A[i][j], A[i][k]+A[k][j])
    print('A{} = {}'.format(k, A))

print('final A: {}'.format(A))
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

print()
for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j]=min(A[i][j], A[i][k]+A[k][j])
    print(f'A{k}\n-----------')
    for i in A:
        print("\t".join(str(l) for l in i))
    print()

print('final A:\n-----------')
for i in A:
    print("\t".join(str(l) for l in i))
print()

"""
4
0
5
INF
INF
0
3
INF
INF
INF
0
1
INF
INF
INF
0
10
"""
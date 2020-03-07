A=[[1,3,4],
   [3,6,7],
   [3,8,9]]
for i in range(len(A)):
    print(A[i])
print("\n matrix B:")
B=[[1,2,3],
   [4,6,7],
   [7,7,9]]

for j in range(len(B)):
    print(B[j])

result=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
print("\result matrix A*B=c:")
for r in result:
    print(r)
    

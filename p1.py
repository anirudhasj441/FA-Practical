A=[[2,3,4],
   [6,7,8],
   [5,4,3]]
for i in range(len(A)):
    print(A[i])
print("\n matrix B:")
B=[[3,2,3],
   [4,6,7],
   [7,8,9]]
for j in range(len(B)):
    print(B[j])
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0 ])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
print("\result matrix A*B=c:")
for r in result:
    print(r)

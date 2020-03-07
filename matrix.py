A=[[2,1,4],
   [1,5,2],
   [1,1,1]]
for i in range(len(A)):
    print(A[i])
print("\n matrix B:")
B=[[3,2,1],
   [2,2,2],
   [1,2,1]]
for j in range(len(B)):
    print(B[j])
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
print("\n result matrix A*B=c")
for r in result:
    print(r)
    

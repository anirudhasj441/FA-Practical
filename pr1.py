A=[[6,9,1],
   [9,5,7],
   [7,8,9]]
for i in range(len(A)):
    print(A[i])
print("\n matrix B:")
B=[[5,8,9,2],
   [6,7,3,3],
   [7,5,9,1]]
for j in range(len(B)):
    print(B[j])
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
print("\n result matrix A*B=c:")
for r in result:
    print(r)
  

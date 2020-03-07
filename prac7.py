def Largest(L):
     global pairs
     if len(L)==1:
          return L[0]
     else:
          left=Largest(L[:len(L)//2])
          right=Largest(L[len(L)//2:])
          pairs.append((left,right))
          return max(left,right)
def second_largest(L):
     global pairs
     biggest=Largest(L)
     second_L=[min(item)for item in pairs if biggest in item]
     return biggest,Largest(second_L)
if __name__=="__main__":
     pairs=[]
     L=[2,-2,10,4,3,2,-98,432,53,90]
     if len(L)==0:
          first,second=None,None
     elif len(L)==1:
          first,second=L[0],None
     else:
          first,second=second_largest(L)
print("The Largest Number"+str(first))
print("The Second Largest Number"+str(second))

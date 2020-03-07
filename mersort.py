def quickSort(mylist):
    QuickSort(mylist,0,len(mylist)-1)
def QuickSort(mylist,i,j):
    if i<j:
        q=partition(mylist,i,j)
        QuickSort(mylist,i,q-1)
        QuickSort(mylist,q+1,j)
def partition(mylist,i,j):
    pivotelement=mylist[i]
    leftvalue=i+1
    rightvalue=j
    done=False
    while not done:
        while leftvalue<=rightvalue and mylist[leftvalue]<=pivotelement:
            leftvalue=leftvalue+1
        while mylist[rightvalue]>=pivotelement and rightvalue>=leftvalue:
            rightvalue=rightvalue-1
        if rightvalue<leftvalue:
            done=True
        else:
            temp=mylist[leftvalue]
            mylist[leftvalue]=mylist[rightvalue]
            mylist[rightvalue]=temp
    temp=mylist[i]
    mylist[i]=mylist[rightvalue]
    mylist[rightvalue]=temp
    return rightvalue
mylist=[13,8,2,45,67,89,97]
print("Before applying quicksort technique:",mylist)
quickSort(mylist)
print("After applying quicksort technique:",mylist)







    

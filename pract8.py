a = [84,25,32,12,44]
print("Array A",a)
for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[min_index]>a[j]:
            min_index = j
    a[i],a[min_index]=a[min_index],a[i]
    print('iteration %d'% (i+1))
    print(a)
print('smaller no %d'%a[0])
print('greater no %d'%a[len(a)-1])

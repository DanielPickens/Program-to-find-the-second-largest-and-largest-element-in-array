##finds second largest element in an array
list1 = [1, 2, 4, 5, 6, 7]
mx=max(list1[0], list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx  ## this locates or points to the second highest value element
        mx=list1[i] #points to largest element in arr
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]
print("second highest number is : ",\
      str(secondmax))



#finds largest element in array
list1 = [1, 2, 4, 5, 6, 7]
mx=max(list1[0], list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx  ## this locates or points to the second highest value element
        mx=list1[i] #points to largest element in arr
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]
print("second highest number is : ",\
      str(mx))

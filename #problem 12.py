#problem 12

#print a number without string
list1 = [] 
for i in range(5):
    number = str(input("enter the number = "))
    list1.append(number)
    
print(list1)

#solution
for i in range(len((list1))):
    print(int(list1[i]))
    

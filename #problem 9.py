#problem 9

N = int(input("enter the length of the list = "))

list_ = []
for i in range(N):
    number = int(input("enter the number = ")) 
    list_.append(number)
    
print(list_)
set_ = []
for i in list_:
    if i not in set_:
        set_.append(i)
        
print(set_)

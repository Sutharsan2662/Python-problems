#problem 7

#X pattern printing 

N = str(input('enter the number = '))

nums = len(N)

list_ = list(N)

print(list_)

for i in range(len(list_)):
    for j in range(len(list_)):
        if (i == j or j == nums - 1 - i):
            print(list_[j], end=" ")
        else:
            print(end=" ")
    print() 
            
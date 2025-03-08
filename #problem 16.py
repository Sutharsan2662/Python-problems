#problem 16


#evaluating quadratic equation 

#taking the coefficents as the inputs

N = int(input("enter the degree of the polynomial = "))



a = int(input("enter the coefficent of a = "))
b = int(input("enter the coefficent of b = "))
c = int(input("enter the coefficent of c = "))
    


#formula -b+-root over b**2 - 4ac/2a
import math
 #determinant 
 
d = b*b - 4*a*c

if d > 0:
    
    x1 = (-1*b + math.sqrt(d))/(2*a)
    x2 = (-1*b - math.sqrt(d))/(2*a)
    print("the roots of the equation is = "+ str(x1) + "and" + str(x2)) 
    
elif d == 0:
    x1 = (-1*b)/(2*a)
    print("the roots of the equation is = "+ str(x1)) 
else:
    real = (-1*b)/(2*a)
    img = (1*math.sqrt(-1*d))/2*a
    if img > 0:
        print("the roots of the equation is = "+ str(real) + " +i" + str(img) + " and " + str(real) + " -i" + str(img)) 
    else:
         print("the roots of the equation is = "+ str(real) + " -i" + str(-1*img) + " and " + str(real) + " +i" + str(-1*img)) 
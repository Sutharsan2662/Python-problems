#problem 17

#area in between two concentric circle

#area of inner circle 

R1 = float(input("enter the radius of the inner circle = "))
import math
A1 = lambda R1:math.pi*R1**2


#area of outer circle 

R2 = float(input("enter the radius of the outer circle = "))

A2 = lambda R2:math.pi*R2**2

print("the area inbetween the concentric cirsle is = "+str(A2(R2)-A1(R1)))
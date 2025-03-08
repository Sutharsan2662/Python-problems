#problem 13 
import math
#find the area of the ssquare
length = int(input("enter the length in meters = "))
breadth = int(input("enter the breadth in meters = "))

square = lambda length:length**2

print("area of the square = "+str(square(length)))

#find the area of rectangle

rect = lambda length,breadth: length*breadth

print("area of the rectangle = "+str(rect(length,breadth)))

#find the area of cylinder:
radius = float(input("enter the radius of cylinder in meters "))
height = float(input("enter the height of cylinder in meters = "))
cyl = lambda radius,height:2*math.pi*radius*height+2*math.pi*radius**2 

print(cyl(radius,height))
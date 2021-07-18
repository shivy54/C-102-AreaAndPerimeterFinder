import math
print("Welcome to the area finder program")
print("Choose shape")
print("1:Rectangle")
print("2:Square")
print("3:Triangle")
print("4:Circle")
print()
shape = input("Which shape? ")
print()
print("Area or Perimeter??")
print("The circumference of a circle is the perimeter of the circle")
print("1:Area")
print("2:Perimeter")
print()
func = input("Area or perimeter? ")

if func == "1":
    if shape == "1":
        length = float(input("Enter the length:- "))
        breadth = float(input("Enter the breadth:- "))
        area = length * breadth
        print("The area of the rectangle is "+str(area))
    elif shape == "2":
        length = float(input("Enter the length:- "))
        breadth = float(input("Enter the breadth:- "))
        area = length * breadth
        print("The area of the square is "+str(area))
    elif shape == "3":
        height = float(input("Enter the height "))
        base = float(input("Enter the base "))
        area = (height * base) / 2
        print("The area of the triangle is "+str(area))
        
    elif shape == "4":
        r = float(input("Enter the circles radius:- "))
        pi = math.pi
        rr = r*r
        area = pi*rr
        print("The area of the circle is "+str(area))
    else:
        print("please choose one of the given shapes")



elif func == "2":
    if shape == "1":
        length = float(input("Enter the length "))
        breadth = float(input("Enter the breadth "))
        perimeter = (length + breadth) * 2
        print("the perimeter of the rectangle is " + str(perimeter))
    elif shape == "2":
        side = float(input("Enter the size of one side "))
        perimeter = 4*side
        print("the perimeter of the square is " + str(perimeter))
    elif shape == "3":
        Rside = input("Enter the length of the triangle's right side:- ")
        Lside = input("Enter the length of the triangle's left side:- ")
        Base = input("Enter the length of the triangle's base:- ")
        peri = Rside + Lside + Base
        print("The perimeter of the triangle is " + peri)
    elif shape == "4":
        r = float(input("Enter the circles radius:- "))
        pi = math.pi
        t = 2
        C = t * pi * r
        print("The circumference/perimeter of the circle is " + str(C))
    else:
        print("please choose one of the given shapes")
'''
print("Welcome to the area perimeter finder program")
print("Choose shape")
print("1 for Rectangle/Square")
print("2 for Triangle")
print("3 for perimeter of Rectangle/Square")
print("4 for a")

shape = int(input("Enter 1 or 2 or 3 for shape "))
length = float(input("Enter the length "))
breadth = float(input("Enter the breadth "))
area = ''
if shape == 1:
    length = float(input("Enter the length "))
    breadth = float(input("Enter the breadth "))
    area = length * breadth
    print(area)
elif shape == 2:
    length = float(input("Enter the height "))
    breadth = float(input("Enter the base "))
    area = (length * breadth)/2
    print(area)
else:
    length = float(input("Enter the length "))
    breadth = float(input("Enter the breadth "))
    perimeter = (length + breadth) * 2
    print(perimeter)
'''
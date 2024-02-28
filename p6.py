import math
s1=int(input("Enter side1 of a triangle:"))
s2=int(input("Enter Side2 of a triangle:"))
s3=int(input("Enter Side3 of a triangle:"))
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)(s-s2)(s-s3))
print("area of a triangle is",area)

a= int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

import math
e = math.sqrt((b**2)-(4*a*c))

x1 = (-b+e)/(2*a)
x2 = (-b-e)/(2*a)

print("The roots of x are:", x1,"and", x2)

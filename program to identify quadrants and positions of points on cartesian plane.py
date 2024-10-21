x = float(input("Enter x-coordinate:  "))
y = float(input("Enter y-coordinate:  "))

if x>0 and y>0:
    print("The point lies in Quadrant 1")
elif x<0 and y>0:
    print("The point lies in Quadrant 2")
elif x>0 and y>0:
    print("The point lies in quadrant 3")
else:
    print("The point lies in quadrant 4")


if y==0:
    print("The point lies on x-axis")
elif x==0:
    print("The point lies on y-axis")
elif x==0 and y==0:
    print("The point lies at the origin")



import calculate

length = float(input("Enter the length of rectangle: "))
width = float (input("Enter width of the ractangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

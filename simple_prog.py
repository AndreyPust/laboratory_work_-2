import math  # for sqrt

print("Enter the sides of the rectangle")
length = int(input("Enter the length of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))

# defining a rectangle:

if length > width:
    print("Length is greater than width")
    name_rectangle = "rectangle"
elif length < width:
    print("Length is less than width")
    name_rectangle = "rectangle"
else:
    print("The length is equal to the width, this rectangle is a square!")
    name_rectangle = "square"

perimeter_rectangle = (length + width) * 2  # perimeter search
print("Perimeter ", name_rectangle, " = ", perimeter_rectangle)

square_rectangle = length * width  # area search
print("Square ", name_rectangle, " = ", square_rectangle)

diagonal_main = math.sqrt(length * length + width * width)  # diagonal search
print("Diagonal ", name_rectangle, " = ", diagonal_main)

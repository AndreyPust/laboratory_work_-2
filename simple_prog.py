import math

print("Введите стороны прямоугольника")
length = int(input("Введите длину прямоугольника:"))
width = int(input("Введите ширину прямоугольника:"))
if length > width:
    print("Длина больше ширины")
    name_rectangle = "прямоугольника"
elif length < width:
    print("Длина меньше ширины")
    name_rectangle = "прямоугольника"
else:
    print("Длина равна ширине, данный прямоугольник является квадратом!")
    name_rectangle = "квадрата"
perimeter_rectangle = (length + width)*2
print("Периметр ", name_rectangle, "=", perimeter_rectangle)
square_rectangle = length*width
print("Площадь ", name_rectangle, "=", square_rectangle)
diagonal_main = math.sqrt(length*length + width*width)
print("Диагональ ", name_rectangle, "=", diagonal_main)

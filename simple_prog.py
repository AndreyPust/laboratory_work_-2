import math #for sqrt


print("Введите стороны прямоугольника")
length = int(input("Введите длину прямоугольника:"))
width = int(input("Введите ширину прямоугольника:")) #enter sides

#defining a rectangle

if length > width:
    print("Длина больше ширины")
    name_rectangle = "прямоугольника"
elif length < width:
    print("Длина меньше ширины")
    name_rectangle = "прямоугольника"
else:
    print("Длина равна ширине, данный прямоугольник является квадратом!")
    name_rectangle = "квадрата"

perimeter_rectangle = (length + width)*2 #perimeter search
print("Периметр ", name_rectangle, "=", perimeter_rectangle)

square_rectangle = length*width #area search
print("Площадь ", name_rectangle, "=", square_rectangle)

diagonal_main = math.sqrt(length*length + width*width) #diagonal search
print("Диагональ ", name_rectangle, "=", diagonal_main)

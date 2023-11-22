print("Введите стороны прямоугольника:")
length = input("Введите длину прямоугольника:")
width = input("Введите ширину прямоугольника:")
if length > width:
    print("Длина больше ширины")
    name_rectangle = "прямоугольник"
elif length < width:
    print("Длина меньше ширины")
    name_rectangle = "прямоугольник"
else:
    print("Длина равна ширине, данный прямоугольник является квадратом!")
    name_rectangle = "квадрат"

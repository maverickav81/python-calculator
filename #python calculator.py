#python area calculator
import math
while True:
    print("Which shape? \n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")
    shape =int(input("Choose the shape(1 to 5): "))
    #Rectangle
    if shape == 1:
        height =float(input("Enter the Height: "))
        base =float(input("Enter the base: "))
        area = (height * base) / 2
        print(f"Triangle area:{area}")
    #Reactangle
    elif shape == 2:
        length =float(input("Enter the Lenth: "))
        width =float(input("Enter the width: "))
        area = length * width
        print(f"Rectangle area:{area}")
    #Square 
    elif shape == 3:
        side =float(input("Enter side value: "))
        area = side ** 2
        print(f"{area} = Square area")
    #Circle
    elif shape == 4:
        radius =float(input("Enter Radius: "))
        area = math.pi * radius ** 2
        print(f"{area} = Radius area")
    elif shape == 5:
        print("***Goodbye***")
        break
    else:
        print(f"{shape} = Wrong shap you choosed")

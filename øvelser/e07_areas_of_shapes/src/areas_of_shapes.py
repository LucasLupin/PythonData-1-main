def calculate_area(shape):
    if shape == "triangle":
        base = float(input("Give base of the triangle: "))
        height = float(input("Give height of the triangle: "))
        area = 0.5 * base * height

    elif shape == "rectangle":
        length = float(input("Give length of the rectangle: "))
        width = float(input("Give width of the rectangle: "))
        area = length * width

    elif shape == "circle":
        radius = float(input("Give radius of the circle: "))
        area = 3.14159 * radius ** 2

    else:
        print("Unknown shape!")
        return

    print(f"The area is {area:.6f}")

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        calculate_area(shape)

if __name__ == "__main__":
    main()

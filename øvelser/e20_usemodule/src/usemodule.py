#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    a, b = 3, 4
    print("Hypothenuse: ", triangle.hypothenuse(a, b))
    print("Area: ", triangle.area(a, b))

if __name__ == "__main__":
    main()

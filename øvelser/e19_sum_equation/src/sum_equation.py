#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    else:
        result = " + ".join(map(str, L)) + " = " + str(sum(L))
        return result

def main():
    print(sum_equation([1, 5, 7]))

if __name__ == "__main__":
    main()


#!/usr/bin/env python3

def triple(x):
    return x * 3

def square(i):
    return i ** 2

def main():
    for i in range(1, 11):
        j = triple(i)
        h = square(i)

        if h > j:
            break

        print(f"triple({i})=={j} square({i})=={h}")

if __name__ == "__main__":
    main()


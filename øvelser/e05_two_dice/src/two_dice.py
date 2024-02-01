#!/usr/bin/env python3

def main():
    for x in range (1, 7):
        for j in range(1, 7):
            pair = x + j

            if (pair == 5): 
                print(f"({x}, {j})")

if __name__ == "__main__":
    main()

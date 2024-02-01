#!/usr/bin/env python3

def detect_ranges(L):
    if not L:  # Tjekker om listen er tom
        return []

    sorted_L = sorted(L)
    result = []
    start = sorted_L[0]
    end = start
    
    for number in sorted_L[1:] + [None]:
        if number == end + 1:
            end = number
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1))
            if number is not None:
                start = number
                end = number

    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

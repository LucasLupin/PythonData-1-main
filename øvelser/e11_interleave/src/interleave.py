#!/usr/bin/env python3

def interleave(*lists):
    NewList = zip(*lists)
    result = []

    for t in NewList:
        for v in t:
            result.append(v)

    return result




def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

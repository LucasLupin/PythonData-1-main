#!/usr/bin/env python3

def transform(s1, s2):

    list1 = list(map(int, s1.split()))
    list2 = list(map(int, s2.split()))

    zippedList = list(zip(list1,list2))
    multipliedList = [a*b for a,b in zippedList]
    print(multipliedList)

    return multipliedList




def main():
    pass

if __name__ == "__main__":
    main()
    transform("1 5 3", "2 6 -1")
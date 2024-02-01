#!/usr/bin/env python3

def positive_list(L):

    #posetiveList = [(l) for l in L if (l > 0)] 
    def is_positive(x):
        return x > 0

    # Filter out negative numbers and zero
    return list(filter(is_positive, L))
    

def main():
    print(positive_list([2, -2, 0, 1, -7]))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def merge(L1, L2):
    i, j = 0, 0
    merged_list = []

    # Loop until one list is exhausted
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1

    while i < len(L1):
        merged_list.append(L1[i])
        i += 1

    while j < len(L2):
        merged_list.append(L2[j])
        j += 1

    return merged_list

def main():
    PreList1 = [5, 3, 7, 1]
    PreList2 = [7, 12, 8, 2, 4]

    L1 = sorted(PreList1)
    L2 = sorted(PreList2)

    merged = merge(L1, L2)
    print(merged)

if __name__ == "__main__":
    main()

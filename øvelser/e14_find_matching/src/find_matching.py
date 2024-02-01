#!/usr/bin/env python3

def find_matching(string, matching_str):
    matching_index = []
    
    for index,string in enumerate(string):
        if matching_str in string:
            matching_index.append(index)
    return matching_index

def main():
    pass

if __name__ == "__main__":
    main()
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(result)

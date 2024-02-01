#!/usr/bin/env python3

import re


def file_listing(filename=r"C:\Users\lukr\Desktop\H3\Python\PythonData-1-main\øvelser\e22_file_listing\src\listing.txt"):
    pattern = r'\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)'
    result = []

    #\s+ matches one or more whitespace characters.
    #(\d+) captures a group of one or more digits (file size).
    #(\w+) captures a word character group (month).
    #(\d+) captures the day.
    #(\d+):(\d+) captures the hour and minute.
    #(.+) captures the remaining part of the line, which is the filename.

    with open(filename, "r") as file: 
        for line in file:
            match = re.search(pattern,line)
            if match:
                size, month, day, hour, minute, name = match.groups()
                result.append((int(size), month, int(day), int(hour), int(minute), name))

    print(result)
    return result

def main():
    file_listing()

if __name__ == "__main__":
    main()

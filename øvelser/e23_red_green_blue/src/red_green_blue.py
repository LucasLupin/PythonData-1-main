#!/usr/bin/env python3

import re

def red_green_blue(filename=r"C:\Users\lukr\Desktop\H3\Python\PythonData-1-main\øvelser\e23_red_green_blue\src\rgb.txt"):
    pattern = r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+)'
    result = []
    line_count = 0

    #\s+ matches one or more whitespace characters.
    #(\d+) captures a group of one or more digits (file size).
    #(\w+) captures a word character group (month).
    #(\d+) captures the day.
    #(\d+):(\d+) captures the hour and minute.
    #(.+) captures the remaining part of the line, which is the filename.

    with open(filename, "r") as file:
        next(file)
        for line in file:
            match = re.search(pattern,line)
            if match:
                red,green,blue,name = match.groups()
                result.append(f'{red}\t{green}\t{blue}\t{name}')
                line_count += 1

    print(f'Processed {line_count} lines.')

    print(result)
    return result


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
    
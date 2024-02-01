#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    pattern = r'\[\s*([+-]?\d+)\s*\]'

    FilteredList = [int(num) for num in re.findall(pattern,s)]
    #\[ and \] match the literal square brackets.
    #\s* matches zero or more whitespace characters.
    #[+-]? optionally matches either a + or - sign.
    #\d+ matches one or more digits.

    return FilteredList

def main():
    test_string = "afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(test_string))

if __name__ == "__main__":
    main()

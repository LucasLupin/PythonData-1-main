# Øvelser

## et par links...

- [Laurent Pointal's fantastisk kompakte cheatsheet](#%20oplæg%20uge.md<https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf>)
- [Verdens længste cheatsheet](<https://websitesetup.org/wp-content/uploads/2020/04/Python-Cheat-Sheet.png>)
- <https://assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf>
- <https://github.com/pandas-dev/pandas/blob/main/doc/cheatsheet/Pandas_Cheat_Sheet.pdf>
- <http://datacamp-community-prod.s3.amazonaws.com/e1a8f39d-71ad-4d13-9a6b-618fe1b8c9e9>

TOC

- [Øvelser](#øvelser)
  - [et par links...](#et-par-links)
- [\[Part 01\]](#part-01)
- [Basics](#basics)
      - [Øvelse 1 (hej verden)](#øvelse-1-hej-verden)
      - [Øvelse 2 (kompliment)](#øvelse-2-kompliment)
  - [variabler](#variabler)
      - [Øvelse 3 (multiplikation)](#øvelse-3-multiplikation)
  - [Datatyper](#datatyper)
  - [Forgreninger](#forgreninger)
      - [Exercise 4 (multiplication table)](#exercise-4-multiplication-table)
      - [Exercise 5 (two dice)](#exercise-5-two-dice)
  - [Functions](#functions)
      - [Exercise 6 (triple square)](#exercise-6-triple-square)
        - [Part 1](#part-1)
        - [Part 2](#part-2)
      - [Exercise 7 (areas of shapes)](#exercise-7-areas-of-shapes)
  - [Datastrukturer](#datastrukturer)
      - [Exercise 8 (solve quadratic)](#exercise-8-solve-quadratic)
      - [Exercise 9 (merge)](#exercise-9-merge)
      - [Exercise 10 (detect ranges)](#exercise-10-detect-ranges)
      - [Exercise 11 (interleave)](#exercise-11-interleave)
      - [Exercise 12 (distinct characters)](#exercise-12-distinct-characters)
      - [Exercise 13 (reverse dictionary)](#exercise-13-reverse-dictionary)
      - [Exercise 14 (find matching)](#exercise-14-find-matching)
      - [Exercise 15 (two dice comprehension)](#exercise-15-two-dice-comprehension)
      - [Exercise 16 (transform)](#exercise-16-transform)
      - [Exercise 17 (positive list)](#exercise-17-positive-list)
  - [String handling](#string-handling)
      - [Exercise 18 (acronyms)](#exercise-18-acronyms)
      - [Exercise 19 (sum equation)](#exercise-19-sum-equation)
  - [Moduler](#moduler)
      - [Exercise 20 (usemodule)](#exercise-20-usemodule)
  - [RegEx](#regex)
- [\[Part02\]](#part02)
      - [Exercise 21 (integers in brackets)](#exercise-21-integers-in-brackets)
      - [Exercise 22 (file listing)](#exercise-22-file-listing)
      - [Exercise 23 (red green blue)](#exercise-23-red-green-blue)
      - [Exercise 24 (word frequencies)](#exercise-24-word-frequencies)
      - [Exercise 25 (summary)](#exercise-25-summary)
      - [Exercise 26 (file count)](#exercise-26-file-count)
      - [Exercise 27 (file extensions)](#exercise-27-file-extensions)
  - [Læs (og skriv, i) filer](#læs-og-skriv-i-filer)
  - [RegEx](#regex-1)
  - [Objekter](#objekter)
      - [Exercise 28 (prepend)](#exercise-28-prepend)
      - [Exercise 29 (rational)](#exercise-29-rational)
  - [Undtagelser (Exceptions)](#undtagelser-exceptions)
      - [Exercise 30 (extract numbers)](#exercise-30-extract-numbers)
- [Numpy](#numpy)
      - [Exercise 31 (rows and columns)](#exercise-31-rows-and-columns)
      - [Exercise 32 (row and column vectors)](#exercise-32-row-and-column-vectors)
      - [Exercise 33 (diamond)](#exercise-33-diamond)
      - [Exercise 34 (vector lengths)](#exercise-34-vector-lengths)
      - [Exercise 35 (vector angles)](#exercise-35-vector-angles)
  - [Test your solution in the main program.](#test-your-solution-in-the-main-program)
- [\[Part03\]](#part03)
- [NumPy (continues) \[`numpy2.ipynb`\]](#numpy-continues-numpy2ipynb)
      - [Exercise 37 (column comparison)](#exercise-37-column-comparison)
      - [Exercise 38 (first half second half)](#exercise-38-first-half-second-half)
      - [Exercise 39 (most frequent first)](#exercise-39-most-frequent-first)
      - [Exercise 40 (matrix power)](#exercise-40-matrix-power)
      - [Exercise 41 (correlation)](#exercise-41-correlation)
      - [Exercise 42 (meeting lines)](#exercise-42-meeting-lines)
      - [Exercise 43 (meeting planes)](#exercise-43-meeting-planes)
      - [Exercise 44 (almost meeting lines)](#exercise-44-almost-meeting-lines)
- [MatPlotLib](#matplotlib)
      - [Exercise 45 (multiple graphs)](#exercise-45-multiple-graphs)
      - [Exercise 46 (subfigures)](#exercise-46-subfigures)
- [Image processing](#image-processing)
      - [Exercise 47 (to grayscale)](#exercise-47-to-grayscale)
        - [Part 1.](#part-1-1)
        - [Part 2.](#part-2-1)
      - [Exercise 48 (radial fade)](#exercise-48-radial-fade)
        - [Part1.](#part1)
        - [Part 2.](#part-2-2)
- [Pandas](#pandas)
      - [Exercise 49 (read series)](#exercise-49-read-series)
      - [Exercise 50 (operations on series)](#exercise-50-operations-on-series)
      - [Exercise 51 (inverse series)](#exercise-51-inverse-series)
  - [What happens if some value appears multiple times in the original Series? What happens if you use this value to index the resulting Series?](#what-happens-if-some-value-appears-multiple-times-in-the-original-series-what-happens-if-you-use-this-value-to-index-the-resulting-series)
- [\[ PART 3 \]](#-part-3-)
      - [Exercise 52 (cities)](#exercise-52-cities)
      - [Exercise 53 (powers of series)](#exercise-53-powers-of-series)
      - [Exercise 54 (municipal information)](#exercise-54-municipal-information)
  - [Note, sometimes file ending `tsv` (tab separated values) is used instead of `csv` if the separator is a tab.](#note-sometimes-file-ending-tsv-tab-separated-values-is-used-instead-of-csv-if-the-separator-is-a-tab)
      - [Exercise 55 (municipalities of finland)](#exercise-55-municipalities-of-finland)
  - [Test your function from the `main` function.](#test-your-function-from-the-main-function)
      - [Exercise 56 (swedish and foreigners)](#exercise-56-swedish-and-foreigners)
      - [Exercise 57 (growing municipalities)](#exercise-57-growing-municipalities)
      - [Exercise 58 (subsetting with loc)](#exercise-58-subsetting-with-loc)
      - [Exercise 59 (subsetting by positions)](#exercise-59-subsetting-by-positions)
      - [Exercise 60 (snow depth)](#exercise-60-snow-depth)
      - [Exercise 61 (average temperature)](#exercise-61-average-temperature)
      - [Exercise 62 (below zero)](#exercise-62-below-zero)
      - [Exercise 63 (cyclists)](#exercise-63-cyclists)
      - [Exercise 64 (missing value types)](#exercise-64-missing-value-types)
      - [Exercise 65 (special missing values)](#exercise-65-special-missing-values)
      - [Exercise 66 (last week)](#exercise-66-last-week)
      - [Exercise 67 (split date)](#exercise-67-split-date)

      - [Exercise 68 (cleaning data)](#exercise-68-cleaning-data)
      - [Exercise 69 (cycling weather)](#exercise-69-cycling-weather)
      - [Exercise 70 (top bands)](#exercise-70-top-bands)
      - [Exercise 71 (cyclists per day)](#exercise-71-cyclists-per-day)
      - [Exercise 72 (best record company)](#exercise-72-best-record-company)
      - [Exercise 73 (suicide fractions)](#exercise-73-suicide-fractions)
      - [Exercise 74 (suicide weather)](#exercise-74-suicide-weather)
      - [Exercise 75 (bicycle timeseries)](#exercise-75-bicycle-timeseries)
      - [Exercise 76 (commute)](#exercise-76-commute)

# [Part 01]

# Basics

#### Øvelse 1 (hej verden)
Øvelsen har en skabelon-fil eller en "stub". Den ligger i mappen `exercises/part01/e01_hello_world`
Udfyld det manglende stykke i løsnings-stub-filen `hello_world.py` i undermappen `src` og få den til at udskrive følgende:

`Hello, world!`

Sørg for at bruge korrekt indrykning. Du kan køre det med kommando `python src/hello_world.py`. Hvis output ser godt ud, kan du teste det med kommando `python -m tmc`. ~~Hvis testene virker, skal du indsende din løsning til serveren med kommando  `tmc submit`~~.

---


#### Øvelse 2 (kompliment)
Udfyld stub-løsningen for at få programmet til at fungere som følger:  
Programmet skal bede brugeren om et input, og udskrive et svar som eksemplerne herunder viser.

```
What country are you from? Sweden
I have heard that Sweden is a beautiful country.

What country are you from? Chile  
I have heard that Chile is a beautiful country.
```


## variabler

#### Øvelse 3 (multiplikation) 

Lav et program, der giver følgende output.  
Du skal bruge et for-loop i din løsning.

```python
4 multiplied by 0 is 0
4 multiplied by 1 is 4
4 multiplied by 2 is 8
4 multiplied by 3 is 12
4 multiplied by 4 is 16
4 multiplied by 5 is 20
4 multiplied by 6 is 24
4 multiplied by 7 is 28
4 multiplied by 8 is 32
4 multiplied by 9 is 36
4 multiplied by 10 is 40
```

---


## Datatyper

## Forgreninger 

* loops, 
* betingede valg (if/else)

#### Exercise 4 (multiplication table)

In the `main` function print a multiplication table, which is shown below:
```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
```
For example at row 4 and column 9 we have 4*9=36.

Use two nested for loops to achive this. Note that you can use the following form to stop the `print` function from automatically starting a new line:


```python
print("text", end="")
print("more text")
```

    textmore text


Print the numbers in a field with width four, so that the numbers are nicely aligned. For instructions on how adjust the field width refer to [pyformat.info](https://pyformat.info/#number_padding).

---

#### Exercise 5 (two dice)

Let us consider throwing two dice. (A dice can give a value between 1 and 6.) Use two nested `for`-loops in the `main` function to iterate through all possible combinations the pair of dice can give. 
There are 36 possible combinations. 
Print all those combinations as (ordered) pairs,  that sum to 5. 
For example, your printout should include the pair `(2,3)`. Print one pair per line.

---

## Functions

#### Exercise 6 (triple square)

Write two functions: `triple` and `square`. Function `triple` multiplies its parameter by three. Function `square` raises its parameter to the power of two. For example, we have equalities `triple(5)==15`
and `square(5)==25`.

##### Part 1

In the `main` function write a `for` loop that iterates through values 1 to 10, and for each value prints its triple and its square. The output should be as follows:

```python
triple(1)==3 square(1)==1
triple(2)==6 square(2)==4
...
```

##### Part 2

Now modify this `for` loop so that it stops iteration when the square of a value is larger than the
triple of the value, without printing anything in the last iteration.

Note that the test cases check that both functions `triple` and `square` are called exactly once per iteration.

---

#### Exercise 7 (areas of shapes)

Create a program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.

An endless loop should ask for which shape you want the area be calculated. n empty string as input will exit the loop.
If the user gives a string that is none of the given shapes, the message “unknown shape!” should be printed.
Then it will ask for dimensions for that particular shape. When all the necessary dimensions are given, it prints the area, and starts the loop all over again. Use format specifier `f` for the area.

What happens if you give incorrect dimensions, like giving string "aa" as radius? You don't have to check for errors in the input.

Example interaction:

```python
Choose a shape (triangle, rectangle, circle): triangle
Give base of the triangle: 20
Give height of the triangle: 5
The area is 50.000000
Choose a shape (triangle, rectangle, circle): rectangel
Unknown shape!
Choose a shape (triangle, rectangle, circle): rectangle
Give width of the rectangle: 20
Give height of the rectangle: 4
The area is 80.000000
Choose a shape (triangle, rectangle, circle): circle
Give radius of the circle: 10
The area is 314.159265
Choose a shape (triangle, rectangle, circle): 
```

---

## Datastrukturer

* Lister
* Tupler

#### Exercise 8 (solve quadratic)

In mathematics, the quadratic equation $ax^2+bx+c=0$ can be solved with the formula 

$$x=\frac{-b\pm \sqrt{b^2 -4ac}}{2a}$$

In code it might be usefull to declare a variable for a part of the formula, named `d`, defined by $\sqrt{b^2 -4ac}$. the formula then can be written as:

$$x=\frac{-b\pm d}{2a}$$

We need both the positive and the negative version og the square root, becaurce all squareroots have to solutions, since both $ 2^2 = 4 $ and $(-2)^2 = 4 $ thus $ \sqrt{4} $ has both $ 2 $ and $ -2 $ as solutions.

Remember the order of precedence are important, especially when you implement mathematical expressions.

Write a function `solve_quadratic`, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters. It should work like this:

```python
print(solve_quadratic(1,-3,2))
(2.0,1.0)
print(solve_quadratic(1,2,1))
(-1.0,-1.0)
```

You may want to use the `math.sqrt` function from the `math` module in your solution. Test that your function works in the main function!

---

#### Exercise 9 (merge)

Suppose we have two lists `L1` and `L2` that contain integers which are sorted in ascending order.  
Create a function `merge` that gets these lists as parameters and returns a new sorted list `L` that has all the elements of `L1` and `L2`. So, `len(L)` should equal to `len(L1)+len(L2)`.  
Do this using the fact that both lists are already sorted. You can’t use the `sorted` function or the `sort` method in implementing the `merge` method. You can however use these `sorted` in the main function for creating inputs to the `merge` function.

Test with a couple of examples in the `main` function that your solution works correctly.

Note: __In Python argument lists are passed by reference to the function, they are not copied! Make sure you don't modify the original lists of the caller.__

---

#### Exercise 10 (detect ranges)

Create a function named `detect_ranges` that gets a list of integers as a parameter.  

The function should then  
- sort this list, and 
- transform the list into another list where pairs are used for all the detected intervals. So `3,4,5,6` is replaced by the pair `(3,7)`. 
- Numbers that are not part of any interval result just single numbers.  

The resulting list consists of these numbers and pairs, separated by commas.

An example of how this function works:

```python
print(detect_ranges([2,5,4,8,12,6,7,10,13]))
[2,(4,9),10,(12,14)]
```

Note that the second element of the pair does not belong to the range. __This is consistent with the way Python's `range` function works.__ You may assume that no element in the input list appears multiple times.

---

#### Exercise 11 (interleave)

Write function `interleave` that gets arbitrary number of lists as parameters. You may assume that all the lists have equal length. The function should return one list containing all the elements from the input lists interleaved.
Test your function from the `main` function of the program.

Example:
`interleave([1,2,3], [20,30,40], ['a', 'b', 'c'])`
should return
`[1, 20, 'a', 2, 30, 'b', 3, 40, 'c']`.
Use the `zip` function to implement `interleave`. Remember the `extend` method of list objects.

---
* Sets

#### Exercise 12 (distinct characters)

Write function `distinct_characters` that gets a list of strings as a parameter. It should return a dictionary whose keys are the strings of the input list and the corresponding values are the numbers of distinct characters in the key.

Use the `set` container to temporarily store the distinct characters in a string.

Example of usage:
`distinct_characters(["check", "look", "try", "pop"])`
should return
`{ "check" : 4, "look" : 3, "try" : 3, "pop" : 2}`.

---

* Dictionarys

#### Exercise 13 (reverse dictionary)

Let `d` be a dictionary that has English words as keys and a list of Finnish words as values. So, the
dictionary can be used to find out the Finnish equivalents of an English word in the following way:

```python
d["move"]
["liikuttaa"]
d["hide"]
["piilottaa", "salata"]
```

Make a function `reverse_dictionary` that creates a Finnish to English dictionary based on a English to Finnish dictionary given as a parameter. The values of the created dictionary should be lists of words. It should work like this:

```python
d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)
{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}
```

Be careful with synonyms and homonyms!

---

#### Exercise 14 (find matching)

Write function `find_matching` that gets a list of strings and a search string as parameters. The function should return the indices to those elements in the input list that contain the search string. Use the function `enumerate`.

An example:
`find_matching(["sensitive", "engine", "rubbish", "comment"], "en")`
should return the list
`[0, 1, 3]`.

---

* Comprehensions

#### Exercise 15 (two dice comprehension)

Redo the earlier exercise which printed all the pairs of two dice results that sum to 5. But this time use a list comprehension. Print one pair per line.

---

#### Exercise 16 (transform)

Write a function `transform` that gets two strings as parameters and returns a list of integers. 
The function should 
- split the strings into words, and 
- convert these words to integers. 

This should give two lists of integers. Then the function should 
- return a list whose elements are multiplication of two integers in the respective positions in the lists.  

For example
`transform("1 5 3", "2 6 -1")`
should return the list of integers
`[2, 30, -3]`.

You __have__ to use `split`, `map`, and `zip` functions/methods. You may assume that the two input strings are in correct format.

---

#### Exercise 17 (positive list)

Write a function `positive_list` that gets a list of numbers as a parameter, and returns a list with the negative numbers and zero filtered out using the `filter` function.

The function call `positive_list([2,-2,0,1,-7])` should return the list `[2,1]`. Test your function in the `main` function.

---

* sequence processing

## String handling

#### Exercise 18 (acronyms)

Write function `acronyms` which takes a string as a parameter and returns a list of acronyms. A word is an acronym if it has length at least two, and all its characters are in uppercase. Before acronym detection, delete punctuation with the `strip` method.

Test this function in the `main` function with the following call:

```python
print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))
```

This should return
```['EU', 'GDPR', 'IBM', 'IBM', 'EEA', 'EEA', 'IBM', 'PO', 'PO6', '3AU']```

---

#### Exercise 19 (sum equation)

Write a function `sum_equation` which takes a list of positive integers as parameters and returns a string with an equation of the sum of the elements.

Example:
`sum_equation([1,5,7])`
returns
`"1 + 5 + 7 = 13"`
Observe, the spaces should be exactly as shown above. For an empty list the function should return the string "0 = 0".

---

## Moduler

#### Exercise 20 (usemodule)

Create your own module as file `triangle.py` in the `src` folder. The module should contain two functions:

* `hypothenuse` which returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle
* `area` which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.

Make sure both the functions and the module have descriptive docstrings. Add also the `__version__` and `__author__` attributes to the module. Call both your functions from the main function (which is in file `usemodule.py`).

---

## RegEx

# [Part02]
#### Exercise 21 (integers in brackets)

Write function `integers_in_brackets` that finds from a given string all integers that are enclosed in brackets.

Example run:
`integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx")`
returns
`[12, -43, 12]`.
So there can be whitespace between the number and the brackets, but no other character besides those that make up the integer.

Test your function from the `main` function.

---

#### Exercise 22 (file listing)

The file `src/listing.txt` contains a list of files with one line per file. Each line contains seven fields: access rights, number of references, owner's name, name of owning group, file size, date, filename. These fields are separated with one or more spaces. Note that there may be spaces also within these seven fields.

Write function `file_listing` that loads the file `src/listing.txt`. It should return a list of tuples (size, month, day, hour, minute, filename). Use regular expressions to do this (either `match`, `search`, `findall`, or `finditer` method).

An example: for line
```
-rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf
```
the function should create the tuple `(25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf")`.

---

#### Exercise 23 (red green blue)

The file `src/rgb.txt` contains names of colors and their numerical representations in RGB format. The RBG format allows a color to be represented as a mixture of red, green, and blue components. Each component can have an integer value in the range [0,255]. Each line in the file contains four fields: red, green, blue, and colorname.
Each field is separated by some amount of whitespace (tab or space in this case).
The text file is formatted to make it print nicely, but that makes it harder to process by a computer. Note that some color names can also contain a space character.
 
Write function `red_green_blue` that reads the file `rgb.txt` from the folder `src`.  Remove the irrelevant first line of the file. The function should return a list of strings. Clean-up the file so that the strings in the returned list have four fields separated by a single tab character (`\t`). Use regular expressions to do this.

The first string in the returned list should be:
```
'255\t250\t250\tsnow'
```

---

#### Exercise 24 (word frequencies)

Create function `word_frequencies` that gets a filename as a parameter and returns a dict with the word frequencies. In the dictionary the keys are the words and the corresponding values are the number of times that word occurred in the file specified by the function parameter. Read all the lines from the file and split the lines into words using the `split()` method. Further, remove punctuation from the ends of words using the `strip("""!"#$%&'()*,-./:;?@[]_""")` method call.

Test this function in the main function using the file `alice.txt`. In the output, there should be a word and its count per line separated by a tab:

```
The     64
Project 83
Gutenberg	26
EBook   3
of      303
```

---

#### Exercise 25 (summary)

This exercise can give two points at maximum!

Part 1.

Create a function called `summary` that gets a filename as a parameter. The input
file should contain a floating point number on each line of the file. Make your function read these
numbers and then return a triple containing the sum, average, and standard deviation of these numbers for the file.
As a reminder, the formula for corrected sample standard deviation is
$\sqrt{\frac{\sum_{i=1}^n (x_i - \overline x)^2}{n-1}}$, where $\overline x$ is the average.

The `main` function should call the function summary for each filename in the list `sys.argv[1:]` of command line parameters. (Skip `sys.argv[0]` since it contains the name of the current program.)

Example of usage from the command line:
`python3 src/summary.py src/example.txt src/example2.txt`

Print floating point numbers using six decimals precision. The output should look like this:
```
File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
File: src/example2.txt Sum: 5446.200000 Average: 1815.400000 Stddev: 3124.294045
```

Part 2.

If some line doesn’t represent a number, you can just ignore that line. You can achieve this with the *try-except* block. An example of recovering from an exceptional situation:
```python
try:
    x = float(line)           # The float constructor raises ValueError exception if conversion is no possible
except ValueError:
    # Statements in here are executed when the above conversion fails
```
We will cover more about exceptions later in the course.

---

#### Exercise 26 (file count)

This exercise can give two points at maximum!

Part 1.

Create a function `file_count` that gets a filename as parameter and returns a triple of numbers. The function should read the file, count the number of lines, words, and characters in the file, and return a triple with these count in this order. You get division into words by splitting at whitespace. You don't have to remove punctuation.

Part 2.

Create a main function that in a loop calls `file_count` using each filename in the list of command line parameters `sys.argv[1:]` as a parameter, in turn.
For call `python3 src/file_count file1 file2 ...`
the output should be
```
?      ?       ?       file1
?      ?       ?       file2
...
```
The fields are separated by tabs (`\t`). The fields are in order: linecount, wordcount, charactercount, filename.

---

#### Exercise 27 (file extensions)

This exercise can give two points at maximum!

Part 1.

Write function `file_extensions` that gets as a parameter a filename.
It should read through the lines from this file. Each line contains a filename.
Find the extension for each filename. The function should return a pair, where the
first element is a list containing all filenames with no extension (with the preceding period (`.`) removed).
The second element of the pair is a dictionary with extensions as keys and corresponding values are lists with filenames having that extension.

Sounds a bit complicated, but hopefully the next example will clarify this.
If the file contains the following lines
```
file1.txt
mydocument.pdf
file2.txt
archive.tar.gz
test
```
then the return value should be the pair:
`(["test"], { "txt" : ["file1.txt", "file2.txt"], "pdf" : ["mydocument.pdf"], "gz" : ["archive.tar.gz"] } )`

Part 2.

Write a `main` method that calls the `file_extensions` function with "src/filenames.txt" as the argument. Then print the results so that for each extension there is a line consisting of the extension and the number of files with that extension. The first line of the output should give the number of files without extensions.

With the example in part 1, the output should be
```
1 files with no extension
gz 1
pdf 1
txt 2
```
Had there been no filenames without extension then the first line would have been `0 files with no extension`. In the printout list the extensions in alphabetical order.

---

## Læs (og skriv, i) filer

## RegEx



## Objekter

#### Exercise 28 (prepend)

Create a class called `Prepend`. We create an instance of the class by giving a string as a parameter
to the initializer. The initializer stores the parameter in an instance attribute `start`. The class
also has a method `write(s)` which prints the string `s` prepended with the `start` string.
An example of usage:
```python
p = Prepend("+++ ")
p.write("Hello");
```
Will print
```
+++ Hello
```

Try out using the class from the `main` function.

---

#### Exercise 29 (rational)


Create a class `Rational` whose instances are rational numbers. A new rational number can be
created with the call to the class. For example, the call `r=Rational(1,4)` creates a rational
number “one quarter”. Make the instances support the following operations:
`+` `-` `*` `/` `<` `>` `==`
with their natural behaviour. Make the rationals also printable so that from the printout we can
clearly see that they are rational numbers.

---

## Undtagelser (Exceptions)

#### Exercise 30 (extract numbers)

Write a function `extract_numbers` that gets a string as a parameter. It should return a list of numbers that can be both ints and floats. Split the string to words at whitespace using the `split()` method. Then iterate through each word, and initially try to convert to an int. If unsuccesful, then try to convert to a float. If not a number then skip the word.

Example run:
`print(extract_numbers("abd 123 1.2 test 13.2 -1"))`
will return
`[123, 1.2, 13.2, -1]`

---

# Numpy 
[numpy.ipynb]

#### Exercise 31 (rows and columns)

Write two functions, `get_rows` and `get_columns`, that get a two dimensional array as parameter.
They should return the list of rows and columns of the array, respectively. The rows and columns should be one dimensional arrays. You may use the *transpose* operation, which flips rows to columns, in your solution. The transpose is done by the `T` method:

---
#### Exercise 32 (row and column vectors)

Create function `get_row_vectors` that returns a list of rows from the input array of shape `(n,m)`, but this time the rows must have shape `(1,m)`. Similarly, create function `get_columns_vectors` that returns a list of columns (each having shape `(n,1)`) of the input matrix .

Example: for a 2x3 input matrix

```
 [[5 0 3]
  [3 7 9]]
```

the result should be

```
Row vectors: 
[array([[5, 0, 3]]), array([[3, 7, 9]])]
Column vectors: 
[array([[5],
        [3]]), 
 array([[0],
        [7]]), 
 array([[3],
        [9]])]
```

The above output is basically just the returned lists printed with `print`. Only some
whitespace is adjusted to make it look nicer. Output is not tested.


---

#### Exercise 33 (diamond)

Create a function `diamond` that returns a two dimensional integer array where the `1`s form a diamond shape. Rest of the numbers are `0`. The function should get a parameter that tells the length of a side of the diamond. Do this using the `eye` and `concatenate` functions of NumPy and array slicing.

Example of usage:
```
print(diamond(3))
[[0 0 1 0 0]
 [0 1 0 1 0]
 [1 0 0 0 1]
 [0 1 0 1 0]
 [0 0 1 0 0]]
print(diamond(1))
[[1]]
```

---

#### Exercise 34 (vector lengths)

Write function `vector_lengths` that gets a two dimensional array of shape (n,m) as a parameter. Each row in this array corresponds to a vector. The function should return an array of shape (n,), that has the length of each vector in the input. The length is defined by the usual 
[Euclidean norm](<https://en.wikipedia.org/wiki/Norm_(mathematics&#41;#Euclidean_norm>). Don't use loops at all in your solution. Instead use vectorized operations. You must use at least the `np.sum` and the `np.sqrt` functions. You can't use the function `scipy.linalg.norm`. Test your function in the main function.

#### Exercise 35 (vector angles)

Let x and y be m-dimensional vectors. The angle $\alpha$ between two vectors is defined by the equation
$\cos_{xy}(\alpha):=\frac{\langle x,y\rangle}{||x|| ||y||}$,
where the angle brackets denote the [inner product](https://en.wikipedia.org/wiki/Inner_product_space#Euclidean_space), and $||x||:=\sqrt{\langle x,x \rangle}$. 

Write function `vector_angles` that gets two arrays X and Y with same shape (n,m) as parameters. Each row in the arrays corresponds to a vector. The function should return vector of shape (n,) with the corresponding angles between vectors of `X` and `Y` in degrees, not in radians. Again, don't use loops, but use vectorized operations.

Note: function `np.arccos` is only defined on the domain [-1.0,1.0]. If you try to compute `np.arccos(1.000000001)`, it will fail. These kind of errors can occur due to use of finite precision in numerical computations. Force the argument to be in the correct range (`clip` method).

Test your solution in the main program.
---

# [Part03]
# NumPy (continues) [`numpy2.ipynb`]

#### Exercise 37 (column comparison)

Write function `column_comparison` that gets a two dimensional array as parameter. The function should return a new array containing those rows from the input that have the value in the second column larger than in the second last column. You may assume that the input contains at least two columns. Don't use loops, but instead vectorized operations. Try out your function in the main function.

For array

```
 [[8 9 3 8 8]
 [0 5 3 9 9]
 [5 7 6 0 4]
 [7 8 1 6 2]
 [2 1 3 5 8]]
```
the result would be
```
 [[8 9 3 8 8]
 [5 7 6 0 4]
 [7 8 1 6 2]]
```
---

#### Exercise 38 (first half second half)

Write function `first_half_second_half` that gets a two dimensional array of shape `(n,2*m)` as a parameter. The input array has `2*m` columns. The output from the function should be a matrix with those rows from the input that have the sum of the first `m` elements larger than the sum of the last `m` elements on the row. Your solution should call the `np.sum` function or the corresponding method exactly twice.

Example of usage:
```python
a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
first_half_second_half(a)
array([[2, 2, 1, 2]])
```
---

#### Exercise 39 (most frequent first)

**<span style="color:red">Note:</span>** This exercise is fairly difficult. Feel free to skip if you get stuck.

Write function `most_frequent_first` that gets a two dimensional array and an index `c` of a column as parameters. The function should then return the array whose rows are sorted based on column `c`, in the following way. Rows are ordered so that those rows with the most frequent element in column `c` come first, then come the rows with the second most frequent element in column `c`, and so on. Therefore, the values outside column `c` don't affect the ordering in any way.

Example of usage:
```
a:
 [[5 0 3 3 7 9 3 5 2 4]
 [7 6 8 8 1 6 7 7 8 1]
 [5 9 8 9 4 3 0 3 5 0]
 [2 3 8 1 3 3 3 7 0 1]
 [9 9 0 4 7 3 2 7 2 0]
 [0 4 5 5 6 8 4 1 4 9]
 [8 1 1 7 9 9 3 6 7 2]
 [0 3 5 9 4 4 6 4 4 3]
 [4 4 8 4 3 7 5 5 0 1]
 [5 9 3 0 5 0 1 2 4 2]]
print(most_frequent_first(a, -1))
 [[4 4 8 4 3 7 5 5 0 1]
 [2 3 8 1 3 3 3 7 0 1]
 [7 6 8 8 1 6 7 7 8 1]
 [5 9 3 0 5 0 1 2 4 2]
 [8 1 1 7 9 9 3 6 7 2]
 [9 9 0 4 7 3 2 7 2 0]
 [5 9 8 9 4 3 0 3 5 0]
 [0 3 5 9 4 4 6 4 4 3]
 [0 4 5 5 6 8 4 1 4 9]
 [5 0 3 3 7 9 3 5 2 4]]
```

If we look at the last column, we see that the number 1 appears three times, then both numbers 2 and 0 appear twice, and lastly numbers 3, 9, and 4 appear only once. Note that, for example, among those rows that contain in column `c` a number that appear twice in column `c` the order can be arbitrary.

Hint: the function `np.unique` may be useful.

---

#### Exercise 40 (matrix power)

Repeat the functionality of the NumPy function `numpy.linalg.matrix_power`, which raises a square matrix of shape (m,m) to the `n`th power. Here the multiplication is the matrix multiplication. Square matrix `a` raised to power `n` is therefore `a @ a @ ... @ a` where `a` is repeated `n` times. When n is zero then $a^0$ is equal to `np.eye(m)`.

Write function `matrix_power` that gets as first argument a square matrix `a` and as second argument a non-negative integer `n`. The function should return the matrix `a` multiplied by itself `n-1` times.
Use Python's `reduce` function and a generator expression.

Extend the `matrix_power` function.
For negative powers, we define $a^{-1}$ to be equal to the multiplicative inverse of `a`. You can use NumPy's function `numpy.linalg.inv` for this. And you may assume that the input matrix is invertible.

---

#### Exercise 41 (correlation)

This exercise can give two points at maximum!

Load the iris dataset using the provided function `load()` in the stub solution. The four columns of the returned array correspond to

* sepal length (cm)
* sepal width (cm)
* petal length (cm)
* petal width (cm)

Part 1. What is the Pearson correlation between the variables `sepal length` and `petal length`. Compute this using the `scipy.stats.pearsonr` function. It returns a tuple whose first element is the correlation. Write a function `lengths` that loads the data and returns the correlation.

Part 2. What are the correlations between all the variables. Write a function `correlations` that returns an array of shape (4,4) containing the correlations. Use the function `np.corrcoef`. Which pair of variables is the most highly correlated?

Note the input formats of both functions `pearsonr` and `corrcoef`.

---

#### Exercise 42 (meeting lines)

Write function `meeting_lines` that gets the coefficients of two lines as parameters and returns the point where the two lines meet. The equations for the lines are $y=a_1x + b_1$ and $y=a_2x + b_2$. Use the `np.linalg.solve` function. Create a main function to test your solution.

Example of usage:
```
x, y = meeting_lines(a1, b1, a2, b2)
```
---

#### Exercise 43 (meeting planes)
Write function `meeting_planes` that gets the coefficients of three planes as parameters and returns the point where the planes meet. The equations for the planes are:
$z =a_1y + b_1x+ c_1$,
$z =a_2y + b_2x+ c_2$, and
$z =a_3y + b_3x+ c_3$.

Example of usage:
```
x, y, z = meeting_planes(a1, b1, c1,  a2, b2, c2,  a3, b3, c3)
```
---

#### Exercise 44 (almost meeting lines)
In the earlier "meeting lines" exercise there is a problem if the lines don't meet at all. Extend that solution so that it tells the meeting point if it exists, and otherwise finds the point that is closest to the both lines.
You can use the `numpy.linalg.lstsq` for this.

Example of usage:
```
(x, y), exact = almost_meeting_lines(1, 2, -1, 0)
print(x, y, exact)
-1.000000 1.000000 True
```

---

# MatPlotLib

#### Exercise 45 (multiple graphs)

In the above plot the x coordinates were implicitly set to the indices of the array `a`, that is, `arange(10)`. Find out from the documentation of `plt.plot` how to specify the x coordinates explicitly. Find out also how to draw multiple graphs in one axes.

Make your `main` function plot the following two graphs in one axes. The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1. The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.

Add also a title and some labels for x axis and y axis. Note that in the non-interactive mode you have to call `plt.show()` for the figure to show.

The plot should look like the one below.

![multiplot](multiplot.png)

---

#### Exercise 46 (subfigures)

Write function `subfigures` that creates a figure that has two subfigures (two *axes* in matplotlib parlance). The function gets a two dimensional array `a` as a parameter. In the left subfigure draw using the `plot` *method* a graph, whose x coordinates are in the first column of `a` and the y coordinates are in the second column of `a`. In the right subfigure draw using the `scatter` *method* a set of points whose x coords are again in the first column of `a` and whose y coordinates are in the second column of `a`. Additionally, the points should get their color from the third column of `a`, and size of the point from the fourth column of `a`. For this, use the `c` and `s` named parameters of `scatter`, respectively

Test your function `subfigure` from the `main` function.

---

# Image processing

#### Exercise 47 (to grayscale)

This exercise can give two points at maximum!

##### Part 1.

Write a function `to_grayscale` that takes an RGB image (three dimensional array) and returns a two dimensional gray-scale image. The conversion to gray-scale should take a weighted sum of the red, green, and blue values, and use that as the value of gray. The first axis is the x, the second is y, and the third is the color components (red, green, blue).
Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. These weights are so because the human eye is most sensitive to green color and least sensitive to blue color.

In the main function you can, for example, use the provided image `src/painting.png`. Display the grayscale image with the `plt.imshow` function. You may have to call the function `plt.gray` to set the color palette (colormap) to gray.
(See `help(plt.colormaps)` for more information about colormaps.)

##### Part 2.

Write functions `to_red`, `to_green`, and `to_blue` that get a three dimensional array as a parameter and return a three dimensional arrays. For instance, the function `to_red` should zero out the green and blue color components and return the result. In the `main` function create a figure with three subfigures: the top one should be the red image, the middle one the green image, and the bottom one the blue image.

---

#### Exercise 48 (radial fade)

Make program that does fading of an image as earlier, except now not in horizontal direction but in radial direction. As we move away from the centre of the image, the pixels fade to black.

##### Part1.

Write function `center` that returns coordinate pair (center_y, center_x) of the image center. Note that these coordinates might not be integers. Example of usage:

```python
print(center(np.zeros((10, 11, 3))))
(4.5, 5)
```
The function should work both for two and three dimensional images, that is grayscale and color images.

Write also function `radial_distance` that returns for image with width `w` and height `h` an array with shape (h,w), where the number at index (i,j) gives the euclidean distance from the point (i,j) to the center of the image.

##### Part 2.

Create function `scale(a, tmin=0.0, tmax=1.0)` that returns a copy of the array `a` with its elements scaled to be in the range `[tmin,tmax]`.

Using the functions `radial_distance` and `scale` write function `radial_mask` that takes an image as a parameter and returns an array with same height and width filled with values between 0.0 and 1.0. Do this using the `scale` function.  To make the resulting array values near the center of array to be close to 1 and closer to the edges of the array are values closer to be 0, subtract the previous array from 1.

Write also function `radial_fade` that returns the image multiplied by its radial mask.

Test your functions in the `main` function, which should create, using matplotlib, a figure that has three subfigures stacked vertically. On top the original `painting.png`, in the middle the mask, and on the bottom the faded image.

---

# Pandas

#### Exercise 49 (read series)

Write function `read_series` that reads input lines from the user and return a Series. Each line should contain first the index and then the corresponding value, separated by whitespace. The index and values are strings (in this case `dtype` is `object`). An empty line signals the end of Series. Malformed input should cause an exception. An input line is malformed, if it is non-empty and, when split at whitespace, does not result in two parts.

Test your function from the `main` function.

---

#### Exercise 50 (operations on series)

Write function `create_series` that gets two lists of numbers as parameters. Both lists should have length 3.
The function should first create two Series, `s1` and `s2`. The first series should have values from the first parameter list and have corresponding indices `a`, `b`, and  `c`. The second series should get its values from the second parameter list and have again the corresponding indices `a`, `b`, and  `c`. The function should return the pair of these Series.

Then, write a function `modify_series` that gets two Series as parameters. It should add to the first Series `s1` a new value with index `d`. The new value should be the same as the value in Series `s2` with index `b`.
Then delete the element from `s2` that has index `b`. Now the first Series should have four values, while the second list has only two values. Adding a new element to a Series can be achieved by assignment, like with dictionaries. Deletion of an element from a Series can be done with the `del` statement.

Test these functions from the main function. Try adding together the Series returned by the `modify_series` function. The operations on Series use the indices to keep the element-wise operations *aligned*. If for some index the operation could not be performed, the resulting value will be `NaN` (Not A Number).

---

#### Exercise 51 (inverse series)

Write function `inverse_series` that get a Series as a parameter and returns a new series, whose indices and values have swapped roles. Test your function from the `main` function.

What happens if some value appears multiple times in the original Series? What happens if you use this value to index the resulting Series?
---

# [ PART 3 ]

#### Exercise 52 (cities)

Write function `cities` that returns the following DataFrame of top Finnish cities by population:

```
                 Population Total area
Helsinki         643272     715.48
Espoo            279044     528.03
Tampere          231853     689.59
Vantaa           223027     240.35
Oulu             201810     3817.52
```

---

#### Exercise 53 (powers of series)

Make function `powers_of_series` that takes a Series and a positive integer `k` as parameters and returns a DataFrame. The resulting DataFrame should have the same index as the input Series. The first column of the dataFrame should be the input Series, the second column should contain the Series raised to power of two. The third column should contain the Series raised to the power of three, and so on until (and including) power of `k`. The columns should have indices from 1 to k.

The values should be numbers, but the index can have any type.
Test your function from the `main` function. Example of usage:

```
s = pd.Series([1,2,3,4], index=list("abcd"))
print(powers_of_series(s, 3))
```
Should print:
```
   1   2   3
a  1   1   1
b  2   4   8
c  3   9  27
d  4  16  64
```

---

#### Exercise 54 (municipal information)

In the `main` function load a data set of municipal information from the `src` folder (originally from [Statistics Finland](https://pxnet2.stat.fi/PXWeb/pxweb/en/)). Use the function `pd.read_csv`, and note that the separator is a tabulator.

Print the shape of the DataFrame (number of rows and columns) and the column names in the following format:
```
Shape: r,c
Columns:
col1 
col2
...
```

Note, sometimes file ending `tsv` (tab separated values) is used instead of `csv` if the separator is a tab.
---

#### Exercise 55 (municipalities of finland)

Load again the municipal information DataFrame. The rows of the DataFrame correspond to various geographical areas of Finland. The first row is about Finland as a whole, then rows from Akaa to Äänekoski are municipalities of Finland in alphabetical order. After that some larger regions are listed.

Write function `municipalities_of_finland` that returns a DataFrame containing only rows about municipalities.
Give an appropriate argument for `pd.read_csv` so that it interprets the column about region name as the (row) index. This way you can index the DataFrame with the names of the regions.

Test your function from the `main` function.
---

#### Exercise 56 (swedish and foreigners)

Write function `swedish_and_foreigners` that

* Reads the municipalities data set
* Takes the subset about municipalities (like in previous exercise)
* Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
* From this data set take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns.

The function should return this final DataFrame.

Do you see some kind of correlation between the columns about Swedish speaking and foreign people? Do you see correlation between the columns about the population and the proportion of Swedish speaking people in this subset?

---

#### Exercise 57 (growing municipalities)

Write function `growing_municipalities` that gets subset of municipalities (a DataFrame) as a parameter and returns the proportion of municipalities with increasing population in that subset.

Test your function from the `main` function using some subset of the municipalities.
Print the proportion as percentages using 1 decimal precision.

Example output:

```
Proportion of growing municipalities: 12.4%
```

---

#### Exercise 58 (subsetting with loc)

Write function `subsetting_with_loc` that in one go takes the subset of municipalities from Akaa to Äänekoski and restricts it to columns: "Population", "Share of Swedish-speakers of the population, %", and "Share of foreign citizens of the population, %".
The function should return this content as a DataFrame. Use the attribute `loc`.


---

#### Exercise 59 (subsetting by positions)

Write function `subsetting_by_positions` that does the following.

Read the data set of the top forty singles from the beginning of the year 1964 from the `src` folder. Return the top 10 entries and only the columns `Title` and `Artist`. Get these elements by their positions, that is, by using a single call to the `iloc` attribute. The function should return these as a DataFrame.

---

#### Exercise 60 (snow depth)

Write function `snow_depth` that reads in the weather DataFrame from the `src` folder and returns the maximum amount of snow in the year 2017.

Print the result in the `main` function in the following form:
```
Max snow depth: xx.x
```

---

#### Exercise 61 (average temperature)

Write function `average_temperature` that reads the weather data set and returns the average temperature in July.

Print the result in the `main` function in the following form:
```
Average temperature in July: xx.x
```
---

#### Exercise 62 (below zero)

Write function `below_zero` that returns the number of days when the temperature was below zero.

Print the result in the main function in the following form:

```
Number of days below zero: xx
```
---

#### Exercise 63 (cyclists)

Write function `cyclists` that does the following.

Load the Helsinki bicycle data set from the `src` folder (https://hri.fi/data/dataset//helsingin-pyorailijamaarat). The dataset contains the number of cyclists passing by measuring points per hour. The data is gathered over about four years, and there are 20 measuring points around Helsinki. The dataset contains some empty rows at the end. Get rid of these. Also, get rid of columns that contain only missing values. Return the cleaned dataset. 

---

#### Exercise 64 (missing value types)

Make function `missing_value_types` that returns the following DataFrame. Use the `State` column as the (row) index. The value types for the two other columns should be `float` and `object`, respectively. Replace the dashes with the appropriate missing value symbols.

State | Year of independence | President
------|----------------------|----------
United Kingdom | - | -
Finland | 1917 | Niinistö
USA | 1776 | Trump
Sweden | 1523 | -
Germany | - | Steinmeier
Russia | 1992 | Putin

---

#### Exercise 65 (special missing values)

Write function `special_missing_values` that does the following.

Read the data set of the top forty singles from the beginning of the year 1964 from the `src` folder. Return the rows whose singles' position dropped compared to last week's position (column LW=Last Week).

To do this you first have to convert the special values "New" and "Re" (Re-entry) to missing values (`None`).

---

#### Exercise 66 (last week)

This exercise can give two points at maximum!

Write function `last_week` that reads the top40 data set mentioned in the above exercise. The function should then try to reconstruct the top40 list of the previous week based on that week's list. Try to do this as well as possible. You can fill the values that are impossible to reconstruct by missing value symbols. Your solution should work for a top40 list of any week. So don't rely on specific features of this top40 list. The column `WoC` means "Weeks on Chart", that is, on how many weeks this song has been on the top 40 list.

Hint. First create the last week's top40 list of those songs that are also on this week's list. Then add those entries that were not on this week's list. Finally sort by position.

Hint 2. The `where` method of Series and DataFrame can be useful. It can also be nested.

Hint 3. Like in NumPy, you can use with Pandas the bitwise operators `&`, `|`, and `~`.
Remember that he bitwise operators have higher precedence than the comparison operations, so you may
have to use parentheses around comparisons, if you combined result of comparisons with bitwise operators.

You get a second point, if you get the columns `LW` and `Peak Pos` correct.

---

#### Exercise 67 (split date)

Read again the bicycle data set from `src` folder,
and clean it as in the earlier exercise. Then split the `Päivämäärä` column into a DataFrame with five columns with column names `Weekday`, `Day`, `Month`, `Year`, and `Hour`. Note that you also need to to do some conversions. To get Hours, drop the colon and minutes. Convert field `Weekday` according the following rule:
```
ma -> Mon
ti -> Tue
ke -> Wed
to -> Thu
pe -> Fri
la -> Sat
su -> Sun
```
Convert the `Month` column according to the following mapping
```
tammi 1
helmi 2
maalis 3
huhti 4
touko 5
kesä 6
heinä 7
elo 8
syys 9
loka 10
marras 11
joulu 12
```

Create function `split_date` that does the above and returns a DataFrame with five columns. You may want to use the `map` method of Series objects.

So the first element in the `Päivämäärä` column of the original data set should be converted from
`ke 1 tammi 2014 00:00`
to
`Wed 1 1 2014 0` . Test your solution from the `main` function.
---

#### Exercise 68 (cleaning data)

This exercise can give two points at maximum!

The entries in the following table of US presidents are not uniformly formatted. Make function `cleaning_data` that reads the table from the tsv file `src/presidents.tsv` and returns the cleaned version of it. Note, you must do the edits programmatically using the string edit methods, not by creating a new DataFrame by hand. The columns should have `dtype`s `object`, `integer`, `float`, `integer`, `object`. The `where` method of DataFrames can be helpful, likewise the [string methods](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods) of Series objects. You get an additional point, if you manage to get the columns President and Vice-president right!

President |	Start |	Last |	Seasons | 	Vice-president|
----------|-------|------|----------|------------------|
donald trump|	2017 Jan|	-|	1|	Mike pence
barack obama|	2009|	2017|	2|	joe Biden
bush, george|	2001|	2009|	2|	Cheney, dick
Clinton, Bill|	1993|	2001|	two|	gore, Al

---

#### Exercise 69 (cycling weather)

Merge the processed cycling data set (from the previous exercise) and weather data set along the columns year, month, and day. Note that the names of these columns might be different in the two tables: use the `left_on` and `right_on` parameters. Then drop useless columns 'm', 'd', 'Time', and 'Time zone'.

Write function `cycling_weather` that reads the data sets and returns the resulting DataFrame.

---

#### Exercise 70 (top bands)

Merge the DataFrames UK top40 and the bands DataFrame that are stored in the `src` folder.
Do all this in the parameterless function `top_bands`, which should return the merged DataFrame.
Use the `left_on` and `right_on` parameters to `merge`. Test your function from the `main` function.

---

#### Exercise 71 (cyclists per day)

This exercise can give two points at maximum!

Part 1.

Read, clean and parse the bicycle data set as before. Group the rows by year, month, and day. Get the sum for each group.
Make function `cyclists_per_day` that does the above. The function should return a DataFrame.
Make sure that the columns Hour and Weekday are not included in the returned DataFrame.

Part 2.

In the `main` function, using the function `cyclists_per_day`, get the daily counts.  The index of the DataFrame now consists of tuples (Year, Month, Day). Then restrict this data to August of year 2017, and plot this data. Don't forget to call the `plt.show` function of matplotlib. The x-axis should have ticks from 1 to 31, and there should be a curve to each measuring station. Can you spot the weekends?

---

#### Exercise 72 (best record company)

We use again the UK top 40 data set from the first week of 1964 in the `src` folder. Here we define "goodness" of a record company (`Publisher`) based on the sum of the weeks on chart (WoC) of its singles. Return a DataFrame of the singles by the best record company (a subset of rows of the original DataFrame). Do this with function `best_record_company`.

---

#### Exercise 73 (suicide fractions)

Load the suicide data set from `src` folder. This data was originally downloaded from [Kaggle](https://www.kaggle.com/szamil/who-suicide-statistics). Kaggle contains lots of interesting open data sets.

Write function `suicide_fractions` that loads the data set and returns a Series that has the country as the (row) index and as the column the mean fraction of suicides per population in that country. In other words, the value is the average of suicide fractions. The information about year, sex and age is not used.

---

#### Exercise 74 (suicide weather)

Copy the function `suicide fractions` from the previous exercise. 

Implement function `suicide_weather` as described below.
We use the dataset of average temperature (over years 1961-1990) in different countries from `src/List_of_countries_by_average_yearly_temperature.html` (https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature) .
You can use the function `pd.read_html` to get all the tables from a html page. By default `pd.read_html` does not know which row contains column headers and which column contains row headers. Therefore, you have to give both `index_col` and `header` parameters to `read_html`. Maku sure you use the country as the (row) index for both of the DataFrames. What is the [Spearman correlation](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) between these variables? Use the `corr` method of Series object. Note the the two Series need not be sorted as the indices of the rows (country names) are used to align them.

The return value of the function `suicide_weather` is a tuple (suicide_rows, temperature_rows, common_rows, spearman_correlation)
The output from the `main` function should be of the following form:

```
Suicide DataFrame has x rows
Temperature DataFrame has x rows
Common DataFrame has x rows
Spearman correlation: x.x
```

You might have trouble when trying to convert the temperatures to float. The is because the negative numbers on that html page use a special *unicode minus sign*, which looks typographically nice, but the float constructor cannot interpret it as a minus sign. You can try out the following example:

---

#### Exercise 75 (bicycle timeseries)

Write function `bicycle_timeseries` that

* reads the data set
* cleans it
* turns its `Päivämäärä` column into (row) DatetimeIndex (that is, to row names) of that DataFrame
* returns the new DataFrame

---

#### Exercise 76 (commute)

In function `commute` do the following:

Use the function `bicycle_timeseries` to get the bicycle data. Restrict to August 2017, group by the weekday, aggregate by summing. Set the `Weekday` column to numbers from one to seven. Then set the column `Weekday` as the (row) index. Return the resulting DataFrame from the function.

In the `main` function plot the DataFrame. Xticklabels should be the weekdays. Don't forget to call `show` function!

If you want the xticklabels to be `['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']` instead of numbers (1,..,7), then it may get a bit messy. There seems to be a problem with non-numeric `x` values. You could try the following after plotting, but you don't have to:

```python
weekdays="x mon tue wed thu fri sat sun".title().split()
plt.gca().set_xticklabels(weekdays)
```

---


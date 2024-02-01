import sys
import math

def summary(filename):
    with open(filename, 'r') as file:
        numbers = []
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                continue

        if not numbers:
            return (0, 0, 0)  # Handle empty or non-numeric files

        total = sum(numbers)
        average = total / len(numbers)
        stddev = math.sqrt(sum((x - average) ** 2 for x in numbers) / (len(numbers) - 1))

        return (total, average, stddev)

def main():
    for filename in sys.argv[1:]:
        total, average, stddev = summary(filename)
        print(f"File: {filename} Sum: {total:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")

if __name__ == "__main__":
    main()


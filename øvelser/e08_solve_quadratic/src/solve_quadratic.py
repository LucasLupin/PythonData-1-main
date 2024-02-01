import math

def solve_quadratic(a, b, c):

    d = math.sqrt(b**2 - 4*a*c)
    
    # Calculate the two solutions
    sol1 = (-b + d) / (2*a)
    sol2 = (-b -d) / (2*a)
    
    return (sol1, sol2)

def main():
    print(solve_quadratic(1, -3, 2)) 
    print(solve_quadratic(1, 2, 1))

if __name__ == "__main__":
    main()

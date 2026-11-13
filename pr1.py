"""Write a program non-recursive and recursive program to calculate Fibonacci numbers and
analyze their time and space complexity."""


# Fibonacci Series - Non-Recursive and Recursive

def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


nterms = int(input("How many terms?: "))

if nterms <= 0:
    print("Enter a positive integer.")
else:
    print("\nFibonacci Sequence (Non-Recursive):")
    
    n1, n2 = 0, 1
    for i in range(nterms):
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth

    print("\n\nFibonacci Sequence (Recursive):")
    
    for i in range(nterms):
        print(rec_fib(i), end=" ")
def fatorial(n):
    if (n == 0):
        return 1
    return n * fatorial(n-1)

def fibonacci(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    return fibonacci(n - 1)  + fibonacci(n - 2)

if __name__ == '__main__':
    fat = fatorial(6)
    fib = []
    for i in range(1, 11):
        fib.append(fibonacci(i))
    
    print(fat)
    print(fib)

   
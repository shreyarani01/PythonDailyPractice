def fibonacci(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fibonacci(m-1) + fibonacci(m-2)
    
print(fibonacci(12))
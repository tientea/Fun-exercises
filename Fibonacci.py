def Fibonacci():
    user = int(input("Please enter the desired amount of Fibonacci numbers:  "))
    i = 1
    if user == 0:
        fib = []
    elif user == 1:
        fib = [1]
    elif user == 2:
        fib = [1,1]
    elif user > 2: 
        fib = [1,1]
        while i < (user - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    return fib

print(Fibonacci())
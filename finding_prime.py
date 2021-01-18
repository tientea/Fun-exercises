def get_input(user ="Give me a number above 2: "):
    n = 0
    while n < 3: 
        n = int(input(user))
    return n
    
def get_divisors(n):
    divisors = [i for i in list(range(2,n)) if n%i == 0]
    return divisors

n = get_input()
divisors = get_divisors(n)
if divisors == []:
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number due to its divisors {}".format(n,divisors))
    
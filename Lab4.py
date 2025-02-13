def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a ,b = b , a + b

    return b
    #print(f"fibonacci({n}) == {b}")


#fibonacci(6)

def is_prime(n):
    if n<=0 :
        return False
    if n==1:
        return False
    if n==2:
        return True
    if 0<=n:
        for i in range (2, n):
            if n % i == 0:
                return False

    return True

#print(is_prime(-2))





def print_prime_factors(n):
    result = str(n) + " = "  # Start with the number
    factors = []  # List to store prime factors

    # Start dividing by 2 (smallest prime)
    while n % 2 == 0:
        factors.append(2)
        n //= 2  # Reduce n

    # Check for odd factors from 3 onward
    for i in range(3, n + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # Join factors with ' * '
    result += " * ".join(map(str, factors))
    print(result)

#print_prime_factors(2475)










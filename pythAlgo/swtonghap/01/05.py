def isPrime(n):
    # Write your code here
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return i
    return 1
import sys

def sieve_of_eratosthenes(n):
    
    numbers = list(range(2, n + 1))

 
    primes = []
    while numbers:

        prime = numbers[0]
        primes.append(prime)

       
        numbers = [num for num in numbers if num % prime != 0]

    return primes

if __name__ == "__main__":
 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <number>")
        sys.exit(1)

    try:
       
        num = int(sys.argv[1])

     
        if num < 0:
            print("Please enter a non-negative integer.")
            sys.exit(1)

     
        result = sieve_of_eratosthenes(num)


        print(sorted(result))

    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)


# prime number checker
def prime_checker(number=1):
    is_prime = True
    # prime number can only be decided by 1 and itself so if there is no remainder it's not prime
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# tester
n = int(input("Check this number: "))
prime_checker(number=n)




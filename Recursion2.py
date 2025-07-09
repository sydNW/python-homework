# 1) Recursive multiplication using repeated addition
def recursive_multiply(a, b):
    if b == 0:
        return 0
    return a + recursive_multiply(a, b - 1)


# 2) Recursive exponentiation without using **
def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)


# 3) Countdown from n to 0
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)


# 4) Count up from 0 to n using modified countdown
def countup(n, current=0):
    if current > n:
        return
    print(current)
    countup(n, current + 1)


# 5) Reverse a string using recursion
def reverse_string(s):
    if s == "":
        return s
    return s[-1] + reverse_string(s[:-1])


# 6) Check if a number is prime recursively
def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)


# 7) Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # 1) Test recursive multiplication
    # print("1) Multiply 4 * 3 =", recursive_multiply(4, 3))

    # 2) Test recursive exponentiation
    # print("2) Power 2^5 =", recursive_power(2, 5))

    # 3) Test countdown from 5 to 0
    # print("3) Countdown from 5:")
    # countdown(5)

    # 4) Test countup from 0 to 5
    # print("4) Countup to 5:")
    # countup(5)

    # 5) Test reverse string
    # print("5) Reverse 'hello' =", reverse_string("hello"))

    # 6) Test prime check
    print("6) Is 29 prime? =", is_prime(29))
    print("6) Is 15 prime? =", is_prime(15))

    # 7) Test Fibonacci
    # print("7) Fibonacci of 6 =", fibonacci(6))
    # print("7) Fibonacci of 10 =", fibonacci(10))
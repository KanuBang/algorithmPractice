
def factorial(n):
    if n < 1:
        return 1
    print(n, "호출")
    return n * factorial(n-1)

n = factorial(int(input()))
print(n)
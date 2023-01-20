def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

loop = True
num = 0
fibonacci_array = []

while loop:
    fibonacci_value = fibonacci(num)
    fibonacci_array.append(fibonacci_value)
    num += 1
    if fibonacci_value > 10000:
        loop = False
print(fibonacci_array)
# Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче
# нельзя использовать циклы — используйте рекурсию.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))

# решение нашел в сети, так и не понял этот алгоритм
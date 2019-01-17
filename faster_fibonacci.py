#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci_while(n):
    cache = {0:0,1:1}
    i = 2
    while i <= n:
        cache[i] = cache[i-1] + cache[i-2]
        i = i + 1

    return cache[n]


def fibonacci(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after , current + after

    return current





print(fibonacci_while(36))
print(fibonacci(36))
#>>> 14930352

# cache = {0:0,1:1}
# if 1 and 0 in cache:
#     print(cache[1])

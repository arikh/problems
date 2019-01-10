#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    cache = {0:0,1:1}
    i = 0
    while i <= n:
        if i == 0:
            return cache[0]
        if i == 1:
            return cache[1]
        if cache[i-1] and cache[i-2]:
            cache[i] = cache[i-1] + cache[i-2]
        n = n + 1

    return cache[i]






print(fibonacci(3))
#>>> 14930352

# cache = {0:0,1:1}
# if 1 and 0 in cache:
#     print(cache[1])

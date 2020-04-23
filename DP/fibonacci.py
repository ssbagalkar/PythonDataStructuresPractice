#https://www.youtube.com/watch?v=vYquumk4nWw
# This solution is not effective as it uses recursion and complexity is o(2^n)

# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

# optimized memoized solution

# https://www.youtube.com/watch?v=Qk0zUZW-U_M

fib_cache={}
def fib_memoized(n):
    # if we have already cached the value, then return it
    if n in fib_cache:
        return fib_cache[n]

    # Compute N-th term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fib_memoized(n-2)+ fib_memoized(n-1)

        # Cache the value and return
        fib_cache[n] = value
        return value

# https://avikdas.com/2019/04/15/a-graphical-introduction-to-dynamic-programming.html
# https://www.youtube.com/watch?v=5dRGRueKU3M
def fib_bottom_up(n):
    if n <=1:
        return n
    dp_array = [-1  for ii in range(n+1)]
    dp_array[0]=0
    dp_array[1]=1
    for ii in range(2, n + 1):  # end of range is exclusive
        dp_array[ii] = dp_array[ii-2] + dp_array[ii-1]
    return dp_array[n]

for n in range(1, 11):
    print(n, ":", fib_bottom_up(n))
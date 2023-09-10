#Write an implementation of the fibonacci sequence that computes the nth term of the sequence where n is a random number from 15 to 35 inclusive.


import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

#time the function
start_time = time.time()
#take user input between 15 and 35
n = int(input("Enter a number between 15 and 35: "))
#call the function
print(fib(n))
#time the function
# round secods to 3 decimel places
print("Time taken: {:.3f} seconds".format(time.time() - start_time))



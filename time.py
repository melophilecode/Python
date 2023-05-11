import time
 
 
# function to test elapsed time for
def print_square(x):
    return x ** 2
 
 
# records start time
start = time.perf_counter()
 
# calls the function
print_square(3)
 
# record end time
end = time.perf_counter()
 
# find elapsed time in seconds
ms = (end-start) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")

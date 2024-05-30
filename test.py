import timeit

code1_to_measure = """
def isPalindrome(x):
    x_string = str(x)
    x_reversed = x_string[::-1]
    if x_string == x_reversed:
        return True
    else:
        return False
"""

code2_to_measure = """
def isPalindrome(x):
    x = str(x)
    y = x[::-1]
    if x == y:
        return True
    else:
        return False
"""

code3_to_measure = """
def isPalindrome(x):
    return x == int(str(x)[::-1]) if x >= 0 else False
"""

runs = 1000
def measure_and_average(code, runs=20):
    times = timeit.repeat(code, number=100000, repeat=runs)
    return sum(times) / len(times)


# Measure and calculate average execution times
average_time1 = measure_and_average(code1_to_measure,runs)
average_time2 = measure_and_average(code2_to_measure,runs)
average_time3 = measure_and_average(code3_to_measure,runs)

# Create a list of tuples containing code and average execution time
code_average_times = [
    ("Peter, Code 1", average_time1),
    ("Sam, Code 2", average_time2),
    ("Maro, Code 3", average_time3),
]

# Sort the list based on average execution time
code_average_times.sort(key=lambda x: x[1])

# Print the results
for code, average_time in code_average_times:
    print(f"{code}: {average_time} seconds (average over {runs} runs)")

def fibonacci_generator(start=0, end=float('inf')):
    # Initialize the first two numbers in the Fibonacci sequence
    a, b = 0, 1
    
    # Continue generating Fibonacci numbers until the current number exceeds the specified end range
    while a < end:
        # Check if the current Fibonacci number is within the specified range
        if a >= start:
            # Yield the current Fibonacci number
            yield a
        
        # Update the Fibonacci sequence for the next iteration
        a, b = b, a + b

# Prompt the user to input the starting and ending ranges
start_range = int(input("Enter the starting range for Fibonacci sequence: "))
end_range = int(input("Enter the ending range for Fibonacci sequence: "))

# Create a Fibonacci generator with the specified range
fib_gen = fibonacci_generator(start_range, end_range)

# Print the Fibonacci sequence within the specified range
print("Fibonacci sequence in the specified range:")
for num in fib_gen:
    print(num)

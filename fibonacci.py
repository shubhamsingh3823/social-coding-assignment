def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

try:
    number = int(input("Enter a number: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        fib_seq = fibonacci_sequence(number)
        print("Fibonacci sequence up to {}:".format(number))
        print(fib_seq)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

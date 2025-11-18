def reverse_number(n):
    return int(str(n)[::-1])

def add_reversed_numbers(a, b):
    # Reverse the numbers back to their original form
    orig_a = reverse_number(a)
    orig_b = reverse_number(b)

    # Add the original numbers
    sum_orig = orig_a + orig_b

    # Reverse the sum
    reversed_sum = reverse_number(sum_orig)

    return reversed_sum

# Test the function
num1 = int(input("Enter first reversed number: "))
num2 = int(input("Enter second reversed number: "))
print("Reversed sum is:", add_reversed_numbers(num1, num2))
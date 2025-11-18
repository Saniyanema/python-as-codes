def last_digit_of_power(a, b):
    # Use modular exponentiation to avoid large numbers
    return pow(a, b, 10)

def main():
    try:
        N = int(input())
        for _ in range(N):
            a, b = map(int, input().split())
            print(last_digit_of_power(a, b))
    except Exception as e:
        # In a real application, you'd log this error
        pass

if __name__ == "_main_":
    main()
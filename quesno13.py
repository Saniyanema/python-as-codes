def find_last_stone(N):
    i = 1
    while N > 0:
        # Ramesh's turn
        stones_to_put = min(i, N)
        N -= stones_to_put
        if N == 0:
            return "Ramesh"
        # Suresh's turn
        stones_to_put = min(i * 2, N)
        N -= stones_to_put
        if N == 0:
            return "Suresh"
        i += 1

N = int(input())
print(find_last_stone(N))


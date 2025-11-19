
import math

def calculate_lcm_gcd(X, Y):
    gcd = math.gcd(X, Y)
    lcm = (X * Y) // gcd
    return lcm, gcd

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    lcm, gcd = calculate_lcm_gcd(X, Y)
    print(f"LCM: {lcm}, GCD: {gcd}")

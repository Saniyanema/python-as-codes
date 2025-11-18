a=int(input("enter first no of ap:"))
n=int(input("enter the nth term needed to calculate:"))
d=int(input("enter the common difference of the ap:"))

term= a + (n-1) * d
total = n * (2 * a + (n-1) * d //2)
print(term)
print(total)

def find_partners(N, X):
    partners = []
    for i in range(N):
        skill = int(input())
        if skill >= X:
            partners.append(i + 1)
    return partners

N = int(input())
X = int(input())
partners = find_partners(N, X)
if partners:
    print("Partners are:", partners)
else:
    print("No partners found")

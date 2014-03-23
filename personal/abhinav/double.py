# CodeChef - Practice - Easy
# Double Strings and Palindromes
# PROBCODE: DOUBLE

def maxDS(a):
    if a%2 is 0:
        return a
    else:
        return a-1


i = int(input())
for _ in range(i):
    print(maxDS(int(input())))

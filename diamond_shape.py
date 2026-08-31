'''n = int(input('Enter width of diamond: '))

for i in range(1,n+1):
    print((n-i)*' '+'* '*i)
for i in range(n-1,0,-1):
    print((n-i)*' '+'* '*i)'''
n = int(input("Enter width of diamond: "))

for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    print(" " * (n - i) + "* " * i)
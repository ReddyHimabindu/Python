#Find the factors of a number using while loop
n= int(input("Enter a number to find its factor: "))
print (1, end=' ')
factor = 2
while factor <= n :
    if num % factor == 0:
        print(factor, end=' ')
    factor += 1

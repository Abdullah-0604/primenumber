p = 600851475143 

n = 2 

while n * n < p:

    while p%n == 0:

        p = p / n

    n = n + 1

print (p)
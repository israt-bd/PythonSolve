import math
n = input()
y = int(n)

a = int("%i" % y)
b = int("%i%i" % (y,y))
c = int("%i%i%i" % (y,y,y))

sum = a+b+c

print(sum)
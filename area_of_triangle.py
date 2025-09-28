x = float(input("x:"))
y = float(input("y:"))
z = float(input("z:"))

q = (x + y + z)/2

area = (q*(q-x)*(q-y)*(q-z)) ** 0.5

print("area of triangle:", area)


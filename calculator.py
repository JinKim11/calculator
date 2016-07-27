def add(num1, num2):
	return num1 + num2
def subtract(num1, num2):
	return num2 - num1
def multiply (num1, num2):
	return num1 * num2
def divide (num1, num2):
	return num1 / num2
def modulo (num1, num2):
	return num1 % num2
def power (base, exponent):
	return base ** exponent
def square (num):
	return power(num, 2)
def subtract2 (num1, num2):
	return (num1 - num2)

print power(3,(add (2,3)))

print subtract2(add(1,2), multiply(3, add(4,5)))

print multiply(7, add(3,8))

print divide(modulo(3,4), multiply(9,9)) 

print square(add(1, 2))

print add (1,2) + 3

print add (4,5) + subtract (6,9)

print divide (12,2) - 60


print square (4)

print power (4,5)

print modulo (4,5)

print divide (4,5)

print multiply (4,5)

print subtract (4,5)

print add (4,5)

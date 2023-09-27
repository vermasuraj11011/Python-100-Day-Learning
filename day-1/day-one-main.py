print("hello")

name = input("What is your name ?\n")
print("hello " + name)
print("your name has " + str(len(name)) + " character")

a = int(input("enter value of 'a' \n"))
b = int(input("enter value of 'b' \n"))

temp = a
a = b
b = temp

print("Value of a: " + str(a))
print("Value of b: " + str(b))

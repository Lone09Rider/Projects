import random
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
y = "abcdefghijklmnopqrstuvwxyz"
z = "!@#$%^&*()_+=-?|\/.,<>"
a = "1234567890"

p = x + y + z + a
length = 8
password = "".join(random.sample(p,length))
print(password)

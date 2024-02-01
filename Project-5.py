import random

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
    , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
c = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=']

p = int(input("How many alphabets do you want in your password? :  "))
q = int(input("How many numbers do you want in your password? :  "))
r = int(input("How many symbols do you want in your password? :  "))

n = []
x = ""

for i in range(0, p):
    n.append(random.choice(a))
for i in range(0, q):
    n.append(random.choice(b))
for i in range(0, r):
    n.append(random.choice(c))

random.shuffle(n)

for i in range(0, p+q+r):
    x += n[i]

print(f"Your Password Is : {x}.")

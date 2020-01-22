def add(a, b):
    #print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    #print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    #print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    #print(f"DIVIDING {a} / {b}")
    return a / b

simpel = 1337 + 42 - 13 / 7 * 666

leet = 1000 + 337
answer = 42
unlucky = 10 + 3
lucky = 7
devil = 667 - 1

echtsimpel = add(leet, subtract(answer, multiply(devil, divide(unlucky, lucky))))

print(simpel)
print(echtsimpel)

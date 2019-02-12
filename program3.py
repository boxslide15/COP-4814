def programThree(x):
    return {x : x * x for x in range(1, x + 1)}

x = int(input("Please enter an integer: "))

print(programThree(x))
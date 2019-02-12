def programSeven(a, b):
    programSeven = [i for i in a if (i in b)]
    return programSeven

a = [1, 2, 3, 3, 4, 4, 7, 9]

b = [3, 4, 4, 5, 6, 7]

print(programSeven(a, b))
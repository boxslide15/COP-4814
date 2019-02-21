def programOne():
    start = 2000
    stop = 3201
    for i in range(start, stop + 1):
        if i % 7 == 0:
            if i % 5 != 0:
                print(i)

print(programOne())
def fibonacci(N):
    a = 0
    if N > 0:
        yield a
        N -= 1
    b = 1
    if N > 0:
        yield b
        N -= 1
    while N > 0:
        a , b = b, a + b
        yield b
        N -= 1

sequence_1 = fibonacci(10)
for i in sequence_1:
    print(i,end=' ')
import time 

start = time.time()

n = 0
d = 0
while (True):
    n += 1
    d += n

    div = 0
    for i in range(1, int(d ** 0.5) + 1):
        if d % i == 0:
            div += 2

        if int(d ** 0.5) * int(d ** 0.5) == d:
            div -= 1
            
    if div > 500:
        print(d)
        break

print(time.time() - start)

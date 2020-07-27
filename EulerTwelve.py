import time
start = time.time()

n = 0
d = 0

def divisors(d):
    
    prev = 1
    for i in range(2, d//2 + 1):
        c = 0
        if d%i == 0:
            while d%i == 0:
                c += 1
                d /= i
        if c != 0:
            prev = prev * (c + 1)
        if d == 1:
            return prev
    return prev

while True:
    n += 1
    d += n
    
    if divisors(d) > 500:
        print(d)
        break
print(time.time() - start)

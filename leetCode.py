a = int(input())
b = int(input())
i = 1
count = 0  
while i <= min(a, b):
    if a % i == 0 and b % i == 0:
        count += 1  
    i += 1
print(count)

n=77833

for i in range(2,n):
    if n % i == 0:
        print(False)
        exit()
print(True)
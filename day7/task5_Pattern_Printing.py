print("---method 1: string multiplication---")
for i in  range(1,6):
    print("*" * i)

print()

print("---method 2: nested loop---")

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()    
names = set()

for _ in range(int(input())):
    names.add(input())

#print("\n".join(names))
print(*names, sep="\n")
n = int(input("n = "))

list = []
for i in range(n + 1):
    list.append(i)
list[1] = 0
i = 2
while i <= n:
    if list[i] != 0:
        j = i + i
        while j <= n:
            list[j] = 0
            j = j + i
    i += 1
list = set(list)
list.remove(0)
print(list)
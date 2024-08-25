import random

n = random.choice(range(3, 21))
print(n)
gt = []
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            gt.append([str(i), str(j)]) #Записываем пару в словарь, если пара кратна указанному числу и этой пары нет в списке
password = ''
for k in gt:
    password += ''.join(k)
print(gt)
print(password)
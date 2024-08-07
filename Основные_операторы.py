import random

n = random.choice(range(3, 21))
print(n)
gt = []
for i in range(1, n):
    for j in range(1, n):
        if i == j or i + j > n:
            continue #Пропускаем пару, если числа равны между собой или их сумма больше указанного числа
        elif n % (i + j) == 0 and [str(i), str(j)] not in gt and [str(j), str(i)] not in gt:
            gt.append([str(i), str(j)]) #Записываем пару в словарь, если пара кратна указанному числу и этой пары нет в списке
password = ''
for k in gt:
    password += ''.join(k)
print(gt)
print(password)
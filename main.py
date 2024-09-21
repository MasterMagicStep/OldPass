n = int(input('Введите целое число от 3 до 20: '))
def GetPassword(num):
    pas = ''
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            if num% (i + j) == 0:
                pas += str(i) + str(j)
    return pas


result = GetPassword(n)
print('Пароль:', result)
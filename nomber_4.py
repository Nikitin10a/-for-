K = int(input("Введите первое число: "))
N = int(input("Введите второе число: "))

sum = 0

for x in range (K+K%2, N+1, 2):
    sum += x
    print(sum)
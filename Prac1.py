"""#"""
import math

#Завдання1
first_name = input('Введіть імʼя: ')
last_name = input('Введіть прізвище: ')
birth_year = input('Введіть рік народження: ')
#A
print(first_name, last_name, birth_year, sep = ',')
#B
print(first_name, last_name, birth_year,sep = '\n')

print()

#Завдання2
a = int(input('Перше число: '))
b = int(input('Друге число: '))

#1
print('Сума:',sum((a,b)))
print()
#2
print('Різниця:',a-b)
print()
#3
print('Множення:',a*b)
print()
#4
print('Середнє арифметичне:',(a+b)/2)
print()
#5
print('Середнє геометричне:',(a*b)**0.5)
print()
#6
print('Абсолютне значення різниці:',abs(a-b))
print()
#7
print('Максимум:',max(a,b))
print()
#8
print('Мінімум:',min(a,b))
print()
#9
print('Сума квадратів:',a^2 + b^2)
print()
#10
print('Квадрат суми:',(a+b)**2)
print()
#11
print('a в степені b:',a^b)
print()


#Завдання3
num = (input('Введіть число: '))
total = None
for i in num:
    total = sum(int(i) for i in num)
print('+'.join(num),'=',total)

print()

#Завдання4
a = int(input('Введіть a: '))
b = int(input('Введіть b: '))
c = int(input('Введіть c: '))
d = b**2 - 4*a*c
x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)
x3 = -b / (2*a)

equation1 = None
equation2 = None
equation3 = None

if d > 0:
    equation1 = a*(x1**2) + b*x1 + c
    equation2 = a*(x2**2) + b*x2 + c
    print('Є два різних дійсних корені:')
    print('Корінь 1:',round(x1,2))
    print('Корінь 2:',round(x2,2))
elif d == 0:
    equation3 = a*(x3**2) + b*x3 + c
    print('Є один подвійний корінь:')
    print('Корінь:',round(x3,2))
elif d < 0:
    print('Дійсних коренів немає')

print()

#Завдання5
s0 = float(input('Введіть s0: '))
v0 = float(input('Введіть v0: '))
t = float(input('Введіть t '))
g = 9.81
INT = float(input('Введіть INT: '))
YRS = float(input('Введіть YRS: '))
a = float(input('Введіть a: '))
b = float(input('Введіть b: '))
y = float(input('Введіть y: '))
m1 = float(input('Введіть m1: '))
m2 = float(input('Введіть m2: '))
p = float(input('Введіть p: '))
PV = float(input('Введіть PV: '))

s = s0 + v0 * t + 1/2 * g * t^2
FV = PV *((1 + INT/100)^YRS)
G = 4 * math.pi^2 * (a^3/p^2(m1 + m2))
c = math.sqrt(a^2 + b^2 - 2*a*b*math.cos(y))


#Завдання6
x = float(input('Введіть x: '))
drib = print('Дробова частина:',x - abs(int(x)))

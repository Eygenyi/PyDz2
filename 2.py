s=int(input('введите сумму чисел '))
p=int(input('введите произведение чисел '))
x=0
y=0
for x in range(1000):
    for y in range(1000):
        if s==x+y and p==x*y:
            print('первое число =',x,'второе число =',y)

s=int(input('введите сумму чисел '))
p=int(input('введите произведение чисел '))
x=0
y=0
# for x in range(1000):
#     for y in range(1000):
#         if s==x+y and p==x*y:
#             print('первое число =',x,'второе число =',y)
while x<1000:
    while y<1000:
        if s==x+y and p==x*y:
            print('первое число =',y)
            print('второе число =',x)

    y+=1
x+=1

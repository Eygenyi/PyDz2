import random
mon=int(input("кол-во монет:" ))
arr=[]
i=0
count1=0
count2=0
for i in range(mon):
    arr.append(random.randint(0, 1))
    if arr[i]==0:
        count1+=1
    elif arr[i]==1:
        count2+=1
print(arr)
if count1>count2:
    print('перевернуть монет : ',count2)
else:
    print('перевернуть монет : ',count1)

    

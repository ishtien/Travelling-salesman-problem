import numpy
import random
import math
import copy
import time

#讀檔
#array = numpy.loadtxt('D:\python\gr17_d.txt')
array = numpy.loadtxt('gr17_d.txt')

#初始排序
order=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#設定T1
T1=500
x1=0
x2=0

#初始解
for i in range(0,16):
    x1=x1+array[i][(i+1)%17]

#計算時間開始
start_time=time.time()

#n=120
for n in range(1,110):
    x2=0
    swap1=random.randint(0,16)
    swap2=random.randint(0,16)
    ordertest=order.copy()

    #隨興選兩個交換節點交換
    ordertest[swap1],ordertest[swap2]=ordertest[swap2],ordertest[swap1]

    #計算新的path長度
    for i in range(0,16):
        x2=x2+array[ordertest[i]][ordertest[(i+1)%17]]

    print(x2)

    #如果新的path較長，進行p跟y之比對
    if x2>x1:
        p=random.uniform(0,1)
        print('p:' + str(p))
        y=math.exp((-(x2-x1))/T1)
        print('y:' + str(y))
        if p<y: 
            #print('hiiii')
            order=ordertest.copy()
            x1=x2
    #如果新的path較短，置換
    else:
        order=ordertest.copy()
        x1=x2

    #將溫度更新
    T1=0.95*T1
    print(order)
    ans=0
    for i in range(0,16):
        ans=ans+array[order[i]][order[(i+1)%17]]

#印出結果
print('ans:'+str(ans))
print("--- %s seconds ---" % (time.time() - start_time))
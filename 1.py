from random import randint

flag = False
while flag == False:
    arr = [randint(10,100) for i in range (15)]
    arr.sort()
    arr.reverse()
    if arr[1] + arr[2] > arr[0]:
        per = (arr[0] + arr[1] +arr[2]) * 0.5
        print((per * (per - arr[0])*(per - arr [1]) * (per - arr[2])) ** 0.5)
        flag = True

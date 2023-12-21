import random
import datetime
import time
def wow():
    a = [i for i in range(1,46)]
    now = datetime.datetime.now()
    print("************오늘의 로또 추첨************")
    print("%d 년 %d 월 %d 일" %(now.year, now.month, now.day))
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    print("결과는!!!")
    for i in range(7):
        c = random.choice(a)
        a.remove(c)
        print(c)
wow()
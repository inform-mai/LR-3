from random import *
import logging
logging.basicConfig(level=logging.DEBUG,filename='Sorting_1.log',filemode='w',format="%(asctime)s %(levelname)s %(message)s")

def bubble_sort(list):
    logging.debug('START')
    flag = True
    cnt_iter = 0
    while flag:
        cnt_iter+=1
        flag = False
        for i in range(len(list)-1):
            cnt_iter+=1
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1], list[i]
                flag = True
    print(f'Количество итераций: {cnt_iter}')
    logging.debug('END')

my_list = [randint(-10**3,10**3) for _ in range(10)]
bubble_sort(my_list)
print(my_list)
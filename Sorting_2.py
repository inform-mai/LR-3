from random import *
import logging
logging.basicConfig(level=logging.DEBUG,filename='Sorting_2.log',filemode='w',format="%(asctime)s %(levelname)s %(message)s")

def insert_sorting(list):
    cnt_iter = 0
    logging.debug('START')
    for i in range(1,len(list)):
        cnt_iter+=1
        j=i-1
        insert_item = list[i]
        while j>=0 and list[j]>insert_item:
            cnt_iter+=1
            list[j+1]=list[j]
            j-=1
        list[j+1] = insert_item
    logging.debug('END')
    print(f'Количество итераций: {cnt_iter}')

my_list =[randint(-10**3,10**3) for _ in range(10)]
insert_sorting(my_list)
print(my_list)
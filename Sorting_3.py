from random import *
import logging
logging.basicConfig(level=logging.DEBUG,filename='Sorting_3.log',filemode='w',format="%(asctime)s %(levelname)s %(message)s")
#Сортировка выборкой
def selection_sort(list):
    logging.debug('START')
    cnt_iter = 0
    for i in range(len(list)):
        cnt_iter+=1
        mn_ind=i
        for j in range(i+1,len(list)):
            cnt_iter+=1
            if list[j]<list[mn_ind]:
                mn_ind=j
        list[i],list[mn_ind]=list[mn_ind],list[i]
    logging.debug('END')
    print(f'Количество итераций: {cnt_iter}')

my_list=[randint(-10**3,10**3) for _ in range(10)]
selection_sort(my_list)
print(my_list)
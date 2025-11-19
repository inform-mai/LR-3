from random import *
import logging
logging.basicConfig(level=logging.DEBUG,filename='Sorting_6.log',filemode='w',format="%(asctime)s %(levelname)s %(message)s")
cnt_iter=0
def quick_sort(arr):
    logging.debug('DEBUG')
    global cnt_iter
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    cnt_iter+=len(arr[:-1])
    right = [x for x in arr[:-1] if x >= pivot]
    cnt_iter += len(arr[:-1])
    logging.debug('DEBUG')
    return quick_sort(left) + [pivot] + quick_sort(right)


my_list=[randint(-10**3,10**3) for _ in range(10)]
sorted_list=quick_sort(my_list)
print(f'Количество итераций: {cnt_iter}')
print(sorted_list)
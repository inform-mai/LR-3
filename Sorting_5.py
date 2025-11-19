from random import *
import logging
logging.basicConfig(level=logging.DEBUG,filename='Sorting_5.log',filemode='w',format="%(asctime)s %(levelname)s %(message)s")
cnt_iter=0
def merge_sort(arr):
    logging.debug('DEBUG')
    global cnt_iter
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    logging.debug('DEBUG')
    return merge(left, right)

def merge(left, right):
    global cnt_iter
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        cnt_iter+=1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


my_list=[randint(-10**3,10**3) for _ in range(10)]
my_list_sorted = merge_sort(my_list)
print(f'Количество итераций: {cnt_iter}')
print(my_list_sorted)

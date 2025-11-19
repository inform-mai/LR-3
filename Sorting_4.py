from random import *
import logging
logging.basicConfig(level=logging.DEBUG,filename='Sorting_4.log',filemode='w',format="%(asctime)s %(levelname)s %(message)s")


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    cnt_iter=0
    logging.debug('START')
    n = len(nums)
    for i in range(n, -1, -1):
        cnt_iter+=1
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        cnt_iter+=1
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    logging.debug('END')
    print(f'Количество итераций: {cnt_iter}')

my_list = [randint(-10**3,10**3) for _ in range(10)]
heap_sort(my_list)
print(my_list)
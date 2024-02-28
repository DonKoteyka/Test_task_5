import numpy as np
import copy
import datetime

def comb_sort(array):
    """
    уже придумано множество методов сортировок, для эталона я выбрал сортировку расчёской https://habr.com/ru/articles/204600/
    """

    start_1 = datetime.datetime.now()
    run = copy.copy(array)
    n = len(run)
    gap = n
    shrink = 1.247
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False
        for i in range(n - gap):
            if run[i] > run[i + gap]:
                run[i], run[i + gap] = run[i + gap], run[i]
                swapped = True
    print("время выполнения сортировки расчёской: " + str(datetime.datetime.now() - start_1))
    return run

def strage_sort(array):
    """
    но решил написать собственную сортировку, получилось не так локонично, но работает
    """
    start_2 = datetime.datetime.now()
    cache = list()
    ram = list()
    min_array = min(array)
    ram.append(min_array)
    for i in array:
        if i == min_array:
            pass
        elif ram[-1] <= i:
            ram.append(i)
        else:
            cache.append(i)
    ram_max = max(ram)
    for i in cache:
        for index, value in enumerate(ram):
            if index == 0:
                    pass
            elif value > i:
                ram.insert(index, i)
                break
            elif i > ram_max:
                    ram.append(i)

    print("время выполнения странной сортировки : " + str(datetime.datetime.now() - start_2))
    return ram

if __name__ == "__main__":
    array = np.random.randint(1, 99999, 700)

    result_1 = strage_sort(array)
    result_2 = comb_sort(array)

    print("Отсортированный массив:")
    for i in result_1:
        print(i, end=" < ")
    # print(result_1 == result_2)

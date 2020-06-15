#耗cpu的操作使用多进程
#切换成本高

#1.计算
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# if __name__ == "__main__":
#
#     with ThreadPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib,(num)) for num in range(35,40)]
#         start = time.time()
#         for future in as_completed(all_task):
#             data =future.result()
#             print('result:',data)
#         print(time.time()-start)

#2.对于io操作来说

def random_sleep(n):
    time.sleep(n)
    return n
if __name__ == "__main__":

    with ProcessPoolExecutor(10) as executor:
        all_task = [executor.submit(random_sleep,(num)) for num in [2]*10]
        start = time.time()
        for future in as_completed(all_task):
            data =future.result()
            print('result:',data)
        print(time.time()-start)

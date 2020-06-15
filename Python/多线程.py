# import threading
# import time
# def doFirstThing(url):
#     print("First Thing Star")
#     time.sleep(2)
#     print('First Thing Finished')
#
# def doSecondThing(url):
#     print("Second Thing Star\n")
#     time.sleep(4)
#     print('Second Thing Finished')
#
# if __name__ == "__main__":
#     thread1 = threading.Thread(target=doFirstThing,args=("",))
#     thread2 = threading.Thread(target=doSecondThing, args=("",))
#     start_time = time.time()
#
#     # thread1.setDaemon(True)
#     # thread2.setDaemon(True)
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     end = time.time()
#     print('time:%s'%(end-start_time))
import threading
import time
class doFirstThing(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print("First Thing Star")
        time.sleep(2)
        print('First Thing Finished')


class doSecondThing(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("Second Thing Star")
        time.sleep(4)
        print('Second Thing Finished')

if __name__=="__main__":

    thread1 = doFirstThing('FirstThing')
    thread2 = doSecondThing('SecondThing')
    start_time = time.time()

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end = time.time()
    print('time:%s'%(end-start_time))
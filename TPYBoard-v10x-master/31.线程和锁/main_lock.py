import _thread
import time
 
lock=_thread.allocate_lock()
 
def myThread_A():
    print('我是 thread A-')
    _thread.exit()
 
 
def myThread_B(time_):
    time.sleep(time_)
    if lock.acquire():#锁住资源
        print('我是 thread B-')
        print('我是 thread B- Sleep 5s')
        time.sleep(5)
        print('我是 thread B-Wake up')
        lock.release()#打开锁 释放资源
    _thread.exit()
 
def myThread_C(time_):
    time.sleep(time_)
    if lock.acquire():#B先抢到了资源 需等待B释放后才能占有
        print('我是 thread C-')
        lock.release()
    _thread.exit()
 
_thread.start_new_thread(myThread_A, ())
_thread.start_new_thread(myThread_B, (2,))
_thread.start_new_thread(myThread_C, (3,))
 
while True:
    pass
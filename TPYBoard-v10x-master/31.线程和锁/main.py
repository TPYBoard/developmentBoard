import _thread
import time
 
lock=_thread.allocate_lock()
 
def myThread_A():
    print('我是 thread A-')
    _thread.exit()
 
 
def myThread_B(time_):
    time.sleep(time_)
    print('我是 thread B-')
    print('我是 thread B- Sleep 5s')
    time.sleep(5)
    print('我是 thread B-Wake up')
    _thread.exit()
 
def myThread_C(time_):
    time.sleep(time_)
    print('我是 thread C-')
    _thread.exit()
 
_thread.start_new_thread(myThread_A, ())
_thread.start_new_thread(myThread_B, (2,))
_thread.start_new_thread(myThread_C, (3,))
 
while True:
    pass
import time, threading


# 新线程执行的代码:
def loop():
    """
     线程
    """
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()  # 等待线程结束的时间，没有参数就是一直等待线程结束为止
print('thread %s ended.' % threading.current_thread().name)

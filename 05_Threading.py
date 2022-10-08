import logging
import threading
import time,os
import concurrent.futures

# def my_func():
#     print("hello")
#     time.sleep(10)
#     return True
# if __name__=='__main__':
#     my_func()
# ======================

# def my_func(name):
#     print(f"my_func startd {name}")
#     time.sleep(10)
#     print("my_func ended")
# if __name__=='__main__':
#     print('Main started')
#     t=threading.Thread(target=my_func, args=["python learning"])
#     t.start()
#     print("main ended")
# ==================================
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#
#     logging.info("Main    : all done")

# ===============================
# Deamon thread : If a thread is running as deamon thread it will be terminated once main is exited

# from threading import *
#
# print(current_thread().isDaemon())
#
# print(current_thread().daemon)

# =====================
# import module
# from threading import *
#
# def fun_daemon():
#     print("GFG")
#
# thread_1 = Thread(target=fun_daemon)
# print(thread_1.isDaemon())
# thread_1.start()
# print(thread_1.daemon)
# ================
#
# def fun():
#     print("Geeks For Geeks")
#
#
# T = Thread(target=fun)
#
# print("GFG")
# print(T.isDaemon())
#
# # set thread as Daemon
# T.setDaemon(True)
#
# # check status
# print(T.isDaemon())
# T.start()

# =================

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(10)
#     logging.info("Thread %s: finishing", name)
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,),daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     logging.info("Main    : all done")
# ===========================================
'''thread.start_new_thread ( function, args[, kwargs] )

run(): It is the entry point function for any thread.

start(): The start() method triggers a thread when run method is called.

join([time]): The join() method enables a program to wait for threads to terminate.

isAlive(): The isAlive() method verifies an active thread.

getName(): The getName() method retrieves the name of a thread.

setName(): The setName() method updates the name of a thread.'''
# ======================
# To tell one thread to wait for another thread to finish, you call .join().
# the main thread will pause and wait for the thread x to complete running.

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(8)
#     logging.info("Thread %s: finishing", name)
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join()
#     logging.info("Main    : all done")
# ============================

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()
#
#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)
# =========================
'''There’s an easier way to start up a group of threads than the one you saw above. 
It’s called a ThreadPoolExecutor.
'''
#
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function, range(3))
# ===========================

# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print( "%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # Create two threads as follows
# t1 = threading.Thread(target=print_time, args=("Thread-1", 2, ))
# t1.start()
# t2 = threading.Thread(target=print_time, args=("Thread-2", 4, ))
# t2.start()
# ======================
# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("Cube: {}".format(num * num * num))
#
#
# def print_square(num):
#     """
#     function to print square of given num
#     """
#     print("Square: {}".format(num * num))
#
#
# if __name__ == "__main__":
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
#
#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()
#
#     # wait until thread 1 is completely executed
#     t1.join()
#     # wait until thread 2 is completely executed
#     t2.join()
#
#     # both threads completely executed
#     print("Done!")

# ========================

# def task1():
#     print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 1: {}".format(os.getpid()))
#
#
# def task2():
#     print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 2: {}".format(os.getpid()))
#
#
# if __name__ == "__main__":
#     # print ID of current process
#     print("ID of process running main program: {}".format(os.getpid()))
#
#     # print name of main thread
#     print("Main thread name: {}".format(threading.main_thread().name))
#
#     # creating threads
#     t1 = threading.Thread(target=task1, name='t1')
#     t2 = threading.Thread(target=task2, name='t2')
#
#     # starting threads
#     t1.start()
#     t2.start()
#
#     # wait until all threads finish
#     t1.join()
#     t2.join()
# ======================
import time
# from threading import Thread
#
# def sleepMe(i):
#     print("Thread %i going to sleep for 5 seconds." % i)
#     time.sleep(5)
#     print("Thread %i is awake now." % i)
#
# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()
#    ============================

# import time
# import threading
# from threading import Thread
#
# def sleepMe(i):
#     print("Thread %i going to sleep for 5 seconds." % i)
#     time.sleep(5)
#     print("Thread %i is awake now." % i)
#
# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()
#     print("Current Thread count: %i." % threading.active_count())
# ========================
# Race condition
# import threading
#
# # global variable x
# x = 0
#
# def increment():
# 	"""
# 	function to increment global variable x
# 	"""
# 	global x
# 	x += 1
#
# def thread_task():
# 	"""
# 	task for thread
# 	calls increment function 100000 times.
# 	"""
# 	for _ in range(100000):
# 		increment()
#
# def main_task():
# 	global x
# 	# setting global variable x as 0
# 	x = 0
#
# 	# creating threads
# 	t1 = threading.Thread(target=thread_task)
# 	t2 = threading.Thread(target=thread_task)
#
# 	# start threads
# 	t1.start()
# 	t2.start()
#
# 	# wait until threads finish their job
# 	t1.join()
# 	t2.join()
#
# if __name__ == "__main__":
# 	for i in range(10):
# 		main_task()
# 		print("Iteration {0}: x = {1}".format(i,x))

# ===========================
# import threading
#
# # global variable x
# x = 0
#
# def increment():
# 	"""
# 	function to increment global variable x
# 	"""
# 	global x
# 	x += 1
#
# def thread_task(lock):
# 	"""
# 	task for thread
# 	calls increment function 100000 times.
# 	"""
# 	for _ in range(100000):
# 		lock.acquire()
# 		increment()
# 		lock.release()
#
# def main_task():
# 	global x
# 	# setting global variable x as 0
# 	x = 0
#
# 	# creating a lock
# 	lock = threading.Lock()
#
# 	# creating threads
# 	t1 = threading.Thread(target=thread_task, args=(lock,))
# 	t2 = threading.Thread(target=thread_task, args=(lock,))
#
# 	# start threads
# 	t1.start()
# 	t2.start()
#
# 	# wait until threads finish their job
# 	t1.join()
# 	t2.join()
#
# if __name__ == "__main__":
# 	for i in range(10):
# 		main_task()
# 		print("Iteration {0}: x = {1}".format(i,x))
# ====================

#
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0
#
#     def update(self, name):
#         logging.info("Thread %s: starting update", name)
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
#         logging.info("Thread %s: finishing update", name)
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     database = FakeDatabase()
#     logging.info("Testing update. Starting value is %d.", database.value)
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for index in range(2):
#             executor.submit(database.update, index)
#     logging.info("Testing update. Ending value is %d.", database.value)
# =====================================
class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
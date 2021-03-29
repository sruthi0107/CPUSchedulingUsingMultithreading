import threading
from FCFS import findavgTime_FCFS,findTurnAroundTime_FCFS,findWaitingTime_FCFS
from SJF import findavgTime_SJF,findTurnAroundTime_SJF,findWaitingTime_SJF
import tkinter as tk
import time

start = time.time()
processes = [ 1, 2, 3]
n = len(processes)

# Burst time of all processes
burst_time = [10, 5, 8]

proc = [[1, 6, 1], [2, 8, 1],
        [3, 7, 2], [4, 3, 3]]
n1 = 4


t1 = threading.Thread(target=findavgTime_FCFS, args=(processes, n, burst_time,))
t2 = threading.Thread(target=findavgTime_SJF, args=(proc,n1,))

t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

end=time.time()
# both threads completely executed
print(f"Runtime of the program is {end - start}")
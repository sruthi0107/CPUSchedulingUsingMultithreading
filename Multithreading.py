#import threading
import tkinter as tk
import time
import pygame
import numpy as np
from FCFS import fcfs, findTurnAroundTime_FCFS, findWaitingTime_FCFS
from SJF import sjf
from subprocess import *

# Defining process Ids
processes = [ 1, 2, 3, 4]
n = len(processes)

# Burst time of all processes
burst_time = [3, 8, 4, 6]

Popen('python FCFS.py')
time.sleep(1)
Popen('python SJF.py')

'''
t1 = threading.Thread(target=fcfs, args=(processes, n, burst_time,))
t2 = threading.Thread(target=sjf,  args=(processes, n, burst_time,))

t1.start() #starting thread1
t2.start() #starting thread2

t1.join()  # wait until thread 1 is completely executed
t2.join()  # wait until thread 2 is completely executed
'''
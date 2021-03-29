import tkinter as tk
import numpy as np
import pygame
import time

def findWaitingTime_FCFS(processes, n, bt, wt):
    pygame.init()
    screen = pygame.display.set_mode((350, 350))
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    grid=np.zeros((35,35))
    wt[0] = 0
    tat = [0] * n
    grid[0,wt[0]:bt[0]]=1
    done=False
    while not done:
        pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(0, wt[0], (bt[0])*10,10))
        pygame.display.flip()
        for i in range(1, n ):
            wt[i] = bt[i - 1] + wt[i - 1] 
            pygame.time.delay(2000)
            pygame.draw.rect(screen, (0, 50*i, 50), pygame.Rect(wt[i]*10,i*10,  (bt[i])*10,10))
            pygame.display.flip()
            clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

def findTurnAroundTime_FCFS(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def FCFS( processes, n, bt):
    wt = [0] * n
    tat = [0] * n 
    total_wt = 0
    total_tat = 0
    findWaitingTime_FCFS(processes, n, bt, wt)
    findTurnAroundTime_FCFS(processes, n, bt, wt, tat)
    '''
    print( "Processes Burst time " + 
                  " Waiting time " + 
                " Turn around time")
  
    # Calculate total waiting time 
    # and total turn around time
    for i in range(n):
      
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" + 
                    str(bt[i]) + "\t " + 
                    str(wt[i]) + "\t\t " + 
                    str(tat[i])) 
  
    print( "Average waiting time = "+
                   str(total_wt / n))
    print("Average turn around time = "+
                     str(total_tat / n))
    '''
    root=tk.Tk()
    string="Processes Burst time " + " Waiting time " + " Turn around time"
    tk.Label(root, text=string).pack()
    for i in range(n):
        string=""
        # Calculate total waiting time and total turn around time
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        string+=" " + str(i + 1) + "\t" + \
                    str(bt[i]) + "\t " + \
                    str(wt[i]) + "\t\t " + \
                    str(tat[i]) 
        tk.Label(root,text=string).pack()
    
    tk.Label(root,text="Average waiting time = "+str(total_wt / n)).pack()
    tk.Label(root,text="Average turn around time = "+str(total_tat / n)).pack()
    root.mainloop()
  
# Driver code
if __name__ =="__main__":
    processes = [ 1, 2, 3, 4]
    n = len(processes)
    burst_time = [3, 8, 4, 6]
    FCFS(processes, n, burst_time)
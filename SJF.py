import pygame
import tkinter as tk
import time
def SJF(processes,n,bt):
    #Applying bubble sort to sort process according to their burst time
    for i in range(0,n-1): 
        for j in range(0,n-i-1):
            if(bt[j]>bt[j+1]):
                temp=bt[j]
                bt[j]=bt[j+1]
                bt[j+1]=temp
                temp=processes[j]
                processes[j]=processes[j+1]
                processes[j+1]=temp
    
    #pygame-gantt chart
    wt,tat=[],[] 
    total_wt=0
    total_tat=0

    wt.insert(0,0)
    tat.insert(0,bt[0])

    pygame.init()
    screen = pygame.display.set_mode((350, 350))
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    done=False
    while not done:
            pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(0, wt[0], (bt[0])*10,10))
            pygame.display.flip()
            for i in range(1,n):  
                wt.insert(i,wt[i-1]+bt[i-1])
                tat.insert(i,wt[i]+bt[i])
                wt[i] = bt[i - 1] + wt[i - 1] 
                pygame.time.delay(2000)
                pygame.draw.rect(screen, (0, 50*i, 50), pygame.Rect(wt[i]*10,i*10,  (bt[i])*10,10))
                pygame.display.flip()
                clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

    #Tkinter screen for printing details
    root=tk.Tk()
    string="Processes Burst time " + " Waiting time " + " Turn around time"
    tk.Label(root, text=string).pack()
    for i in range(n):
        string=""
        # Calculate total waiting time and total turn around time
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        string+=" "+ str(i + 1) + "\t" + \
                    str(bt[i]) + "\t " + \
                    str(wt[i]) + "\t\t " + \
                    str(tat[i]) 
        tk.Label(root,text=string).pack()
    
    tk.Label(root,text="Average waiting time = "+str(total_wt / n)).pack()
    tk.Label(root,text="Average turn around time = "+str(total_tat / n)).pack()
    root.mainloop()

#Driver Code
if __name__ =="__main__":
    processes = [ 1, 2, 3, 4]
    n = len(processes)
    burst_time = [3, 8, 4, 6]
    SJF(processes, n, burst_time)
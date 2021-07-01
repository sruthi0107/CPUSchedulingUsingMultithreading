import pygame
import tkinter as tk
# Function to find the waiting time for all processes 
def findWaitingTime(processes, n, wt): 
    color=[(255,0,0),(25, 255, 228),(0,128,0),(0,0,128),(255,255,0)]
    def drawGrid():
        blockSize = 10 #Set the size of the grid block
        for x in range(0, 350, 10):
            for y in range(0, 160, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen3, (0,0,0), rect, 1)
    rt = [0] * n
    tat = [0] * n
    pygame.init()
    screen3 = pygame.display.set_mode((350, 350))
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 13)
    screen3.fill((255, 255, 255))
    
    # Copy the burst time into rt[] 
    for i in range(n): 
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
    done=False
    i=0
    k=0
    order=[]
    order.append(0)

    # Process until all processes gets  completed 
    while not done:
        pygame.event.get()
        drawGrid()
        while (complete != n):
            
            # Find process with minimum remaining time among the processes that arrives till the current time`
            for j in range(n):
                if ((processes[j][2] <= t) and 
                    (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
            if (check == False):
                t += 1
                continue
                
            # Reduce remaining time by one 
            rt[short] -= 1
            order.append(short)
            if(order[-2]==short):
                pygame.draw.rect(screen3, color[short], pygame.Rect(k*10,i*10, 10,10))
                pygame.time.delay(500)
                pygame.display.flip()
                k+=1
            else:
                i+=1
                pygame.draw.rect(screen3, color[short], pygame.Rect(k*10,i*10, 10,10))
                pygame.time.delay(500)
                pygame.display.flip()
                k+=1

            # Update minimum 
            minm = rt[short] 
            if (minm == 0): 
                minm = 999999999

            # If a process gets completely executed 
            if (rt[short] == 0): 

                # Increment complete 
                complete += 1
                check = False

                # Find finish time of current process 
                fint = t + 1

                # Calculate waiting time 
                wt[short] = (fint - proc[short][1] -    
                                    proc[short][2])

                if (wt[short] < 0):
                    wt[short] = 0
            
            # Increment time 
            t += 1
        findTurnAroundTime(processes, n, wt, tat)
        string="Processes Burst time " + " Waiting time " + " Turn around time"
        text = font.render(string, True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (350 // 2, 350 // 2)
        screen3.blit(text, textRect)
        total_wt = 0
        total_tat = 0
        
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]

            # To print process id
            text = font.render(str(i+1), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (50, 175+((i+1)*15))
            screen3.blit(text, textRect)
            pygame.display.flip()

            #To print Burst time
            text = font.render(str(processes[i][1]), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (100, 175+((i+1)*15))
            screen3.blit(text, textRect)
            pygame.display.flip()

            #To print wait time
            text = font.render(str(wt[i]), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (185, 175+((i+1)*15))
            screen3.blit(text, textRect)
            pygame.display.flip()

            #To print turn around time
            text = font.render(str(tat[i]), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (280, 175+((i+1)*15))
            screen3.blit(text, textRect)
            pygame.display.flip()

        # To print the Average waiting time
        text = font.render("Average waiting time = "+str(total_wt / n), True, (0, 255, 255), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (175, 280)
        screen3.blit(text, textRect)
        pygame.display.flip()

        #To print average turn around time
        text = font.render("Average turn around time = "+str(total_tat / n), True, (0, 255, 255), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (175, 300)
        screen3.blit(text, textRect)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
  
# Function to calculate turn around time 
def findTurnAroundTime(processes, n, wt, tat): 
      
    # Calculating turnaround time 
    for i in range(n):
        tat[i] = processes[i][1] + wt[i] 
  
# Function to calculate average waiting and turn-around times. 
def findavgTime(processes, n): 
    wt = [0] * n
    tat = [0] * n 
  
    # Function to find waiting time of all processes 
    findWaitingTime(processes, n, wt) 
  
      
# Driver code 
if __name__ =="__main__":
      
    # Process id's 
    proc = [[1, 8, 0], [2, 4, 1], [3, 2, 2], [4, 1, 3]]
    n = 4
    findavgTime(proc, n)
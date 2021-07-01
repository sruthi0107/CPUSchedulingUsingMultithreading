import tkinter as tk
import numpy as np
import pygame
import time

def findWaitingTime_FCFS(processes, n, bt, wt):
    color=[(255,0,0),(25, 255, 228),(0,128,0),(0,0,128),(255,255,0)]
    pygame.init()
    screen1 = pygame.display.set_mode((350, 350))
    clock = pygame.time.Clock()
    screen1.fill((255, 255, 255))
    def drawGrid():
        blockSize = 10 #Set the size of the grid block
        for x in range(0, 350, 10):
            for y in range(0, 160, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen1, (0,0,0), rect, 1)
    font = pygame.font.Font('freesansbold.ttf', 13)
    
    grid=np.zeros((35,35))
    wt[0] = 0
    tat = [0] * n
    grid[0,wt[0]:bt[0]]=1
    done=False
    

    while not done:
        pygame.event.get()
        drawGrid()
        pygame.draw.rect(screen1, color[0], pygame.Rect(0, wt[0], (bt[0])*10,10))
        pygame.display.flip()
        for i in range(1, n ):
            wt[i] = bt[i - 1] + wt[i - 1] 
            pygame.time.delay(2000)
            pygame.draw.rect(screen1, color[i], pygame.Rect(wt[i]*10,i*10,  (bt[i])*10,10))
            #waiting time is used to span the distance from the y axis, burst time is used to draw the rectangle proportional to the burst time
            pygame.display.flip()
            clock.tick(60)

        findTurnAroundTime_FCFS(processes, n, bt, wt, tat)
        string="Processes Burst time " + " Waiting time " + " Turn around time"
        text = font.render(string, True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (350 // 2, 350 // 2)
        screen1.blit(text, textRect)
        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            # To print process id
            text = font.render(str(i+1), True, (0, 255, 0), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (50, 175+((i+1)*15))
            screen1.blit(text, textRect)

            #To print Burst time
            text = font.render(str(bt[i]), True, (0, 255, 0), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (100, 175+((i+1)*15))
            screen1.blit(text, textRect)

            #To print wait time
            text = font.render(str(wt[i]), True, (0, 255, 0), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (185, 175+((i+1)*15))
            screen1.blit(text, textRect)

            #To print turn around time
            text = font.render(str(tat[i]), True, (0, 255, 0), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (280, 175+((i+1)*15))
            screen1.blit(text, textRect)

        # To print the Average waiting time
        text = font.render("Average waiting time = "+str(total_wt / n), True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (175, 280)
        screen1.blit(text, textRect)

        #To print average turn around time
        text = font.render("Average turn around time = "+str(total_tat / n), True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (175, 300)
        screen1.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

def findTurnAroundTime_FCFS(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def fcfs( processes, n, bt):
    wt = [0] * n
    tat = [0] * n 

    findWaitingTime_FCFS(processes, n, bt, wt)
  
# Driver code
if __name__ =="__main__":
    processes = [ 1, 2, 3, 4]
    n = len(processes)
    burst_time = [3, 8, 4, 6]
    fcfs(processes, n, burst_time)
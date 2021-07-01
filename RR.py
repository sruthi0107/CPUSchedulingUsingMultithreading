import pygame

def rr(proc,time_quantum,n):
    color=[(255,0,0),(25, 255, 228),(0,128,0),(0,0,128),(255,255,0)]
    def drawGrid():
        blockSize = 10 #Set the size of the grid block
        for x in range(0, 350, 10):
            for y in range(0, 160, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (0,0,0), rect, 1)

    pygame.init()
    screen = pygame.display.set_mode((350, 350))
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 13)
    screen.fill((255, 255, 255))
    done=False

    #Initialising necessary data
    total_time= 0
    bt,wt,ct,tat,ready_queue=[0]*n,[0]*n,[0]*n,[0]*n,[0]
    for i in range(n):
        total_time+=proc[i][1]
    curr_time,flag=0,0
    prev_k,j,prev_proc=0,-1,-1

    #loop
    while not done:
        pygame.event.get()
        drawGrid()
        while curr_time!=total_time:
            initime=curr_time
            currpro=ready_queue.pop(0)
            if proc[currpro][2]>time_quantum:
                k=time_quantum
                curr_time+=time_quantum
                proc[currpro][2]-=time_quantum
            else:
                k=proc[currpro][2]
                curr_time+=proc[currpro][2]
                proc[currpro][2]=0
                ct[currpro]=curr_time
            if flag==0:
                for i in range(n):
                    if proc[i][0]>initime and proc[i][0]<=curr_time:
                        ready_queue.append(i)
                        if i==n-1: flag=1
            if proc[currpro][2]>0:
                ready_queue.append(currpro)
            
            if prev_proc!=currpro:
                j+=1
            pygame.draw.rect(screen, color[currpro], pygame.Rect(prev_k*10,j*10,k*10,10))
            pygame.time.delay(500)
            pygame.display.flip()
            prev_k+=k
            prev_proc=currpro

        #Printing the data
        string="Processes Burst time " + " Waiting time " + " Turn around time"
        text = font.render(string, True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (350 // 2, 350 // 2)
        screen.blit(text, textRect)

        total_tat,total_wt=0,0

        for i in range(n):
            tat[i]=ct[i]-proc[i][0]
            wt[i]=tat[i]-proc[i][1]

        for i in range(n):
            total_wt+=wt[i]
            total_tat+=tat[i]
            
            #To print process id
            text = font.render(str(i+1), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (50, 175+((i+1)*15))
            screen.blit(text, textRect)
            pygame.display.flip()

            #To print Burst time
            text = font.render(str(proc[i][1]), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (100, 175+((i+1)*15))
            screen.blit(text, textRect)
            pygame.display.flip()

            #To print waiting time
            text = font.render(str(wt[i]), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (185, 175+((i+1)*15))
            screen.blit(text, textRect)
            pygame.display.flip()

            #To print turnaround time
            text = font.render(str(tat[i]), True, (0, 255, 255), (0, 0, 128))
            textRect = text.get_rect()
            textRect.center = (280, 175+((i+1)*15))
            screen.blit(text, textRect)
            pygame.display.flip()

        # To print the Average waiting time
        text = font.render("Average waiting time = "+str(total_wt / n), True, (0, 255, 255), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (175, 280)
        screen.blit(text, textRect)
        pygame.display.flip()

        #To print average turn around time
        text = font.render("Average turn around time = "+str(total_tat / n), True, (0, 255, 255), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (175, 300)
        screen.blit(text, textRect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

#Driver code
if __name__ == '__main__':
    processes = [[0, 5, 5], [1, 4, 4], [2, 2, 2], [3, 1, 1]]
    time_quantum=2
    n=len(processes)
    rr(processes,time_quantum,n)
import pygame
from classes import Graph,Map,Button


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
SNOW = (255,250,250)
BLUE = (50,50,255)

#------CUSTOMIZING VARIABLES------
dimensions = (1000,1000)
start = (100,100)
goal = (510,510)
obsdim = 30
obsnum = 50
menusize = (100,1000)
starting_pos = (0,0)
carryOn = True
draw_line = False
draw_circle = False
draw_rectangle = False
play = False
d1 = False
d2  =False
d3 = False
lineobs = []
#----- INITIALIZING EVERYTHING------
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("RRT path planning")
map1 = pygame.display.set_mode((dimensions[0],dimensions[1]))
menuSurface = pygame.Surface(menusize)
map2 = Map(start, goal, obsdim, obsnum)
graph = Graph(start, goal, dimensions, obsdim, obsnum)
obs = graph.makeObs()
####------BUTTONS--------

resetButton = Button(10,10, 70, 45, 'Reset', RED)
playButton = Button(10, resetButton.y+10+resetButton.height, 70, 45, 'Play', GREEN)
lineButton = Button(10, playButton.y+100+playButton.height, 70, 45, 'Line', YELLOW)
circleButton = Button(10, lineButton.y+10+lineButton.height, 70, 45, 'Circle', YELLOW)
rectButton = Button(10, circleButton.y+10+circleButton.height, 80, 45, 'Rectangle', YELLOW)
startButton = Button(10, rectButton.y+100+rectButton.height, 70, 45, 'Start', BLUE)
goalButton = Button(10, startButton.y+10+startButton.height, 70, 45, 'Goal', BLUE)


def drawmenu():
    menuSurface.set_alpha(126)
    menuSurface.fill((0,0,0))
    map1.blit(menuSurface, (0, 0))
    playButton.draw(map1)
    lineButton.draw(map1)
    circleButton.draw(map1)
    resetButton.draw(map1)
    rectButton.draw(map1)
    startButton.draw(map1)
    goalButton.draw(map1)

#-------MAIN EVENT LOOP----------#
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                if resetButton.clicked(pos):
                    lineobs = []
                elif playButton.clicked(pos):
                    print(playButton.color)
                    if play:
                        playButton.color = GREEN
                        playButton.text = 'Play'
                    else:
                        playButton.color = YELLOW
                        playButton.text = 'Stop'
                    play = not play
                    draw_line = False
                    draw_circle = False
                    draw_rectangle = False                        
                
                elif lineButton.clicked(pos):
                    draw_line = True
                    draw_circle = False
                    draw_rectangle = False
                elif circleButton.clicked(pos):
                    draw_line = False
                    draw_circle = True
                    draw_rectangle = False
                elif rectButton.clicked(pos):
                    draw_line = False
                    draw_circle = False
                    draw_rectangle = True
                elif startButton.clicked(pos):
                    pass
                elif goalButton.clicked(pos):
                    pass
                elif not play:
                    if draw_line:
                        if d1:
                            
                            d1 = False
                            lineobs.append((starting_pos,pos))
                            
                        else:
                            d1 = True
                            starting_pos = pos
                            #pygame.draw.line(map1,BLACK , starting_pos, pygame.mouse.get_pos(), 1)
                        
                
                            
            elif event.button == 3:
                d1 = False
                d2 = False
                d3 = False                
        
    
    map1.fill((255,255,255))
    map2.drawObs(obs, map1)
    map2.drawMap(obs, map1)
    
    
    if d1 == True and draw_line:
        pygame.draw.line(map1,BLACK , starting_pos, pygame.mouse.get_pos(), 1)    
    for l in lineobs:
        pygame.draw.line(map1, BLACK, l[0], l[1],1)
    
    
    drawmenu()

    pygame.display.flip()
    clock.tick(60)  
    #pygame.display.update()
                 
   
    
#pygame.display.update()
#pygame.event.clear()
#pygame.event.wait(1000000000)

pygame.quit()

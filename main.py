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
GREY = (70,70,70)

#------CUSTOMIZING VARIABLES------
dimensions = (1000,1000)
start = (300,300)
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
circleobs = []
rectangleobs = []
start1 = False
goal1 = False
nodes = []
edges = []
#----- INITIALIZING EVERYTHING------
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("RRT path planning")
map1 = pygame.display.set_mode((dimensions[0],dimensions[1]))
menuSurface = pygame.Surface(menusize)
map2 = Map(start, goal, obsdim, obsnum)
graph = Graph(start, goal, dimensions, obsdim, lineobs,circleobs,rectangleobs)
#obs = graph.makeObs()
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
def drawgraph():
    pass
        
#-------MAIN EVENT LOOP----------#
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                if resetButton.clicked(pos):
                    graph.lineobs = []
                    graph.circleobs = []
                    graph.rectangleobs = []
                    start1 = False
                    goal1 = False
                    map2.start = (300,300)
                    map2.goal = (510,510)
                elif playButton.clicked(pos):
                    
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
                    start1 = False
                    goal1 = False
                elif lineButton.clicked(pos):
                    draw_line = True
                    draw_circle = False
                    draw_rectangle = False
                    start1 = False
                    goal1 = False

                elif circleButton.clicked(pos):
                    draw_line = False
                    draw_circle = True
                    draw_rectangle = False
                    start1 = False
                    goal1 = False

                elif rectButton.clicked(pos):
                    draw_line = False
                    draw_circle = False
                    draw_rectangle = True
                    start1 = False
                    goal1 = False

                elif startButton.clicked(pos):
                    start1 = True
                    play = False
                    draw_line = False
                    draw_circle = False
                    draw_rectangle = False                        
                    goal1 = False
                    
                elif goalButton.clicked(pos):
                    start1 = False
                    play = False
                    draw_line = False
                    draw_circle = False
                    draw_rectangle = False                        
                    goal1 = True

                elif not play:
                    if draw_line:
                        if d1:
                            
                            d1 = False
                            graph.lineobs.append((starting_pos,pos))
                            print(graph.number_of_obs())     
                        else:
                            d1 = True
                            starting_pos = pos
                            #pygame.draw.line(map1,BLACK , starting_pos, pygame.mouse.get_pos(), 1)
                        
                    if start1:
                        map2.start = pos
                        start1 = False
                    if goal1:
                        map2.goal = pos
                        goal1 = False
                    if draw_circle:
                        
                        graph.circleobs.append(pos)
                        draw_circle = False
                        
                    if draw_rectangle:
                        rect = pygame.Rect(pos,(30,30))
                        graph.rectangleobs.append(rect)                                       
                        draw_rectangle = False
            elif event.button == 3:
                d1 = False
                d2 = False
                d3 = False                
        
    
    #map2.drawObs(obs, map1)
    map1.fill((255,255,255))
    map2.drawMap(map1)
    
    
    if d1 == True and draw_line:
        pygame.draw.line(map1,GREY , starting_pos, pygame.mouse.get_pos(), 1)
    if draw_circle:
        pygame.draw.circle(map1, GREY, pygame.mouse.get_pos(), 10) 
    if draw_rectangle:
        rect = pygame.Rect(pygame.mouse.get_pos(), (30,30))
        pygame.draw.rect(map1,GREY,rect)
    for l in graph.lineobs:
        pygame.draw.line(map1, GREY, l[0], l[1],1)
    for c in graph.circleobs:
        pygame.draw.circle(map1, GREY, c, 10)
    for r in graph.rectangleobs:
        
        pygame.draw.rect(map1,GREY,r)
    
    drawmenu()
    if play:
        x,y = graph.sample_envir()
        n = graph.number_of_nodes()
        graph.add_node(n, x, y)
        x1,y1 = graph.x[n],graph.y[n]
        x2,y2 = graph.x[n-1],graph.y[n-1]
        if graph.isFree():
            nodes.append((graph.x[n],graph.y[n]))
            if not graph.crossObstacle(x1, y1, x2, y2):
                edges.append(((x1,y1),(x2,y2)))
    #pygame.draw.circle(map1, RED, pygame.mouse.get_pos(), 2)
    
    for n in nodes:
        pygame.draw.circle(map1, RED, n, map2.nodeRad,map2.nodeThickness)
    for e in edges:
        pygame.draw.line(map1, BLUE, e[0], e[1])
    clock.tick(60)  
    pygame.display.flip()
                
    pygame.display.update()
   
    
#pygame.display.update()
#pygame.event.clear()
#pygame.event.wait(1000000000)

pygame.quit()

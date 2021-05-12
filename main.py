import pygame
from classes import Graph,Map

def main():
    dimensions = (1000,1000)
    start = (50,50)
    goal = (510,510)
    obsdim = 30
    obsnum = 50
    menusize = (100,1000)

    pygame.init()
    clock = pygame.time.Clock()
    map1 = Map(start,goal,dimensions,obsdim,obsnum,menusize)
    graph = Graph(start,goal,dimensions,obsdim,obsnum)

    obstacles = graph.makeObs()

    map1.drawMap(obstacles)

    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(1000000000)

    
    
    clock.tick(60)

if __name__ == '__main__':


    
    main()
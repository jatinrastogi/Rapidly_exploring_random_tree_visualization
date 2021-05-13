import pygame
import random
import math

class Map:
    def __init__(self,start,goal,Map,obsdim,obsnum):
        self.start = start
        self.goal = goal
        
        self.map = Map
       
       
        self.nodeRad = 0
        self.nodeThickness = 0
        self.edgeThickness = 1
        
        self.obstacles = []
        self.obsdim = obsdim
        self.obsNumber = obsnum

        self.grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.White = (255,255,255)

    def drawMap(self,obstacles):
        pygame.draw.circle(self.map,self.Green,self.start,self.nodeRad+5,0)
        pygame.draw.circle(self.map,self.Green,self.goal,self.nodeRad+20,1)
        self.drawObs(obstacles)
    def drawPath(self):
        pass
    def drawObs(self,obstacles):
        obstaclesList = obstacles.copy()
        while(len(obstaclesList)>0):
            obstacle = obstaclesList.pop(0)
            pygame.draw.rect(self.map,self.grey,obstacle)


class Graph:
    def __init__(self,start,goal,MapDimensions,obsdim,obsnum):
        (x,y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False
        self.maph,self.mapw = MapDimensions
        self.x = []
        self.y = []
        self.parent = []
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)

        self.obstacles = []
        self.obsDim = obsdim
        self.obsNum = obsnum

        self.goalstate = None
        self.path = []

    def makeRandomRect(self):
        uppercornerx = int(random.uniform(0,self.mapw-self.obsDim))
        uppercornery = int(random.uniform(0,self.maph-self.obsDim))
        return (uppercornerx,uppercornery)

    def makeObs(self):
        obs = []

        for _ in range(self.obsNum):
            rectang = None
            startgoalcol = True
            while startgoalcol:
                upper = self.makeRandomRect()
                rectang = pygame.Rect(upper,(self.obsDim,self.obsDim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startgoalcol = True
                else:
                    startgoalcol = False

            obs.append(rectang)

        self.obstacles = obs.copy()
        return obs


    def add_node(self):
        pass
    def remove_node(self):
        pass
    def add_edge(self):
        pass
    def remove_edge(self):
        pass
    
    def number_of_nodes(self):
        pass

    def distance(self):
        pass
    def nearest(self):
        pass
    def isFree(self):
        pass
    def crossObstacle(self):
        pass
    def connect(self):
        pass
    def step(self):
        pass
    def path_to_goal(self):
        pass
    def getPathCoords(self):
        pass
    def bias(self):
        pass
    def expand(self):
        pass
    def cost(self):
        pass

class Button():
    def __init__(self, x, y, width, height, text, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, t):
        # Render new label
        self._text = t
        self.label = pygame.font.SysFont("monospace", 15).render(t, 1, (0, 0, 0))

    def values(self):
        return (self.x, self.y, self.width, self.height)

    def draw(self, surface):
        # Draw button
        pygame.draw.rect(surface, self.color, self.values())
        # Draw label
        surface.blit(self.label, (self.x + (self.width/2 - self.label.get_width()/2), self.y+(self.height/2 - self.label.get_height()/2)))
    
    def clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
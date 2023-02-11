import pygame
import sys
import numpy as np

pygame.init()

screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Crusor drawing persistence diagram")

run = True
clicked = False
drawing_coordinates = []  # storing (x,y) coordinates of where the user is drawing using cursor

while run:
    screen.fill( (255,255,255))
    # make drawing wherever the cursosr clicked
    for (x,y) in drawing_coordinates :
        pygame.draw.circle(screen, center=[x,y], color=(255,0,0), radius=2)
    
    # closing the screen when button "x" is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN :     # when button mouse is pressed down once
            clicked = True
            x, y = pygame.mouse.get_pos()
            drawing_coordinates.append( (x,y) )
        if event.type == pygame.MOUSEMOTION :         # when cursor is moved with mouse button is pressed down cointinuously
            if clicked : 
                x, y = pygame.mouse.get_pos()
                drawing_coordinates.append( (x,y) )
        if event.type == pygame.MOUSEBUTTONUP :       # when mouse button is released, stop making drawing
            clicked = False

    pygame.display.update()

pygame.quit()

# Now the drawing is done, Let us move on to Topologival data analysis
# We are plotting the persistence diagram of the drawing made with cursor

# Basic imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import networkx as nx
from IPython.display import Video

# scikit-tda imports that perform the core of the computation
import sktda
import ripser 
import persim

drawing_data = np.array(drawing_coordinates)
diagrams = ripser.ripser(drawing_data)['dgms']
persim.plot_diagrams(diagrams, show=True)

import pygame
import random

class Spike():
    """Spawns from the sides of the arena horizontally, stays for a few seconds, and leaves. Before it comes onto screen,
    a red flashing particle appears where it spawns. More spawn at a time the higher the difficulty number."""
    def __init__(self):
        # Defines position, color, and speed
        self.pos
        self.color
        self.speed

class Fireball():
    """Spawns from anywhere and moves in a straight line. Speeds up the higher the difficulty number."""
    def __init__(self):
        # Defines position, size of the fireballs, color, shape, and speed
        self.pos
        self.size
        self.color
        self.shape
        self.speed

class Crusher():
    """Spawns in a random area, killing the player if landed above them. The area flashes red before coming down, and cannot
    be passed when down. Dissappears after some time, allowing the player to move into that area. Spawns more the higher the
    difficulty number"""
    def __init__(self):
        # Defines position, size, color, and speed
        self.pos
        self.size
        self.color
        self.speed

class LavaPit():
    """Spawns after a certain time around the arena, making it smaller. Only a certain amount of area is effected by the lava,
    so the player can actually play. If the players goes over it, they fall and die."""
    def __init__(self):
        # Defines size and color
        self.size
        self.color

class PlayerHitbox():
    """This is the player's hitbox, it is invisible to the player. It checks if it hits a obstacle, and once it does, the player 
    game overs."""
    def __init__(self):
        # define position, size, alpha, and shape
        self.pos
        self.size
        self.alpha
        self.shape

class Arena():
    """The arena is the background of the game and where the player spawns. They start in the middle, over a lava pit. The edges of the arena turn 
    into lava pits, making the area smaller."""
    def __init__(self):
        # define size, screen, and color 
        self.size
        self.screen
        self.color

def main():
    pygame.init()
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Pit of Trials Game")
    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
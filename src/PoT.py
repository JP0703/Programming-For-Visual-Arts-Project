import pygame
import random

class Spike():
    """Spawns from the sides of the arena horizontally, stays for a few seconds, and leaves. Before it comes onto screen,
    a red flashing particle appears where it spawns. More spawn at a time the higher the difficulty number."""
    def __init__(self):
        pass

class Fireball():
    """Spawns from anywhere and moves in a straight line. Speeds up the higher the difficulty number."""
    def __init__(self):
        pass

class Crusher():
    """Spawns in a random area, killing the player if landed above them. The area flashes red before coming down, and cannot
    be passed when down. Dissappears after some time, allowing the player to move into that area. Spawns more the higher the
    difficulty number"""
    def __init__(self):
        pass

class LavaPit():
    """Spawns after a certain time around the arena, making it smaller. Only a certain amount of area is effected by the lava,
    so the player can actually play. If the players goes over it, they fall and die."""
    def __init__(self):
        pass
    
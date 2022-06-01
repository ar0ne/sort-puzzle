"""Sort puzzle game"""
import pygame
from pyghelpers import pyghelpers
from scenes.play import PlayScene
from scenes.result import ResultScene
from scenes.splash import SpashScene

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
scenes = [SpashScene(window), PlayScene(window), ResultScene(window)]
scene_manager = pyghelpers.SceneMgr(scenes, FRAMES_PER_SECOND)
scene_manager.run()
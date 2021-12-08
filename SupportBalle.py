
import random

import pygame
from pygame.math import Vector2

import core


class Balle:
    def __init__(self, largeur=400, hauteur=400, vector2):
        self.position = Vector2(400,200)
        self.couleur = (255,0,0)
        self.vitesse = vector2
        self.acceleration = vector2
        self.vitesse max(20)
        self.vitesse min (10)


    def show(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.taille)


    def deplacement(self,target):

        if core.getKeyPressList(276):
            if core.memory("supportBalle").core.memory("positionGauche")
        elif core.getKeyPressList(275):
            if core.memory("SupportBalle").core.memory("positionDroite")


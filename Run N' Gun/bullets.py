from tkinter import *
from winsound import *
import random
import time
import math

class Bullets():
    
    def __init__(self, x, y, direction, canvas, weapon, who):
        self.canvas = canvas
        self.direction = direction
        self.w = weapon
        self.br = PhotoImage(file = "Other\\rB.gif")
        self.bl = PhotoImage(file = "Other\\lB.gif")
        self.speed = 0
        self.damage = 0
        self.removed = False
        self.targetHit = False
        self.obstacleHit = False
        if weapon == "Pistol":
            self.spread = 10
            self.damage = .7
            x += + 26
            lx = x - 26
            y -= 8
            PlaySound("SFX\Pistol.wav", SND_FILENAME and SND_ASYNC)
        if weapon == "Uzi":
            self.damage = .5
            self.spread = 50
            x += 26
            lx = x - 26
            y -= 8
            PlaySound("SFX\\Uzi.wav", SND_FILENAME and SND_ASYNC)
        if weapon == "Shotgun":
            self.damage = .6
            self.spread = 100
            x += 25
            lx = x - 25
            y -= 4
            PlaySound("SFX\Shotgun.wav", SND_FILENAME and SND_ASYNC)
        if weapon == "AR":
            self.damage = 1.1
            self.spread = 20
            x += 25
            lx = x - 25
            y -= 5
            PlaySound("SFX\AR.wav", SND_FILENAME and SND_ASYNC)
        if weapon == "Sniper":
            self.damage = 5
            self.spread = 0
            x += 26
            lx = x - 26
            y -= 7
            PlaySound("SFX\Sniper.wav", SND_FILENAME and SND_ASYNC)
        if who == "p":
            self.ys = random.randint(-self.spread, self.spread)
            self.ys = self.ys/10
            if direction == "r":
                self.speed = 20
                self.bullet = self.canvas.create_image(x, y, image = self.br)
            if direction == "l":
                self.speed = -20
                self.bullet = self.canvas.create_image(lx, y, image = self.bl)

        if who == "e":
            self.ys = random.randint(-self.spread, self.spread)
            self.ys = self.ys/10
            self.speed = -20
            self.bullet = self.canvas.create_image(lx, y, image = self.bl)

    def getDamage(self):
        self.targetHit = True
        return self.damage

    def hitFloors(self):
        self.obstacleHit = True
        
    def removeB(self):
        remove = False
        xy = self.canvas.coords(self.bullet)
        if self.obstacleHit:
            remove = True
        if self.targetHit:
            remove = True
        if xy[1] > 750 or xy[1] < 0:
            remove = True
        if remove:
            self.removed = True
            self.canvas.delete(self.bullet)
            return True
        return False
        
    def bLoc(self):
        xy = self.canvas.coords(self.bullet)
        return xy

    def move(self):
        if self.removed:
            return
        self.canvas.move(self.bullet, self.speed, self.ys)

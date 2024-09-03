from tkinter import *
import random
import time
import math
import bullets

class Enemies():

    def __init__(self, x, y, canvas, weapon):
        self.eD = PhotoImage(file = "Enemies\dEnemy.gif")
        self.eP = PhotoImage(file = "Enemies\pEnemyL.gif")
        self.eU = PhotoImage(file = "Enemies\\uEnemyL.gif")
        self.eSH = PhotoImage(file = "Enemies\shEnemyL.gif")
        self.weapon = weapon
        self.canvas = canvas
        self.deadTimer = 50
        self.health = 5
        self.mGain = 10
        self.bulletL = []
        self.bDelay = 0
        self.removed = False
        self.stopShoot = False
        if self.weapon == "Pistol":
            self.health = 2.5
            self.mGain = 15
            self.enemy = self.canvas.create_image(x, y, image = self.eP)
        if self.weapon == "Uzi":
            self.health = 2.5
            self.mGain = 30
            self.enemy = self.canvas.create_image(x, y, image = self.eU)
        if self.weapon == "Shotgun":
            self.health = 10
            self.mGain = 50
            self.enemy = self.canvas.create_image(x, y, image = self.eSH)

    def eLoc(self):
        xy = self.canvas.coords(self.enemy)
        return xy
    
    def shoot(self):
        xy = self.eLoc()
        x = xy[0]
        y = xy[1]
        if self.bDelay == 0:
            if self.weapon == "Pistol":
                self.bullet = bullets.Bullets(x, y, "", self.canvas, self.weapon, "e")
                self.bulletL.append(self.bullet)
                self.bDelay += 50
            if self.weapon == "Uzi":
                self.bullet = bullets.Bullets(x, y, "", self.canvas, self.weapon, "e")
                self.bulletL.append(self.bullet)
                self.bDelay += 20
            if self.weapon == "Shotgun":
                for i in range(4):
                    self.bullet = bullets.Bullets(x, y, "", self.canvas, self.weapon, "e")
                    self.bulletL.append(self.bullet)
                self.bDelay += 60
        self.bDelay -= 1
        
    def shot(self, damage):
        self.health -= damage

    def ShootOrNah(self):
        return self.stopShoot

    def dead(self):
        if self.health > 0:
            return False
        self.stopShoot = True
        self.canvas.itemconfig(self.enemy, image = self.eD)
        self.deadTimer -= 1
        if self.deadTimer == 0:
            return True

    def gMoney(self):
        return self.mGain

    def enemyB(self):
        return self.bulletL

    def removeE(self):
        remove = False
        if self.dead():
            remove = True
        if remove:
            self.canvas.delete(self.enemy)
            self.removed = True
            return True
        return False

    def move(self, x):
        if self.removed:
            return
        self.canvas.move(self.enemy, -x, 0)

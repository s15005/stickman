__author__ = 's15005masahuk'

from tkinter import  *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. stick Man Races for the Exit")
        self.tk.resizable(0, 0)
        self.tk.wm.attributes("-topmost, 1")
        self.canvas = Canvas(self. tk, within=500, height=500,\
                             highlightthickness=0)
        self.canvas_pack()
        self.tk.update()
        self.canvas_hedth_ = 500
        self. canvas_width_ = 500
        self.bg = PhotoImage(filter="background.gif")
        w = self.bg.width()
        h = self.bg.hedth()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, \
                                         image=self.bg, anchor='nw')
                self.sprites = []
                self.runing = True
    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

class Coorrds:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def within_x(co1, co2):
    return (co2.x1 > co1.x1 <co2.x2
            or  co2.x1 < co1.x2 < co2.x2
            or  co1.x1 < co2.x1 < co1.x2
            or  co1.x1 < co2.x2 < co1.x2)

def within_y(co1, co2):
    return (co2.y1 < co1.y1 < co2.y2
            or  co2.y1 < co1.y2 < co2.y2
            or  co1.y1 < co2.y1 < co2.y2
            or  co1.y1 < co2.y2 < co1.y2)

def collided_left(co1, co2):
    return (within_y(co1, co2) and
               co2.x2 >= co1.x1 >=co2.x1)

def collided_righgt(co1, co2):
    return (within_y(co1,co2) and
             co2.x2 <= co1.x2 <= co2.x2)

def collided_bottom(y, co1, co2):
    return (within_x(co1, co2) and
             co2.y1 <= co1.y1 <= co2.y2)

class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None
        def move(self):
            pass
        def coorda(self):
            return self.coordinates

class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, widht, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.imsge = game.canvas.create_imasge(x, y, \
                                               image=self.photo_image, anchor='nw')
        self.coordinates = Coorrds(x, y, x + widht, y + height)

    class StickFigure(Sprite):
        def __init__(self, game):
            Sprite.__init__(self, game)
            self.images_left = [
                 PhotoImage(file="figure-L1.gif"),
                 PhotoImage(file="figure-L2.gif"),
                 PhotoImage(file="figure-L3.gif")
                ]
            self.images_left = [
                PhotoImage(file="fogure-R1.gif"),
                PhotoImage(file="fogure-R2.gif"),
                PhotoImage(file="figure-R3.gif")
                ]
            self.images = game.canvas.create_imasge(200, 470, \
                                                    image=self.image_left[0], anchor='nw')
            self.x = -2
            self.y = 0
            self.current_image = 0
            self.current_image_add = 1
            self.jump_count = 0
            self.Iast_time = time.time()
            self.coordinates = Coorrds()
            self.canvas.bind_all('<keyPress-Left>', self.turn_left)
            self.canvas.bind_all('<keyPress-Right>', self.turn_right)
            self.canvas.bind_all('<space>', self.jump)

            def turn_left(self, evt):
                if self.y == 0:
                    self.x = -2

            def turn_right(self, evt):
                if self.y == 0:
                    self.x = 2

            def jump(self, evt):
                if self.y == 0:
                     self.y = -4
                     self.jump_count = 0

            def animate(self):
                if self.x != 0 and self.y == 0:
                    if time.time() - self. last_time > 0.1:
                        self.last_time= time.time()
                        self.current_imge += self.current_image_add
                        if self.current_image >= 2:
                            self.current_image_add = -1
                        if self.current_image <= 0:
                            self.current_image_add = 1
                if self.x < 0:
                    if self.y != 0:
                        self.game.canvas.itemconfig(self.image, \
                                                    image=self.images_left[2])
                    else:
                        self.game.canvas.itemconfig(self.image, \
                                                    image=self.imagees_left[self.current_image])
                elif self.x > 0:
                    if self.y !=0:
                        self.game.canvas.itemconfig(self.image,\
                                                    image=self.images_right[2])
                    else:
                        self.game.canvas.itemconfig(self.image,\
                                                    image=self.image_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return  self.coordinates

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
             self.jump_count -= 1
        co = self.coordinates()
        left = True
        right = True
        top = True
        bottom = True
        falling = True
        if self.y > 0 and co. y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
            


        self.sprites = []
        self.running = True
        self.tk.afer(10, self.mainloop):

     def mainloo(self):
         if self.running:
             for sprite in self.sprites:
                 sprite.move()
         self.tk.update_idletasks()
         self.tk.update()
         self.tk.after(10, self.mainloop)

if _name_ == '_main_':
     g = Game()
     platform1 = PlatformSprite(g, PhotoImage(file='platform1.gif'),
                                0, 480, 100, 10)
     g.sprites.append(platform1)
     g.tk.mainloop()

from TkinterMain import *
from tkinter import Canvas, messagebox
import time
import _thread
import random
import socket

root = Tk()

root.title('MyGame')
root.resizable(0,0)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

class User:

    tx, ty = (0, 0) # generate random x, y for food
    flag = True
    
    def __init__(self,name, x, y):
        self.name = name
        self.way = 2
        #self.canvas = canvas
        self.x1 = x
        self.y1 = y
        self.x2 = x+10
        self.y2 = y+10
        self.score = 0

    def generateFood(arr):
        global root
        start = time.time()
        i = 0
        User.tx = random.randrange(10,488, 2)
        User.ty = random.randrange(10,488, 2)
        food = canvas.create_rectangle(User.tx,User.ty,User.tx+4,User.ty+4, fill='red', tag='food')
        while True:
            if( int((time.time() - start)) == 120 ):
                break
            time.sleep(0.01)
            if i == 500:
                canvas.delete(food)
                User.tx = random.randrange(10,488, 2)
                User.ty = random.randrange(10,488, 2)
                food = canvas.create_rectangle(User.tx,User.ty,User.tx+4,User.ty+4, fill='red', tag='food')
                User.flag = True
                i = 0
            i+=1
        root.destroy()
        root = Tk()
        root.geometry("100x100")
        str_ = ""
        for obj, _ in arr:
            str_ += obj.showScore() + "\n"
        messagebox.showinfo("Score",str_)  
            

    def showScore(self):
        return "{} : {}".format(self.name, self.score)
    
    def changeWay(self, way):
        if way == "left":
            self.way = 1
        elif way == "right":
            self.way = 2
        elif way == "up":
            self.way = 3
        elif way == "down":
            self.way = 4

    def listentClientKey(self, socket):
        while True:
            key = socket.recv(1024).decode("utf-8")
            self.changeWay(key)

    def showPosition(self):
        print("{} : ({} {} {} {})".format(self.name,self.x1, self.y1, self.x2, self.y2))


    def play(self, socket):
        
        _thread.start_new_thread(self.listentClientKey, (socket, ))
            
        while True:
            obj = canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill='black')
            time.sleep(0.01)

            if self.way == 1: # left
                if self.x1 >= 2 and self.x2 >= 10:
                    self.x1 -= 1
                    self.x2 -= 1
            elif self.way == 2: # right
                if self.x1 <= 490 and self.x2 <= 498:
                    self.x1 += 1
                    self.x2 += 1
            elif self.way == 3: # up
                if self.y1 >= 2 and self.y2 >= 10:
                    self.y1 -= 1
                    self.y2 -= 1
            elif self.way == 4: # down
                if self.y1 <= 490 and self.y2 <= 498:
                    self.y1 += 1
                    self.y2 += 1

            if User.flag == True:
                if self.x1 < self.tx and self.y1 < self.ty and self.tx+4 < self.x2 and self.ty+4 < self.y2:
                    print('{} eat'.format(self.name))
                    User.flag = False
                    canvas.delete('food')
                    self.score += 1
                    
            canvas.delete(obj)
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if DEBUG:
    print("Socket successfully created")
  
port = 3696

s.bind(('', port))         
if DEBUG:
    print("socket binded to %s" %(port)) 

s.listen(5)     
if DEBUG:
    print("socket is listening")   

plist = []
join = 0

while join < players:
    c, addr = s.accept()
    if DEBUG:
        print("{} {} connected".format(c, addr))
    name = input("Enter Player {} name : ".format(join+1))
    x = random.randrange(10, 480, 2)
    y = random.randrange(10, 480, 2)
    plist.append( [User(name, x, y), c])
    join += 1

for obj, socket in plist:
    _thread.start_new_thread(obj.play, (socket, ))

_thread.start_new_thread(User.generateFood, (plist,))
root.mainloop()

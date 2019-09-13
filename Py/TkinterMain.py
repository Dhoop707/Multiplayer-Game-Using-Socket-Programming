from tkinter import Tk, Frame, Button, Label, BOTTOM, TOP

root = Tk()
DEBUG = 1

players = 0

def startGame(noOfPlayer):
    if DEBUG:
        print("No of players : ", noOfPlayer)
    global root, players
    players = noOfPlayer
    root.destroy()


f1 = Frame(root)
f1.pack()

f2 = Frame(root, width=70, height = 100)
f2.pack(side=BOTTOM)

lab1 = Label(f1, text="Select number of players")
lab1.config(font=("Arial", 15))
lab1.pack()

bt1 = Button(f2,width = 10, text = 'Two', command=lambda:startGame(2))
bt2 = Button(f2,width = 10, text = 'Three', command=lambda:startGame(3))
bt3 = Button(f2,width = 10, text = 'Four', command=lambda:startGame(4))

bt1.config(font=("Arial", 10))
bt2.config(font=("Arial", 10))
bt3.config(font=("Arial", 10))

bt1.pack(side=TOP)
bt2.pack(side=TOP)
bt3.pack(side=TOP)


root.mainloop()
    

import socket                
import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
  
port = 3696                
  
s.connect(('127.0.0.1', port)) 

def on_press_reaction(event):
    if event.name == 'up':
        s.send(bytes("up", "utf-8"))
        print("up")
    elif event.name == "down":
        s.send(bytes("down", "utf-8"))
        print("down")
    elif event.name == "left":
        s.send(bytes("left", "utf-8"))
        print("left")
    elif event.name == "right":
        s.send(bytes("right", "utf-8"))
        print("right")
    else:
        pass
        
keyboard.on_press(on_press_reaction)

while True:
    pass

s.close() 

import tkinter as tk
import time

class car:
    x = 0
    y = 0
    size = 1
    bodyColor = "Black"
    width = 100
    height = 50
    wheelWidth = 10
    wheelHeight = 10
    id1 = 0
    id2 = 0
    id3 = 0
    id4 = 0

    def set(self, x, y, size, bodyColor):
        self.x = x
        self.y = y
        self.size = size
        self.bodyColor = bodyColor
        self.width *= self.size
        self.height *= self.size
        self.wheelWidth *= self.size
        self.wheelHeight *= self.size

    def draw(self):
        self.id1 = canvas.create_rectangle(self.x+self.width*(1/4), self.y, self.x+self.width*(3/4), self.y+self.height/2, fill = self.bodyColor)
        self.id2 = canvas.create_rectangle(self.x, self.y+self.height/2, self.x+self.width, self.y+self.height, fill = self.bodyColor)
        self.id3 = canvas.create_oval(self.x+self.width*(1/4), self.y+self.height,self.x+self.width*(1/4)+self.wheelWidth, self.y+self.height+self.wheelHeight, fill="Black")
        self.id4 = canvas.create_oval(self.x+self.width*(3/4)-self.wheelWidth, self.y+self.height,self.x+self.width*(3/4), self.y+self.height+self.wheelHeight, fill="Black")

    def delete(self):
        canvas.delete(self.id1)
        canvas.delete(self.id2)
        canvas.delete(self.id3)
        canvas.delete(self.id4)

    def move_to_right(self):
        self.delete()
        self.set(self.x + 100, self.y, self.size, self.bodyColor)
        self.draw()

    def move_to_left(self):
        self.delete()
        self.set(self.x - 100, self.y, self.size, self.bodyColor)
        self.draw()


root = tk.Tk()
root.geometry("1000x500")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

car = car()
car.set(10, 50, 1, "blue")
car.draw()

direction = "r"
while(True):
    if(car.x + car.width > 1000):
        direction = "l"
    elif(car.x < 0):
        direction = "r"   
    if(direction == "r"):
        car.move_to_right()
    elif(direction == "l"):
        car.move_to_left()
    time.sleep(0.1)
    root.update()
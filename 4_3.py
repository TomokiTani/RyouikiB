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
    direction = "r"

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
        self.set(self.x + 10, self.y, self.size, self.bodyColor)
        self.draw()

    def move_to_left(self):
        self.delete()
        self.set(self.x - 10, self.y, self.size, self.bodyColor)
        self.draw()

class cannonball:
    x = 0
    y = 0
    width = 10
    height = 10
    id = 0

    def set(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.id = canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill="Black")

    def delete(self):
        canvas.delete(self.id)

    def move(self):
        self.delete()
        self.set(self.x, self.y - self.height)
        self.draw()

root = tk.Tk()
root.geometry("1000x500")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

cannonballs = []
car = car()
car.set(10, 50, 1, "blue")
car.draw()

#大砲
canvas.create_rectangle(480, 460, 520, 480, fill="Green")
canvas.create_rectangle(460, 480, 540, 500, fill="Green")

def key_handler(e):
    y = 450
    cannonballs.append(cannonball())
    cannonballs[len(cannonballs)-1].set(500, y)
    cannonballs[len(cannonballs)-1].draw()

def is_canonnball_hit_car(cannonball):
    if((car.x <= cannonball.x + cannonball.width and car.x + car.width >= cannonball.x) and (car.y <= cannonball.y + cannonball.height and car.y + car.height + car.wheelHeight >= cannonball.y)):
        return True
    return False


def cannonballs_handler():
    delete_indexs = []      
    for i in range(len(cannonballs)):
        if(cannonballs[i].y <= 0):
            delete_indexs.append(i)        
            continue
        cannonballs[i].move()
    for i in range(len(delete_indexs)):
        cannonballs[delete_indexs[i] - i].delete()
        cannonballs.pop(delete_indexs[i] - i)
    canvas.after(100, cannonballs_handler)

def car_handler(): 
    for i in range(len(cannonballs)):
        if(is_canonnball_hit_car(cannonballs[i])):
            car.delete()
            car.set(10, 50, 1, "blue")
            car.draw()
            cannonballs[i].delete()
            cannonballs.pop(i)
            break
    if(car.x + car.width > 1000):
        car.direction = "l"
    elif(car.x < 0):
        car.direction = "r"   
    if(car.direction == "r"):
        car.move_to_right()
    elif(car.direction == "l"):
        car.move_to_left()
    canvas.after(100, car_handler)


root.bind("<KeyPress>", key_handler)

car_handler()
cannonballs_handler()

root.mainloop()
import tkinter as tk
import time

class cannonball:
    x = 0
    y = 0
    width = 100
    height = 50
    id = 0

    def set(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.id = canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="Black")

    def delete(self):
        canvas.delete(self.id)

    def move(self):
        self.delete()
        self.set(self.x, self.y - 10)
        self.draw()

root = tk.Tk()
root.geometry("1000x500")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

cannonballs = []

#大砲
canvas.create_rectangle(480, 460, 520, 480, fill="Green")
canvas.create_rectangle(460, 480, 540, 500, fill="Green")

def key_handler(e):
    y = 400
    start = len(cannonballs)
    for i in range(start, start + 5):
        cannonballs.append(cannonball())
        cannonballs[i].set(500, y)
        cannonballs[i].draw()
        y += 15


def cannonballs_handler():      
    for i in range(len(cannonballs)):
        if(cannonballs[i].y <= 0):
            cannonballs[i].delete()
            continue
        cannonballs[i].move()
        #root.update()
    canvas.after(100, cannonballs_handler)

root.bind("<KeyPress>", key_handler)

cannonballs_handler()

root.mainloop()
    
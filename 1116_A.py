import tkinter as tk

class car:
    x = 0
    y = 0
    size = 1
    bodyColor = "Black"
    width = 100
    height = 50
    wheelWidth = 10
    wheelHeight = 10

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
        canvas.create_rectangle(self.x+self.width*(1/4), self.y, self.x+self.width*(3/4), self.y+self.height/2, fill = self.bodyColor)
        canvas.create_rectangle(self.x, self.y+self.height/2, self.x+self.width, self.y+self.height, fill = self.bodyColor)
        canvas.create_oval(self.x+self.width*(1/4), self.y+self.height,self.x+self.width*(1/4)+self.wheelWidth, self.y+self.height+self.wheelHeight, fill="Black")
        canvas.create_oval(self.x+self.width*(3/4)-self.wheelWidth, self.y+self.height,self.x+self.width*(3/4), self.y+self.height+self.wheelHeight, fill="Black")

root = tk.Tk()
root.geometry("1000x500")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

car = car()
car.set(20, 20, 1, "red")
car.draw()
car.set(200, 200, 2, "blue")
car.draw()

root.mainloop()



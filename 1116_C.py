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

def changeColor(color):
    if color == "red":
        return "blue"
    return "red"

root = tk.Tk()
root.geometry("1000x500")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

cars = []
color = "blue"
carId = 0
for i in range(10, 10+30*10, 30):
    color = changeColor(color)
    for j in range(10, 10+50*10, 50):
        cars.append(car())
        cars[carId].set(j, i, 0.2, color)
        cars[carId].draw()
        color = changeColor(color)
        carId += 1

#×ボタンクリックで、プログラムを終了させる
#これ以降に、コンソール入力の無限ループがあるので
root.protocol("WM_DELETE_WINDOW", exit)

#コンソール入力
while(True):
    id = input("id = ")
    try:
        if(id == "quit"):
            exit()
        elif(int(id) < 0 or int(id) >99):
            print('error')
            exit()
        cars[int(id)].delete()
    except:
        print('error')
        exit()

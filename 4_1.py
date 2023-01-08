import tkinter as tk
import time

root = tk.Tk()
root.geometry("1000x500")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

#大砲
canvas.create_rectangle(480, 460, 520, 480, fill="Green")
canvas.create_rectangle(460, 480, 540, 500, fill="Green")

while(True):
    y = 0
    cannonball = canvas.create_oval(500, 450, 510, 460, fill="Black")
    while(canvas.bbox(cannonball)[1] > 0):
        canvas.delete(cannonball)
        cannonball = canvas.create_oval(500, 450 - y, 510, 460 - y, fill="Black")
        y += 10
        root.update()
        time.sleep(0.1)
    canvas.delete(cannonball)
    time.sleep(0.1)
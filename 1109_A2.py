import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_rectangle(30, 20, 80, 30, fill="Black")
#canvas.create_rectangle(30, 20, 80, 30, fill="Black")


root.mainloop()
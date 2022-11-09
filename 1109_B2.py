import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_rectangle(30, 20, 80, 30, fill="Black")
canvas.create_rectangle(20, 30, 90, 50, fill="Black")
canvas.create_oval(30, 50, 40, 60, fill="Black")
canvas.create_oval(70, 50, 80, 60, fill="Black")
canvas.create_text(50, 80, text="Tani Tomoki", fill="Black")

root.mainloop()
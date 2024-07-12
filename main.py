import tkinter as tk
import time



class TrafficLight:
    def __init__(self, root):
        self.root = root

        self.canvas = tk.Canvas(root, width=200, height=500)
        self.canvas.pack()

        self.red_light = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.yellow_light = self.canvas.create_oval(50, 200, 150, 300, fill="gray")
        self.green_light = self.canvas.create_oval(50, 350, 150, 450, fill="gray")

        self.current_color = None
        self.change_light()

    def change_light(self):
        if self.current_color == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.current_color = "yellow"
            self.root.after(2000, self.change_light)
        elif self.current_color == "yellow":
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.current_color = "green"
            self.root.after(2000, self.change_light)
        elif self.current_color == "green":
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="green")
            self.current_color = "red"
            self.root.after(2000, self.change_light)
        else:
            self.canvas.itemconfig(self.red_light, fill="red")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.current_color = "yellow"
            self.root.after(2000, self.change_light)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x600")
    root.title("Swetafor system")
    traffic_light = TrafficLight(root)
    root.mainloop()

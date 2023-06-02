import sys
import tkinter as tk

sys.path.insert(1, '../search visualizer')
from constants import *

# This is just a test file I used to experiment with tkinter.after()

class App:
    def __init__(self, parent):
        self.root = parent
        self.frames = []
        self.draw_btn()
        self.draw_frames()

    def draw_frames(self):
        for i in range(50):
            self.frames.append(tk.Frame(
                master=self.root,
                relief=tk.RIDGE,
                borderwidth=1,
                bg=GRID_COLOR,
                width=20,
                height=10
                ))
            self.frames[i].pack()

    def draw_btn(self):
        self.count = 0
        def color():
            if self.count >= len(self.frames):
                return
            f = self.frames[self.count]
            self.count += 1
            f['bg'] = "red"
            f.after(50, color)

        btn = tk.Button(master=self.root, text="press me", command=color)
        btn.pack()


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
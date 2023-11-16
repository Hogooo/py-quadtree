from __future__ import annotations
from tkinter import *


class QuadTree:
    node_posx1 = [0, 1, 0, 1]
    node_posy1 = [0, 0, 1, 1]
    node_posx2 = [1, 2, 1, 2]
    node_posy2 = [1, 1, 2, 2]

    def __init__(self,
                 hg: int | QuadTree,
                 hd: int | QuadTree,
                 bg: int | QuadTree,
                 bd: int | QuadTree):
        self.HEIGHT = self.WIDTH = 256
        self.tk_window = None
        self.node_list = [hg, hd, bg, bd]
        self.depth = 0
        self.create_tk_window()
        self.create_tk_canvas()

        for i in range(4):
            print("self.node_list[i] = ", self.node_list[i], ", i = ", i)
            if self.value_is_list(self.node_list[i]):
                print(self.get_sub_list(self.get_list_from_string(self.node_list)))

            else:
                fill = "black" if self.node_list[i] else "grey"
                self.tk_window.canvas.create_rectangle(self.node_posx1[i] * self.WIDTH,
                                                       self.node_posy1[i] * self.HEIGHT,
                                                       self.node_posx2[i] * self.WIDTH,
                                                       self.node_posy2[i] * self.HEIGHT,
                                                       fill=fill)

        self.tk_window.canvas.pack()
        self.tk_window.mainloop()

    def get_list_from_string(self, value) -> list:
        for i in range(4):
            self.node_list[i] = eval(value)
        return self.node_list

    @staticmethod
    def get_sub_list(mainlist: list, sublist=None):
        for i in range(4):
            sublist[i] = mainlist[i]
        return sublist

    @staticmethod
    def value_is_list(value: int | list) -> bool:
        if type(value) is list:
            return True

    def create_tk_window(self):
        self.tk_window = Tk()
        return self.tk_window

    def create_tk_canvas(self):
        self.tk_window.canvas = Canvas(self.tk_window, width=self.WIDTH, height=self.HEIGHT)
        return self.tk_window.canvas


first_quadtree = QuadTree(1, 0, 1, 0)

# "../files/quadtree_easy.txt"
# "../files/quadtree.txt"

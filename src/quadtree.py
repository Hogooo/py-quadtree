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

        for i in range(4):
            if self.value_is_list(self.node_list[i]):
                self.depth += 1
                self.get_sub_list(self.get_list_from_string(self.node_list))
            else:
                fill = "black" if self.node_list[i] else "grey"
                self.create_tk_rectangle(self.WIDTH, self.HEIGHT, fill, self.depth)

    @property
    def depth(self):
        return self.depth

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
        self.tk_window.canvas = Canvas(self.tk_window, width=self.WIDTH, height=self.HEIGHT)

    def create_tk_rectangle(self, w, h, fill, depth):
        for i in range(4):
            self.tk_window.canvas.create_rectangle(int(self.node_posx1[i]),
                                                   int(self.node_posy1[i]),
                                                   int(self.node_posx2[i]),
                                                   int(self.node_posy2[i]),
                                                   fill=fill)

    @depth.setter
    def depth(self, value):
        self._depth = value


first_quadtree = QuadTree(1, 0, 1, 0)

# "../files/quadtree_easy.txt"
# "../files/quadtree.txt"

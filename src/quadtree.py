from __future__ import annotations
from tkinter import *


class QuadTree:
    def __init__(self,
                 hg: int | QuadTree,
                 hd: int | QuadTree,
                 bg: int | QuadTree,
                 bd: int | QuadTree):
        self.HEIGHT = self.WIDTH = 256
        self.tk_window = None
        self.node_list = [hg, hd, bg, bd]

        self.create_tk_window()
        for i in range(4):
            if self.value_is_list(self.node_list[i]):
                self.get_sub_list(self.get_list_from_string(self.node_list))
            else:
                pass

    @property
    def depth(self):
        return 1

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

    def create_tk_rectangle(self):
        self.tk_window.canvas.create_rectangle()

first_quadtree = QuadTree(1, 0, 1, 0)

# "../files/quadtree_easy.txt"
# "../files/quadtree.txt"

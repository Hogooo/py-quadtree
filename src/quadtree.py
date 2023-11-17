from __future__ import annotations
from tkinter import *

WIDTH = HEIGHT = 256
node_posx1 = [0, 1, 0, 1]
node_posy1 = [0, 0, 1, 1]
node_posx2 = [1, 2, 1, 2]
node_posy2 = [1, 1, 2, 2]


def get_list_from_string(mainstring) -> list:
    node_list = []
    for i in range(4):
        node_list[i] = eval(mainstring)
    return node_list


def value_is_list(value: int | list) -> bool:
    if type(value) is list:
        return True


def create_tk_window(quadtree):
    tk_window = Tk()
    tk_canvas = Canvas(tk_window, width=(WIDTH * 2), height=(HEIGHT * 2))
    for i in range(len(quadtree.node_list)):
        print("type = ", type(first_quadtree.node_list[i]), ", i = ", i)
        print("x1 = ", node_posx1[i] * WIDTH,
              "y1 = ", node_posy1[i] * HEIGHT,
              "x2 = ", node_posx2[i] * WIDTH,
              "y2 = ", node_posy2[i] * HEIGHT)

        fill = "black" if first_quadtree.node_list[i] else "white"
        tk_canvas.create_rectangle(node_posx1[i] * WIDTH,
                                   node_posy1[i] * HEIGHT,
                                   node_posx2[i] * WIDTH,
                                   node_posy2[i] * HEIGHT, fill=fill)
    tk_canvas.pack()
    tk_window.mainloop()


class QuadTree:

    def __init__(self, hg: int | list, hd: int | list, bg: int | list, bd: int | list):
        self.node_list = [hg, hd, bg, bd]
        self.depth = 0


first_quadtree = QuadTree(1, 0, 0, 1)
create_tk_window(first_quadtree,)
# [1, 0, 0, 1]

# "../files/quadtree_easy.txt"
# "../files/quadtree.txt"

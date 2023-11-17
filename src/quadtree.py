from __future__ import annotations
from tkinter import *

WIDTH = HEIGHT = 256
node_posx1 = [0, 1, 0, 1]
node_posy1 = [0, 0, 1, 1]
node_posx2 = [1, 2, 1, 2]
node_posy2 = [1, 1, 2, 2]


def get_list_from_string(mainstring: str) -> list:
    node_list = []
    for i in range(4):
        node_list = eval(mainstring)
    return node_list


def value_is_list(value: int | list) -> bool:
    if type(value) is list:
        return True


def create_tk_window(quadtree):
    sub_list = []
    tk_window = Tk()
    tk_canvas = Canvas(tk_window, width=(WIDTH * 3), height=(HEIGHT * 3))
    for i in range(len(quadtree.node_list)):

        print("i = ", i, "node_list[i] =", first_quadtree.node_list[i])

        if value_is_list(quadtree.node_list[i]):
            quadtree.increment_depth()
            for j in range(len(quadtree.node_list[i])):
                fill = "black" if first_quadtree.node_list[i][j] == 1 else "white"
                calculated_x1 = WIDTH + (node_posx1[j] / quadtree.depth) * WIDTH
                calculated_y1 = HEIGHT + (node_posy1[j] / quadtree.depth) * HEIGHT
                calculated_x2 = WIDTH + (node_posx2[j] / quadtree.depth) * WIDTH
                calculated_y2 = HEIGHT + (node_posy2[j] / quadtree.depth) * HEIGHT

                print("j =", j, "fill = ", fill)
                print("x1 = ", calculated_x1, "y1 = ", calculated_y1)
                print("x2 = ", calculated_x2, "y2 = ", calculated_y2, "\n")

                tk_canvas.create_rectangle(calculated_x1, calculated_y1, calculated_x2, calculated_y2, fill=fill)

        else:
            fill = "black" if first_quadtree.node_list[i] == 1 else "white"
            print("type = ", type(first_quadtree.node_list[i]))
            print("x1 = ", node_posx1[i] * WIDTH, "y1 = ", node_posy1[i] * HEIGHT)
            print("x2 = ", node_posx2[i] * WIDTH, "y2 = ", node_posy2[i] * HEIGHT)
            print("################################")
            tk_canvas.create_rectangle(node_posx1[i] * WIDTH,
                                       node_posy1[i] * HEIGHT,
                                       node_posx2[i] * WIDTH,
                                       node_posy2[i] * HEIGHT, fill=fill)
    tk_canvas.pack()
    tk_window.mainloop()


class QuadTree:

    @property
    def depth(self):
        return self._depth

    def __init__(self, hg: int | list, hd: int | list, bg: int | list, bd: int | list):
        self._depth = 1
        self.node_list = [hg, hd, bg, bd]

    def increment_depth(self):
        self.depth += 1

    @depth.setter
    def depth(self, value):
        self._depth = value


first_quadtree = QuadTree(1, 0, 0, [1, 0, 0, 1])
create_tk_window(first_quadtree)
# [1, 0, 0, 1]
# [1, 1, 1, 1]

# "../files/quadtree_easy.txt"
# "../files/quadtree.txt"

from __future__ import annotations
from tkinter import *

processed_list = []
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


def get_list_from_list(inner_list: list, index: int) -> list:
    output_list = []
    for inner_i in range(len(inner_list)):
        output_list = inner_list[index]
    return output_list


<<<<<<< Updated upstream
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
=======
def value_is_list(inner_list: list) -> bool:
    output = False
    if type(inner_list) is list:
        output = True
    return output


def list_contain_list(inner_list: list) -> bool:
    output = False
    for inner_i in range(len(inner_list)):
        if type(inner_list[inner_i]) is list:
            output = True
    return output


def calculate_coordinates(value: int, index: int, depth):

    fill = "black" if value == 1 else "white"

    offset_x1 = node_posx1[index] * WIDTH
    offset_y1 = node_posy1[index] * HEIGHT

    offset_x2 = (node_posx2[index] * WIDTH) / depth
    offset_y2 = (node_posy2[index] * HEIGHT) / depth

    x1 = offset_x1
    y1 = offset_y1
    x2 = offset_x2
    y2 = offset_y2

    #  WIDTH HEIGHT depth node_posy2[index]
    # 0, 0, 0.5, 0.5 | 0.5, 0, 1, 0.5 | 1, 0, 1.5, 0.5 | 1.5, 0, 2, 0.5
    # ---------------|----------------|----------------|----------------
    # 0, 0.5, 0.5, 1 | 0.5, 0.5, 1, 1 | 1, 0.5, 1.5, 1 | 1.5, 0.5, 2, 1

    return x1, y1, x2, y2, str(fill)


def process_list(inner_list: list, inner_tk_window, depth=1):
    output_list = []
    print("process_list triggered, depth =", depth)

    for i in range(len(inner_list)):
        processed_value = inner_list[i]

        if value_is_list(processed_value):
            depth += 1
            process_list(processed_value, inner_tk_window, depth)
            depth -= 1
        else:  # value is not a list
            x1, y1, x2, y2, fill = calculate_coordinates(processed_value, i, depth)
            inner_tk_window.create_tk_rectangle(x1, y1, x2, y2, fill, depth)
    return output_list


class TkWindow:
    def __init__(self):
        self.tk_window = Tk()
        self.tk_canvas = Canvas(self.tk_window, width=(WIDTH * 2), height=(HEIGHT * 2))
        self.tk_canvas.pack()

    def create_tk_rectangle(self, inner_x1, inner_y1, inner_x2, inner_y2, inner_fill, depth):
        print("create_rectangle triggered,",
              "x1 =", inner_x1,
              "y1 =", inner_y1,
              "x2 =", inner_x2,
              "y2 =", inner_y2,
              "fill =", inner_fill,
              "depth =", depth, "\n")
        self.tk_canvas.create_rectangle(inner_x1, inner_y1, inner_x2, inner_y2, fill=inner_fill)
>>>>>>> Stashed changes


class QuadTree:
    def __init__(self, hg: int | list, hd: int | list, bg: int | list, bd: int | list):
        self._depth = 1
        self.node_list = [hg, hd, bg, bd]

    @property
    def depth(self):
        return self._depth

<<<<<<< Updated upstream
    def __init__(self, hg: int | list, hd: int | list, bg: int | list, bd: int | list):
        self._depth = 1
        self.node_list = [hg, hd, bg, bd]
=======
    @depth.setter
    def depth(self, inner_value):
        self._depth = inner_value
>>>>>>> Stashed changes

    def increment_depth(self):
        self.depth += 1

<<<<<<< Updated upstream
    @depth.setter
    def depth(self, value):
        self._depth = value

=======
first_quadtree = QuadTree([1, 0, 0, 1], 0, 0, [1, 0, 0, 1])
first_tk_window = TkWindow()
process_list(first_quadtree.node_list, first_tk_window)
first_tk_window.tk_window.mainloop()
>>>>>>> Stashed changes

first_quadtree = QuadTree(1, 0, 0, [1, 0, 0, 1])
create_tk_window(first_quadtree)
# [1, 0, 0, 1]
# [1, 1, 1, 1]

# "../files/quadtree_easy.txt"
# "../files/quadtree.txt"

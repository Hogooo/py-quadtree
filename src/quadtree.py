from __future__ import annotations
from tkinter import *


class QuadTree:
    WIDTH = HEIGHT = 512
    node_posx1 = [0, 1, 0, 1]
    node_posy1 = [0, 0, 1, 1]
    node_posx2 = [1, 2, 1, 2]
    node_posy2 = [1, 1, 2, 2]

    def __init__(self, filename):
        self.get_string_from_file(self, filename)
        self.get_list_from_string(self, self.ligne)
        self.create_tk_window(self)

    @property
    def depth(self) -> int:
        return 2

    @staticmethod
    def get_string_from_file(self, filename: str) -> str:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename, 'r') as filein:
            lignes = filein.readlines()
            for ligne in lignes:
                self.ligne = ligne
            return self.ligne

    @staticmethod
    def get_list_from_string(self, data: str) -> list:
        """ Generates a Quadtree from a list representation"""
        self.value_list = eval(data)
        self.nb_node = len(self.value_list)
        return self.value_list

    @staticmethod
    def value_is_list(value: int | list) -> bool:
        if type(value) is list:
            return True

    @staticmethod
    def get_sub_list(self, mainlist: list):
        for i in range(self.nb_node):
            if self.value_is_list(mainlist[i]):
                self.sublist = self.value_list[i]


    @staticmethod
    def create_tk_window(self):
        """ TK representation of a Quadtree"""
        self.tk_window = Tk()
        self.tk_window.canvas = Canvas(self.tk_window,
                                       width=(self.WIDTH // 2) * self.nb_node,
                                       height=(self.HEIGHT // 2) * self.nb_node)
        for i in range(self.nb_node):
            if not self.value_is_list(self.value_list[i]):
                fill = "black" if self.value_list[i] else "grey"
                self.create_rectangle_from_bool(self, i, fill)
            else:
                self.create_rectangle_from_list(self, i, self.value_list[i])
        self.tk_window.canvas.pack()
        self.tk_window.mainloop()

    @staticmethod
    def create_rectangle_from_bool(self, i, fill):
        self.tk_window.canvas.create_rectangle(int(self.node_posx1[i]) * self.WIDTH,
                                               int(self.node_posy1[i]) * self.HEIGHT,
                                               int(self.node_posx2[i]) * self.WIDTH,
                                               int(self.node_posy2[i]) * self.HEIGHT,
                                               fill=fill)

    @staticmethod
    def create_rectangle_from_list(self, i, value: list):
            fill = "black" if value[i] else "grey"
            self.tk_window.canvas.create_rectangle(fill=fill)




first_quadtree = QuadTree("../files/quadtree_easy.txt")

second_quadtree = QuadTree("../files/quadtree.txt")

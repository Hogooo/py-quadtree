import sys, os, src
from src import QuadTree, TkQuadTree
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 4


def test_single():
    filename = "files/quadtree_easy.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 1
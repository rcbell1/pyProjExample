import numpy as np

import pyProjExample.mult as mult


def test_mult_scalar():
    x = np.array(5)
    y = np.array(8)
    out = x * y
    assert mult.mult_scalar(x, y) == out


def test_mult_mat():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    out = x @ y
    assert (mult.mult_mat(x, y) == out).all()

"""
Write a fully vectorized implementation of scipy.interpolate.interp1d.

For an array of shape (n, 2) that represents a piecewise xy function
and an array of shape (m,) that represents query x coordinates, return
the corresponding y values of shape (m,). Your solution should be as
vectorized as possible.
"""

import numpy as np


def interp1d(xy: np.ndarray, x: np.ndarray):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    x = x.reshape(-1)
    assert xy.shape[-1] == 2
    assert np.all(np.diff(xy[:, 0]) >= 0)

    # TODO
    # -----------------------------------------------
    raise NotImplementedError
    # -----------------------------------------------


if __name__ == "__main__":
    xy = np.array([
        [0.0, 0.0],
        [1.0, 2.0],
        [3.0, 3.0],
    ])
    xs = np.array([-1.0, 0.0, 0.5, 1.5, 3.0, 4.0])
    expected = np.array([0.0, 0.0, 1.0, 2.25, 3.0, 3.0])
    np.testing.assert_allclose(interp1d(xy, xs), expected)

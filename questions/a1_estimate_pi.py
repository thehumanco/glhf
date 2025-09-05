"""
Estimate the value of pi without importing math.pi or np.pi. Your solution
should be as vectorized as possible. You may add (optional) arguments
that control the accuracy of your estimation.
"""

import numpy as np


def estimate_pi():
    # TODO
    # -----------------------------------------------
    raise NotImplementedError
    # -----------------------------------------------


if __name__ == "__main__":
    pi = estimate_pi()
    print("True pi:", np.pi)
    print("Estimated pi:", pi)
    print("Error:", abs(np.pi - pi))

"""
Implement a function that projects 3D points onto an rgb image,
given known camera intrinsics information. You should handle edge
cases such as when projected points are outside image bounds. Your
solution should be as vectorized as possible.
"""

import cv2
import numpy as np
import torch

from questions.b1_dataloader import BinDataset


def plot_points(rgb: np.ndarray, points: np.ndarray, k: np.ndarray):
    assert rgb.ndim == 3 and rgb.shape[-1] == 3
    assert points.ndim == 2 and points.shape[-1] == 3

    # TODO
    # -----------------------------------------------
    raise NotImplementedError
    # -----------------------------------------------


if __name__ == "__main__":
    import imageio.v2 as imageio
    from tqdm import tqdm

    bindataset = BinDataset("./data/glhf.bin")
    binloader = torch.utils.data.DataLoader(
        bindataset,
        batch_size=8,
        shuffle=False,
        num_workers=0,
        drop_last=False,
    )

    with (
        tqdm(total=len(binloader)) as pbar,
        imageio.get_writer("b2_projection.mp4", codec="libx264", fps=30) as writer,
    ):
        for batch in binloader:
            for rgb, c2w, points in zip(*batch):
                rgb = plot_points(rgb.numpy(), points.numpy(), bindataset.k)
                writer.append_data(rgb)
            pbar.update(1)

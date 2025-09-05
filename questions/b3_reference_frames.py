"""
Complete the following script that projects the 3D points in each frame
into the first frame, given known camera intrinsics and extrinsics. You should
reuse your plot_points function from b2_projection.py and plot everything
onto the rgb image of the first frame.
"""

import numpy as np
import torch

from questions.b1_dataloader import BinDataset
from questions.b2_projection import plot_points


if __name__ == "__main__":
    import imageio.v2 as imageio
    from tqdm import tqdm

    bindataset = BinDataset("./data/glhf.bin")
    binloader = torch.utils.data.DataLoader(
        bindataset,
        batch_size=1,
        shuffle=False,
        num_workers=0,
    )
    rgbs, c2ws, points = [], [], []
    
    with (
        tqdm(range(len(binloader)), total=len(binloader)) as pbar,
        imageio.get_writer("b3_reference_frames.mp4", format="mp4", codec="libx264", fps=30) as writer,
    ):
        for i, batch in enumerate(binloader):
            rgb, c2w, points = batch
            rgb, c2w, points = rgb[0].numpy(), c2w[0].numpy(), points[0].numpy()

            # TODO
            # -----------------------------------------------
            # rgb: shape (h, w, 3)
            # c2w: shape (4, 4)
            # points: shape (n, 3)
            raise NotImplementedError
            # -----------------------------------------------

            writer.append_data(rgb)
            pbar.update(1)

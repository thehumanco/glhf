"""
Implement a dataloader that decodes per-frame information from a binary video file.
The file is structured as a header that contains metadata, followed by a stream
of flattened frames.

The file is a concatenation of the header and all frames sequentially. The header is formatted as:

> header = n|p|h|w|fx|fy|cx|cy

Each frame is formatted as follows:

> frame = rgb|pose|points

The variables and types are as follows:
> n (int32): number of frames
> p (int32): number of points per frame
> h (int32): height of the rgb image per frame
> w (int32): width of the rgb image per frame
> fx (float32): x-axis focal length of the camera
> fy (float32): y-axis focal length of the camera
> cx (float32): x-axis principal point of the camera
> cy (float32): y-axis principal point of the camera

> rgb (uint8): flattened rgb image originally of shape (h, w, 3)
> pose (float32): 7d camera pose of concatenated [quaternion, translation]
> points (float32): flattened array of 3d points originally of shape (p, 3)

You should implement the functions of the torch dataset to retrieve and decode
the per-frame information.
"""

import numpy as np
import torch
from scipy.spatial.transform import Rotation as R


class BinDataset(torch.utils.data.Dataset):

    def __init__(self, bin: str):
        super().__init__()

        # TODO
        # -----------------------------------------------
        pass
        # -----------------------------------------------

    @property
    def k(self):
        """Returns the 3x3 camera intrinsics matrix"""
        # TODO
        # -----------------------------------------------
        raise NotImplementedError
        # -----------------------------------------------

    def __len__(self):
        """Returns the number of frames"""
        # TODO
        # -----------------------------------------------
        raise NotImplementedError
        # -----------------------------------------------

    def __getitem__(self, idx: int):
        """Returns the decoded payload of frame `i` as:
        
            > rgb (np.uint8): rgb image of shape (h, w, 3)
            > c2w (np.float32): camera extrinsics matrix of shape (4, 4)
            > points (np.float32): an array of 3d points of shape (p, 3)
        """
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
        imageio.get_writer("b1_dataloader.mp4", codec="libx264", fps=30) as writer,
    ):
        for batch in binloader:
            for rgb in batch[0]:
                writer.append_data(rgb.numpy())
            pbar.update(1)

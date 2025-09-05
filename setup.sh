#!/bin/bash

python -m pip install -r requirements.txt

# if setting up answer key repository
if [ "$(basename "$PWD")" = "glfh-answers" ]; then
    # download aria devignetting masks
    gdown "https://drive.google.com/uc?id=1hVXvs-hisRZRqMn9b0j_6eW2OZbeCru-&confirm=t"
    unzip devignetting_masks_bin.zip -d devignetting_masks_bin
    rm -rf devignetting_masks_bin.zip

    # download starter dataset
    mkdir -p data/
    cd data/
    gdown "https://drive.google.com/uc?id=1yLr1w8oe9FS3FQHJgrlxJimqgGtyD85x&confirm=t"
    tar -zxf mps_interview_vrs.tar.gz
    cd ../

# if setting up interview candidate repository
else
    # download binarized video file
    mkdir -p data/
    cd data/
    gdown "https://drive.google.com/uc?id=1_lHYRtf40GmQMaZyvsuDXmFeDEdgC6q2&confirm=t"
    cd ../
fi

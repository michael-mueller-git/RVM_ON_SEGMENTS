### SETUP

REQUIREMENTS:
CUDA-Capable GPU ( which should be the most modern nvidia GPUs)

## 1. Download and extract this repository locally:
<img width="861" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/4e37c013-f088-45cf-9a75-b1574c703008">

## 2. Install Miniconda:
https://docs.anaconda.com/free/miniconda/index.html

After installation, verify that you've conda available:
Open up command prompt, type in Conda, it should show this:
<img width="838" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/da52d599-e214-4d3f-8c6e-81f9742499e1">

## 3. Setup the python conda environment that these scripts will use!

3.1 Open Command Prompt
3.2. Type in and execute:

`conda activate base`

3.3. Once base conda is activated, type in and execute:

`conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia  `

This installs the core dependency of pytorch that this whole project requires!
Subject to changes based on this:
https://pytorch.org/get-started/locally/

3.4. Once this is done go to the folder you've extracted, in the explorer bar, type in `cmd`
<img width="946" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/7e2a9211-edb1-448f-9609-24672078372e">

This brings up the command prompt with the current directory set to this (you can CD directly to it if you know how to )

3.5. `Conda activate base` again

3.6. Type in: 
pip install -r requirements_inference.txt

This will install the rest of the dependencies needed!

## 4. Install FFMPEG:
https://phoenixnap.com/kb/ffmpeg-windows

We need this to split up the segments, and recombine them after


###

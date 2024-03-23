# SETUP
First you need to get setup!

REQUIREMENTS:
- Windows PC ( This guide is written for a windows user, unfortunately I don't use Linux or MacOS so i can't help you there)
- CUDA-Capable GPU ( which should be most modern nvidia GPUs)

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

3.6. Type in and execute: 

`pip install -r requirements_inference.txt`

This will install the rest of the dependencies needed!

## 4. Install FFMPEG:
https://phoenixnap.com/kb/ffmpeg-windows

We need this to split up the segments, and recombine them after


# PRE-INFERENCE

Before you start inferencing you need to split up long-form videos into segments!
- This makes the overall inference process more reliable as you wouldn't block the whole inference process due to one small decoding problem
- Becomes less of a memory hog, it can eat up a lot of memory or even run out of memory trying to infer on a 15 minutes 8K video!
- Plus you can stop the process at any time and restart the inference on remaining video segments because the inferenceCustom.py script is designed for it. 

## 1. Drag and Drop the video:
<img width="713" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/1d0860ff-9a06-4d8b-ae24-36bd29ac1c12">

## 2. Specify how long each segment should be:
<img width="867" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/2b30f8b9-148a-413a-8451-ffb99839b024">

The shorter the segment, the more matting pops you will see when the video is combined but it also drastically reduces the amount of memory hog and improves reliability of the whole inference process (I like to go with 15 seconds here)

## 3. After the process is done, confirm that the output is good!
<img width="1158" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/343c31fc-c38c-4a8f-ad0a-162afa3650d7">
There should be a folder named the same as the video but with a suffix of "_segments"
There should be segmented mp4 here + a file_list.txt


# INFERENCING

Inferencing is the act of "inferring" data from the input using the model that has been trained; in this case we want the segments to be used to infer alpha mattes from the model ( rvm_mobilenetv3.pth )

That's handled by inferenceCustom.py!

All you need to do is to:
## 1. Drag and Drop Segments folder onto the "INFER_ON_VIDEO_SEGMENTS.bat"
<img width="662" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/57cd1df3-bea6-406a-872c-bcc22c9c6d23">
## 2. Decide if you want to shutdown the computer after inference is done:
<img width="865" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/ffa553c6-504c-405d-8aaf-efd499b7b343">
I added this because sometimes the inference can run for up to 40 hours on 40 minutes of footage, so i prefer to let it shutdown itself after it's done to save power.

# POST-INFERENCING

Now that inference is done and you have matted video segments, you need to combine them together!

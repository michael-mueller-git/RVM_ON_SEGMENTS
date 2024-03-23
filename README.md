REQUIREMENTS:
CUDA-Capable GPU ( which should be the most modern nvidia GPUs)

### Download and extract this into a location


### Install Miniconda:
https://docs.anaconda.com/free/miniconda/index.html

After installation, verify that you've conda available:
Open up command prompt, type in Conda, it should show this:
<img width="838" alt="image" src="https://github.com/blewClue215/RVM_ON_SEGMENTS/assets/154766775/da52d599-e214-4d3f-8c6e-81f9742499e1">

### Setup the python conda environment that these scripts will use!

1. Open Command Prompt
2. Type in and execute:

`conda activate base`

4. Once base conda is activated, type in and execute:

`conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia  `

subject to changes based on this:
https://pytorch.org/get-started/locally/

5. Once this is done

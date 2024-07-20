from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
from inference_utils import VideoReader, VideoWriter, ImageSequenceWriter
import torch
from model import MattingNetwork
import cv2
import os
import argparse
import glob
import json
import shutil
from tqdm.auto import tqdm


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        #print(f"Folder '{folder_path}' created successfully.")
    #else:
        #print(f"Folder '{folder_path}' already exists.")

# --------------- Arguments ---------------
parser = argparse.ArgumentParser(description='Test Video')
parser.add_argument('--input_folder', type=str, required=True)
parser.add_argument('--output_folder', type=str, required=True)
args = parser.parse_args()

model = MattingNetwork(variant='mobilenetv3').eval().cuda() # Or variant="resnet50"
model.load_state_dict(torch.load('rvm_mobilenetv3.pth'))

# Get all mp4 files in the folder
mp4_files = glob.glob(args.input_folder + '/*.mp4')
json_file_path = f'{args.output_folder}/processed.json'

processDict = {}

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        # Load JSON data into a Python dictionary
        processDict = json.load(json_file)

compFolderPath = f"{args.output_folder}/COMPOSITE"
ensure_folder_exists(compFolderPath)

for mp4_file in mp4_files:
    filename = mp4_file.split("\\")[-1]
    compFilepath = f"{compFolderPath}/{filename}"

    if (compFilepath in processDict.keys()) and (processDict[compFilepath] == True):
        print(f"{filename} already processed, skipping!")
        continue

    print(f"Processing {filename}")
    processDict[compFilepath] = False

    # Write the updated data to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(processDict, json_file, indent=4)

    try:
        source = VideoReader(mp4_file, transform=ToTensor())
        frame_rate = source.frame_rate if isinstance(source, VideoReader) else 30
        output_video_mbps = 40
        writer_com = VideoWriter(compFilepath, frame_rate=frame_rate, bit_rate=output_video_mbps * 1000000)
        bgr = torch.tensor([.47, 1, .6]).view(3, 1, 1).cuda()  # Green background.
        reader = DataLoader(source)

        with torch.no_grad():
            bar = tqdm(total=len(source), disable=False, dynamic_ncols=True)
            rec = [None] * 4  # Initial recurrent states.
            for src in reader:
                fgr, pha, *rec = model(src.cuda(), *rec, downsample_ratio=0.4)  # Cycle the recurrent states.
                com = fgr * pha + bgr * (1 - pha)
                writer_com.write(com)
                bar.update(src.size(1))
        writer_com.close()
    except Exception as e:
        print(e)
        print(f"{filename} failed, skipping")
        continue

    processDict[compFilepath] = True
    with open(json_file_path, 'w') as json_file:
        json.dump(processDict, json_file, indent=4)

FROM anibali/pytorch:1.8.1-cuda11.1-ubuntu20.04
USER 0
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install -y pkg-config libavformat-dev libswresample-dev libswscale-dev libavfilter-dev libavutil-dev libavdevice-dev libavcodec-dev git build-essential vim
RUN git clone https://github.com/michael-mueller-git/RVM_ON_SEGMENTS.git
RUN cd RVM_ON_SEGMENTS && pip install -r requirements_inference.txt
WORKDIR /app/RVM_ON_SEGMENTS
CMD python inferenceCustom.py --input_folder "/in" --output_folder "/out"

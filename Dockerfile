FROM nvidia/cuda:11.7.1-devel-ubuntu20.04
LABEL maintainer="Alexander Hunt <alexander.hunt@ed.ac.uk>"
LABEL description="Docker image setup to use Darknet with Cuda 11.7.1, Cudnn 8 and OpenCV 4.6.0 on Ubuntu 20.04"
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        tzdata \
    && rm -rf /var/lib/apt/lists/*
RUN apt update && apt upgrade -y
RUN apt install libcudnn8* wget unzip -y
RUN apt install python3 python-is-python3 python3-pip -y
RUN apt install wget git libssl-dev zip unzip libeigen3-dev libgflags-dev libgoogle-glog-dev -y
RUN apt-get install libjpeg-dev libpng-dev libtiff-dev libopenjp2-7-dev -y
RUN apt-get install libavcodec-dev libavformat-dev libswscale-dev -y
RUN apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev -y
RUN apt-get install libxvidcore-dev x264 libx264-dev libfaac-dev libmp3lame-dev libtheora-dev -y
RUN apt-get install libfaac-dev libvorbis-dev -y
RUN apt-get install libopencore-amrnb-dev libopencore-amrwb-dev -y
RUN apt-get install libgtk-3-dev -y
RUN apt-get install libtbb-dev -y
RUN apt-get install libprotobuf-dev protobuf-compiler -y
RUN apt-get install libgoogle-glog-dev libgflags-dev -y
RUN apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen -y
RUN apt-get install libgtkglext1 libgtkglext1-dev -y
RUN apt-get install libopenblas-dev liblapacke-dev libva-dev libopenjp2-tools libopenjpip-dec-server libopenjpip-server libqt5opengl5-dev libtesseract-dev -y

RUN wget https://github.com/Kitware/CMake/releases/download/v3.24.2/cmake-3.24.2.tar.gz
RUN tar -xzf cmake-3.24.2.tar.gz 
RUN cd cmake-3.24.2 && ./bootstrap && make -j$(nproc) && make install
RUN cd && rm -rf cmake-3.24.2.tar.gz
# RUN git clone https://ceres-solver.googlesource.com/ceres-solver && cd ceres-solver && mkdir build && cd build
# RUN cd ceres-solver/build && cmake .. && make -j$(nporc) && make test && make install
# RUN cd 
RUN pip3 install --upgrade pip
RUN pip3 install numpy

RUN wget https://github.com/opencv/opencv/archive/refs/tags/4.6.0.zip && unzip 4.6.0.zip
RUN wget https://github.com/opencv/opencv_contrib/archive/refs/tags/4.6.0.tar.gz && tar -xvf 4.6.0.tar.gz
RUN rm 4.6.0.zip 4.6.0.tar.gz

RUN cd opencv-4.6.0 && mkdir build && cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE  -D CMAKE_INSTALL_PREFIX=/usr/local  -D WITH_TBB=ON  -D ENABLE_FAST_MATH=1  -D CUDA_FAST_MATH=1  -D WITH_CUBLAS=1  -D WITH_CUDA=ON  -D BUILD_opencv_cudacodec=ON  -D WITH_CUDNN=ON  -D OPENCV_DNN_CUDA=ON  -D CUDA_ARCH_BIN=8.6  -D WITH_V4L=ON  -D WITH_QT=OFF -D WITH_GTK_2_X=ON -D WITH_OPENGL=ON  -D WITH_GSTREAMER=ON  -D OPENCV_GENERATE_PKGCONFIG=ON  -D OPENCV_PC_FILE_NAME=opencv.pc  -D OPENCV_ENABLE_NONFREE=ON  -D INSTALL_PYTHON_EXAMPLES=ON  -D INSTALL_C_EXAMPLES=ON  -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib-4.6.0/modules  -D BUILD_EXAMPLES=ON  ..
RUN cd opencv-4.6.0 && cd build && cmake --build . --target install --parallel $(nproc)

RUN apt install tmux -y
RUN rm -rf opencv-4.6.0 opencv_contrib-4.6.0
COPY matrix.sh matrix.sh
RUN chmod +x matrix.sh
RUN git clone https://github.com/AlexeyAB/darknet 
COPY Makefile-docker darknet/Makefile
RUN cd darknet && make -j$(nproc)
RUN apt install curl jq -y
ENTRYPOINT ["bash"]



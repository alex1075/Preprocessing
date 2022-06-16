FROM nvidia/cuda:11.5.0-cudnn8-devel-ubuntu20.04
LABEL maintainer="Alexander Hunt <alexander.hunt@ed.ac.uk>"
RUN apt-get update && apt-get upgrade -y

# Set the locale and timezone
RUN apt-get -y install locales
RUN ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime
RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata
# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8   

# Install OpenCV with CUDA and CUDNN support
RUN apt install wget git libssl-dev zip cmake unzip -y
WORKDIR /root/
RUN cd 
RUN wget https://github.com/opencv/opencv/archive/4.5.5.zip
RUN unzip 4.5.5.zip
RUN wget https://github.com/opencv/opencv_contrib/archive/refs/tags/4.5.5.tar.gz
RUN tar -xzf 4.5.5.tar.gz
RUN cd opencv-4.5.5 && mkdir build && cd build

RUN cd opencv-4.5.5 && cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE \
 -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D WITH_TBB=ON \
 -D ENABLE_FAST_MATH=1 \
 -D CUDA_FAST_MATH=1 \
 -D WITH_CUBLAS=1 \
 -D WITH_CUDA=ON \
 -D BUILD_opencv_cudacodec=OFF \
 -D WITH_CUDNN=ON \
 -D OPENCV_DNN_CUDA=ON \
 -D CUDA_ARCH_BIN=5.2 \
 -D WITH_V4L=ON \
 -D WITH_QT=OFF \
 -D WITH_OPENGL=ON \
 -D WITH_GSTREAMER=ON \
 -D OPENCV_GENERATE_PKGCONFIG=ON \
 -D OPENCV_PC_FILE_NAME=opencv.pc \
 -D OPENCV_ENABLE_NONFREE=ON \
 -D INSTALL_PYTHON_EXAMPLES=OFF \
 -D INSTALL_C_EXAMPLES=OFF \
 -D OPENCV_EXTRA_MODULES_PATH=/root/opencv_contrib-4.5.5/modules \
 -D BUILD_EXAMPLES=OFF  ..
RUN cd opencv-4.5.5 && cd build && cmake --build . --target install --parallel $(nproc)
RUN cd && rm -rf opencv-4.5.5.zip  4.5.5.tar.gz 

RUN apt install python3-pip -y
COPY code.py /root/code.py
COPY requirements.txt /root/requirements.txt
RUN touch __innit__.py
RUN cd /root && pip3 install -r requirements.txt
RUN mkdir -p /Volumes/PHD
CMD ["python3 -c "from code import *; iterateBlur()""]

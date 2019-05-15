
#Install 
apt-get update
apt-get upgrade -y
apt-get install vim -y
apt-get install python3-pip -y
apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*
apt-get install python3-opencv

cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
python3 setup.py install --yes USE_AVX_INSTRUCTIONS
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
cd ..
python3 setup.py install


#Python packegs
pip3 install numpy
pip3 install imutils
pip3 install tensorflow
pip3 install tflearn
pip3 install scipy

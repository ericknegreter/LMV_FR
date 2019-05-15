
#Install 
apt-get update
apt-get upgrade -y
apt-get install vim -y
apt-get install python-pip -y
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
    python-dev \
    python-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*
apt-get install python-opencv


#Python packegs
pip install dlib
pip install numpy
pip install imutils
pip install tensorflow
pip install tflearn
pip install scipy

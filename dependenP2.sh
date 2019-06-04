
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
apt-get install apache2 libapache2-mod-php7.0 -y
apt-get install mysql-server mysql-client -y
apt-get install php7.0 -y
apt-get install php7.0 php7.0-mysql php7.0-curl php7.0-json -y
apache2 restart
apt-get install mpg321

#Python packegs
pip install dlib
pip install numpy
pip install imutils
pip install tensorflow
pip install tflearn
pip install scipy
pip install mysql-connector-python
pip install gTTS
pip install paramiko

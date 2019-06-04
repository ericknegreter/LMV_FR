
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
apt-get install apache2 libapache2-mod-php7.0 -y
apt-get install mysql-server mysql-client -y
apt-get install php7.0 -y
apt-get install php7.0 php7.0-mysql php7.0-curl php7.0-json -y
apache2 restart
apt-get install mpg321 -y

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
pip3 install mysql-connector-python
pip3 install gTTS

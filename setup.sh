#! /bin/bash -f 

dir_packages="packages"

cd $dir_packages

dir_packages=`pwd`

# python 3

if [ ! -e "python3" ]
then
    wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz 
    tar -xzf Python-3.6.6.tgz
    mkdir python3
    cd Python-3.6.6    
    ./configure --prefix=${dir_packages}/python3
    make
    make test
    make install
    cd ..
    rm Python-3.6.6.tgz
    rm -rf Python-3.6.6
fi

# numpy

python3/bin/pip3.6 install numpy --no-deps

# astropy

python3/bin/pip3.6 install astropy --no-deps

# matplotlib

packages/python3/bin/pip3.6 install matplotlib --no-deps


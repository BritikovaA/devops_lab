#!/bin/bash

sudo yum install python-pip
sudo yum -y install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

cat <<EOF >> ~/.bashrc
export PATH="/home/$USER/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)" 
eval "\$(pyenv virtualenv-init -)"
EOF

source ~/.bashrc

pyenv install 2.7.16
pyenv install 3.7.0

sudo pip install virtualenv

pyenv virtualenv 2.7.16 environment_2.7
pyenv virtualenv 3.7.0 environment_3.7


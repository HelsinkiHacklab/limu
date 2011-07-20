#!/bin/sh
# Shell script for setting up fresh install of limumaatti
#
# (C) 2011 Juha Autero
#
SETUPDIR=$HOME/limu/server-setup
LIMUHOST=limumaatti

echo "Setting password for $USER"
passwd

echo "Add universe to sources.list"
sudo vi /etc/apt/sources.list
# Installing missing modules
sudo apt-get install sshd xserver-xorg-input-elographics yaml-python
sudo service gdm stop
cp $SETUPDIR/xorg.conf /etc/X11/
sudo service gdm start
echo "$LIMUHOST" >/etc/hostname

cd limu
# Setup server
git submodule init
git submodule update
cd limuweb
# Create databases
./managedb.py syncdb
# Load product information
./managedb.py loaddata product_data
# Start server
# ./managedb.py runserver &

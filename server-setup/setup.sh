#!/bin/sh
# Shell script for setting up fresh install of limumaatti
#
# (C) 2011 Juha Autero
#
SETUPDIR=$HOME/limu/server-setup
LIMUHOST=limumaatti

echo "Setting password for $USER"
passwd

if ls /var/lib/apt/lists/*universe* >/dev/null 2>&1; then
    echo "Universe already exists"
else
    echo "Add universe to sources.list"
    sudo vi /etc/apt/sources.list
fi
# Installing missing modules
sudo apt-get update
sudo apt-get install openssh-server xserver-xorg-input-elographics python-yaml
if [ ! -e /etc/X11/xorg.conf ]; then
    sudo service gdm stop
    sudo cp $SETUPDIR/xorg.conf /etc/X11/
    sudo service gdm start
fi

if [ `cat /etc/hostname` != $LIMUHOST ]; then
    sudo echo "$LIMUHOST" >/etc/hostname
fi

# Setup server
git submodule init
git submodule update
cd limuweb
# Create databases
./manage.py syncdb
# Load product information
./manage.py loaddata product_data
# Start server
./manage.py runserver

#!/bin/sh
# Shell script for setting up fresh install of limumaatti
#
# (C) 2011 Juha Autero
#

cd limuweb
# Create databases
./managedb.py syncdb
# Load product information
./managedb.py loaddata product_data
# Start server
./managedb.py runserver

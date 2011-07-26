# Script to bootstrap limumaatti on clean Ubuntu install.
sudo apt-get install git
# TODO switch to HelsinkiHacklab fork once it has all necessary data.
git clone https://github.com/jautero/limu.git
sh limu/server-setup/setup.sh

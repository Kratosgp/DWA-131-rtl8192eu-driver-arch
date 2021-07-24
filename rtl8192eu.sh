#!/bin/bash

sudo pacman -S git linux-headers-generic build-essential dkms;
sleep 5

git clone https://github.com/Kratosgp/DWA-131-rtl8192eu-driver-arch.git;
sleep 5

tar -xzvf rtl8192eu-linux-driver-realtek-4.4.x.tar.gz;

cd rtl8192eu-linux-driver-realtek-4.4.x

sudo dkms add .;
sleep 3

sudo dkms install rtl8192eu/1.0;
sleep 2

echo "blacklist rtl8xxxu" | sudo tee /etc/modprobe.d/rtl8xxxu.conf;
sleep 3

echo -e "8192eu\n\nloop" | sudo tee /etc/modules;
sleep 3

echo "options 8192eu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/8192eu.conf;
sleep 3

read -p "Do you wish to reboot now?(Y/n): " Input

if [[ $Input = "n" ]];
then
    echo " "
elif  [[ $Input = "Y" ]] | [[ " " ]]
then
    sleep 2
    systemctl reboot -i
fi


# DWA-131(rtl8192eu) driver for LINUX

*This repository only contains the wifi driver.*

You do **NOT** have to download any files manually just - Follow the Installation, automatically driver will be installed to your pc through shell script made by me.


This tree supports Dynamic Kernel Module Support (DKMS), a system for generating kernel modules from out-of-tree kernel sources. It can be used to install/uninstall kernel modules, and the module will be automatically rebuilt from source when the kernel is upgraded (for example using your package manager).



**Installation:**

*Run the following commands in your terminal:*

   1. Download git using pacman
   
    sudo pacman -S git

   2. Locate to your Downloads directory and download the files

    cd Downloads/ && git clone https://github.com/Kratosgp/DWA-131-rtl8192eu-driver-arch.git
    
   3. Locate to the File directory 
   
    cd DWA-131-rtl8192eu-driver-arch/

   4. Grant Permissions for execution of the shell script

    chmod +x rtl8192eu.sh

   5. To run the downloaded shell script
   
    ./rtl8192eu.sh
            
 ***Note: Your PC needs a REBOOT after the installation is complete***


**Checking:**

   Check that your kernel has loaded the right module:
   
    sudo lshw -c network
            
   You should see the line `driver=8192eu`
   
 ***OPTIONAL USAGES:***
   
 **Uninstall:**
   

   If you wish to uninstall the driver at a later point, use 
   
   `sudo dkms uninstall rtl8192eu/1.0`
   
   To completely remove the driver from DKMS use 
   
   `sudo dkms remove rtl8192eu/1.0 --all`

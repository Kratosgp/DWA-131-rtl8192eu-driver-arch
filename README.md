# DWA-131(rtl8192eu) driver for LINUX

*This repository only contains the wifi driver.*

Follow the Installation, automatically driver will be installed to your pc through shell script obtained from another repository.


This tree supports Dynamic Kernel Module Support (DKMS), a system for generating kernel modules from out-of-tree kernel sources. It can be used to install/uninstall kernel modules, and the module will be automatically rebuilt from source when the kernel is upgraded (for example using your package manager).



**Installation:**

*Run the following commands in your terminal:*

   1. Download git using pacman 

            sudo pacman -S git
        
   2. Locate to your Downloads directory 

            cd Downloads/

   3. Download the shell file using git clone 

            git clone https://github.com/Kratosgp/DWA-131-Shell-script.git

   4. To run the downloaded shell script
   
            ./rtl8192eu.sh
            
 ***Note: Your PC will REBOOT after the installation is complete***


**Checking:**

   Check that your kernel has loaded the right module:
   
            sudo lshw -c network
            
   You should see the line `driver=8192eu`
   
 ***OPTIONAL USAGES:***
   
 **Uninstall:**
   
   If you wish to uninstall at a later point,
   
   If you wish to uninstall the driver at a later point, use 
   
   `sudo dkms uninstall rtl8192eu/1.0`
   
   To completely remove the driver from DKMS use 
   
   `sudo dkms remove rtl8192eu/1.0 --all`

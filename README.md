# DWA-131(rtl8192eu) driver for LINUX

This is the source of DWA-131 WiFi Adapter driver, in here you can find the instructions to install this driver in your pc.
This is just the source of the driver.
The installation shell script can be found in another github link.
Follow the Installation process to finish you Installtion with the shell script from another github link.

This tree supports Dynamic Kernel Module Support (DKMS), a system for generating kernel modules from out-of-tree kernel sources. It can be used to install/uninstall kernel modules, and the module will be automatically rebuilt from source when the kernel is upgraded (for example using your package manager).

**Installation:**

*Run the following commands in your terminal:*

   1. Download git using pacman 

            sudo pacman -S git
        
   2. Locate to your Downloads directory 

            cd Downloads/

   3. Download the shell file using git clone 

            git clone 

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

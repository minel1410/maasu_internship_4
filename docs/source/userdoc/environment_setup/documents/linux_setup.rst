=======================================
Development Environment Setup for Linux
=======================================


Installing VSCode and Lark
-------------------------------


Follow these steps to install Visual Studio Code (VSCode) and Lark on Ubuntu:

1. First, update your system by typing:

   .. code-block:: bash

      sudo apt-get update

2. To install VSCode, use the following command:

   .. code-block:: bash

      sudo snap install --classic code

3. Next, download the Lark application from this link(make sure to choose Linux as your OS):

   `Lark Download <https://www.larksuite.com/en_us/download>`_

4. Once the package is downloaded, install it using the following command (replace `packagename` with the actual name of the downloaded package):

   .. code-block:: bash

      sudo dpkg -i packagename



Installing the necessary tools
------------------------------

To set the tools up on Linux, the following shall be executed in Linux terminal:

:: 

    sudo apt -y update
    sudo apt -y install gcc-arm-none-eabi make stlink-tools git
    sudo apt-get install dfu-util


`Source <https://github.com/cpq/bare-metal-programming-guide?tab=readme-ov-file>`_
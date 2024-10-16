=============================
Development Environment Setup
=============================

To set up the development environment for the STM32 microcontrollers without using the STM32CubeIDE, the following tools are necessary, regardless of the OS:

    - `ARM GCC <https://launchpad.net/gcc-arm-embedded>`_ - for compiling and linking
    - `GNU make <http://www.gnu.org/software/make/>`_ - for build automation
    - `ST link <https://github.com/stlink-org/stlink>`_ - for flashing
    - `Git <https://git-scm.com/>`_ - for downloading source code and version control

To perform the setup for your preferred OS, navigate the following pages:

.. toctree::
   :maxdepth: 2
   :caption: OS-based instructions

   documents/ssd_setup.rst
   documents/windows_setup
   documents/linux_setup
   documents/setup_verification
   documents/VScode_setup

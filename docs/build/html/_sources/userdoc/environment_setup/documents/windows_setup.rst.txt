=========================================
Development Environment Setup for Windows
=========================================

To set the tools up on Windows, the following setup instructions shall be followed:

    1. Download and install `gcc-arm-none-eabi-10.3-2021.10-win32.exe <https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-win32.exe?rev=29bb46cfa0434fbda93abb33c1d480e6&hash=3C58D05EA5D32EF127B9E4D13B3244D26188713C>`_. Enable "Add path to environment variable" during the installation.
    2. Create `C:\\tools` folder.
    3. Download `make-4.4.1-without-guile-w32-bin.zip <https://sourceforge.net/projects/ezwinports/files/make-4.4.1-without-guile-w32-bin.zip/download>`_ and unpack `bin/make.exe` into `C:\\tools`.
    4. Add `C:\\tools` intoo the `Path` environment variable.
    5. Enable `Developer Mode` in Windows 10/11, for symbolic link support.
    6. Install `Git <https://git-scm.com/download/win>`_ if not installed already. 


`Source <https://github.com/cpq/bare-metal-programming-guide?tab=readme-ov-file>`_
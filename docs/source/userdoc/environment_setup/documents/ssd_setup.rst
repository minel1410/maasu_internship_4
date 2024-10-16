=================================
How to Format the MAASU SSD
=================================

Follow these steps to format the MAASU SSD and install Ubuntu Linux:

1. On Windows, search for "cmd" in the search bar, then right-click and select **Run as Administrator**.

2. In the Command Prompt, type the following to enter the disk management utility:

   .. code-block:: bash

      diskpart

3. To display all available drives, type:

   .. code-block:: bash

      list disk

4. Identify the MAASU SSD by size, then choose it carefully by typing:

   .. code-block:: bash

      select disk [disk number]

   Make sure to replace `[disk number]` with the correct number. **Be cautious not to select the wrong disk.**

5. To erase the disk, type:

   .. code-block:: bash

      clean

6. Next, create a primary partition by typing:

   .. code-block:: bash

      create partition primary

7. Format the partition as NTFS by typing:

   .. code-block:: bash

      format fs=ntfs quick

8. After formatting is complete, restart your PC.

9. While restarting, press the **Delete** key multiple times to enter the BIOS.

10. In the BIOS, look for **Boot Devices** and select the USB containing the **Linux Ubuntu ISO** file.

11. You will be prompted to install the operating system. When asked to choose a destination for installation, select the MAASU SSD.

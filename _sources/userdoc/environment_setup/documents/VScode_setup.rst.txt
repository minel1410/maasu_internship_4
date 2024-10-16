============
VSCode Setup
============

The IDE utilized in this project for both, development and documentation, is `Visual Studio Code <https://code.visualstudio.com/>`_. To ease the overall workflow and development process, as well as making the documentation uniform, certain VSCode extensions must be installed first.

Documentation
-------------

To create uniform documentation without hassle, which follows the predefined template, incorporating necessary information for each specific documentation categories, snippets are used. There are several different snippets that shall be added, and to have a straightforward way managing them, a snippet manager is needed. The first extension that shall be downloaded is called Snippets Manager, and has VSCode extension ID: ``zjffun.snippetsmanager``.

There are several snippets that shall be added. When you install and enable the mentioned extension, you can click on a square on the left side bar, labeled as Snippets. An overview shall open, with 4 different categories. To add a snipet relevant only for the workspace, you can hover over the `Workspace Snippets` and click `+` to add a new snippet. A dropdown menu will open, providing you with a list of languages you want to create the snippet in. For documentation, we need to select `reStructuredText`. A file will open, in which you can paste the code relevant for each needed snippet. There are several code blocks that need to be inserted:

.. code-block:: json

        "Requirements Snippet": {
            "prefix": " req",
            "body": [
                ".. ${1:req}:: ${2:label}",
                "   :id: ${3:REQ_INT3_$CURRENT_SECONDS_UNIX}",
                "   :status: Draft",
                "   :date-released:",
                "   :priority: Low",
                "   :submitted-by: Ime Prezime",
                "   :modified-by:",
                "   :category: Functional",
                "   :safety-asil: ",
                "   :references: ",
                "   :verification-and-validation: ",
                "",
                "   ${4:description}",
                "${5}"
            ],
            "description": "Custom sphinx directive"
        },

.. req:: label
   :id: REQ_INT3_1728980918
   :status: Draft
   :date-released:
   :priority: Low
   :submitted-by: Minel Salihagic
   :modified-by:
   :category: Functional
   :safety-asil: 
   :references: 
   :verification-and-validation: 

   description


Git Setup Guide
---------------

Follow these steps to install and configure Git, generate an SSH key, and connect it to your GitHub account for seamless Git usage in Visual Studio Code (VSCode):

1. **Update Your Package List**

   First, make sure your package list is up-to-date by running:

   .. code-block:: bash

      sudo apt-get update

2. **Install Git**

   Next, install Git with the following command:

   .. code-block:: bash

      sudo apt install git

   After installation, verify that Git is correctly installed by checking its version:

   .. code-block:: bash

      git --version

   This will display the installed version of Git.

3. **Configure Git User Information**

   Now, configure Git with your name and email. These will be associated with your commits:

   .. code-block:: bash

      git config --global user.name "Your Name"
      git config --global user.email "your_email@example.com"

4. **Generate an SSH Key**

   To securely connect to GitHub, generate an SSH key using RSA encryption:

   .. code-block:: bash

      ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

   Follow the prompts and press **Enter** to accept the default location for saving the key (`/home/your_username/.ssh/id_rsa`). You can also set an optional passphrase.

5. **Copy Your SSH Key to Clipboard**

   To copy the generated SSH key to your clipboard, run the following command:

   .. code-block:: bash

      cat ~/.ssh/id_rsa.pub

   Select and copy the entire output. This is your public SSH key.

6. **Add SSH Key to Your GitHub Account**

   Now, add your SSH key to your GitHub account:

   - Log in to **GitHub**.
   - Go to **Settings > SSH and GPG keys**.
   - Click **New SSH key**, give it a title (e.g., "MAASU SSH"), and paste your SSH key.
   - Click **Add SSH key**.

7. **Test Your SSH Connection**

   Verify that the SSH key is working by testing the connection to GitHub:

   .. code-block:: bash

      ssh -T git@github.com

   You should receive a message confirming that you've successfully authenticated.

8. **Try Cloning a Repository**

   Now that Git is configured with SSH, you can test everything by cloning a repository from GitHub:

   .. code-block:: bash

      git clone git@github.com:username/repository.git

   If the repository is cloned successfully, your setup is complete!

That's it! Your Git and VSCode setup is now ready for use. To test, you should try cloning a test repo and commiting.

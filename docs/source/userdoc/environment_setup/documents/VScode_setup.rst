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


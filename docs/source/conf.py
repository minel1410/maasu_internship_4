# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_rtd_theme
from sphinx_needs.api.configuration import add_dynamic_function
from sphinx_needs.api.configuration import add_warning
sys.path.insert(0, os.path.abspath("../.."))

project = 'Maasu Internship 4'
copyright = '2024, Maasu BH d.o.o.'
author = 'Muna Abu Jaber, Muhamed Trumic'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_needs',
              'sphinx.ext.autodoc',
              'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# === SPHINX NEEDS ===========================================================

needs_id_regex = r"^(REQ|IMPL|TEST)_INT3_[\d]{10,}"
needs_id_required = True  # pylint: disable=C0103:invalid-name
needs_collapse_details = True  # pylint: disable=C0103:invalid-name
needs_include_needs = True  # pylint: disable=C0103:invalid-name
# smartquotes = False

needs_types = [
    dict(
        directive="req",
        title="Requirement",
        prefix="REQ_",
        color="#BFD8D2",
        style="node",
    ),
    dict(
        directive="impl",
        title="Implementation",
        prefix="IMPL_",
        color="#DF744A",
        style="node",
    ),
    dict(
        directive="test",
        title="Test Case",
        prefix="TEST_",
        color="#DCB239",
        style="node",
    ),
    # Kept for backwards compatibility
    # dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node"),
]

needs_extra_options = ['category', 'priority','safety-asil', 'verification-and-validation', 'submitted-by', 'modified-by','date-released', 'references']  # pylint: disable=C0301:line-too-long

# requirement -> implementation -> test
needs_extra_links = [
    {
        # requirement -> implementation
        "option": "implements",
        "incoming": "is implemented by",
        "outgoing": "implements",
        # "style": "#777777",
    },
    {
        # implementation -> test
        "option": "tests",
        "incoming": "is tested by",
        "outgoing": "tests",
        # "style": "#AA0000",
    },
]

needs_global_options = {
    # Apply dynamic style to all needs of "req" type
    "style": [
        ("[[status_based_style()]]", 'type=="req"'),
        ("blue_border, [[status_based_style()]]", 'type=="impl"'),
    ],
}


def need_dependencies_check(need, log):
    """Dynamic method for dynamic evaluation for "requirement" needs"""
    filters = {
        "req": ("implements_back", "Requirement %s has no implementation dependency"),
        "impl": ("tests_back", "Implementation %s has no test dependency"),
    }

    need_filter = filters.get(need.get("type"))
    if not need_filter:
        return
    if not need.get(need_filter[0]):
        log.warning(need_filter[1], need.get("id"))

def status_based_style(app, need, needs): # pylint: disable=W0613:unused-argument
    """
    Evaluates the status of a requirement, and returns corresponding style
    """
    return {
        "Draft": "red_bar",
        "In progress": "yellow_bar",
        "In review": "blue_bar",  
        "Rework": "orange_bar",  
        "Released": "green_bar"}.get(
        need["status"], ""
    )


def setup(app):
    # here we register our custom/dynamic function
    add_dynamic_function(app, status_based_style)
    add_warning(app, "need_dependencies_check", need_dependencies_check)
# -- Import setup -------------------------------------------------------------

from os import path

# -- Project information -----------------------------------------------------

repository = 'system-level'
project = 'System Level Documentation'
copyright = '2026, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "adi_doctools",
    "sphinxcontrib.mermaid",
    "myst_parser",
]

needs_extensions = {
    'adi_doctools': '0.4.33'
}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    'solutions/reference-designs/common/zcu102-zynqmp-setup.rst']

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

# -- Custom extensions configuration ------------------------------------------

mermaid_d3_zoom = True

# -- External docs configuration ----------------------------------------------

interref_repos = [
    'analog-attach',
    'doctools',
    'hdl',
    'pyadi-iio',
    'pyadi-dt',
    'pyadi-jif',
    'genalyzer/master',
    'kuiper',
    'scopy',
    'linux',
    'no-OS',
    'precision-converters-firmware',
    'PrecisionToolbox',
    'testbenches',
    'adi_ros2/humble/adi_meta',
]

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
html_favicon = path.join("sources", "icon.svg")
numfig = True
numfig_per_doc = True

numfig_format = {'figure': 'Figure %s',
                 'table': 'Table %s',
                 'code-block': 'Listing %s',
                 'section': 'Section %s'}

# -- Show TODOs ---------------------------------------------------------------

todo_include_todos = True

# -- Linkcheck ----------------------------------------------------------------

linkcheck_sitemaps = [
    "https://wiki.analog.com/doku.php?do=sitemap",
    "https://www.analog.com/media/en/en-pdf-sitemap.xml",
    "https://www.analog.com/media/en/en-pdp-sitemap.xml",
]
linkcheck_timeout = 5
linkcheck_request_headers = {
    "*": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Accept-Language": "en-US,en;q=0.5",
    },
}
linkcheck_ignore = [
    r'https://www.digikey.com/',
]

# -- Custom roles -------------------------------------------------------------

def reg_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom role for hardware registration links.
    Usage: :reg:`Register <EVAL-CN0511-RPIZ?&v=RevD>`
    Expands to: https://my.analog.com/en/app/registration/hardware/EVAL-CN0511-RPIZ?&v=RevD
    """
    from docutils import nodes
    from docutils.parsers.rst import roles

    # Parse the text to extract link text and target
    parts = text.split('<')
    if len(parts) == 2:
        link_text = parts[0].strip()
        target = parts[1].rstrip('>')
    else:
        # If no explicit link text, use the target as text
        link_text = text
        target = text

    # Build the full URL
    url = f'https://my.analog.com/en/app/registration/hardware/{target}'

    # Create a reference node
    node = nodes.reference(rawtext, link_text, refuri=url, **options)
    return [node], []

def setup(app):
    """Setup function to register custom roles."""
    app.add_role('reg', reg_role)

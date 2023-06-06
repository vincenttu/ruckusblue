# -- Project information -----------------------------------------------------

project = 'Ruckus Blue'
# copyright = '2023, Vincent Tu'
# author = 'Vincent Tu'
# release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_copybutton'
]

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'default'
html_logo = 'images/RB_square_canvas.png'
html_favicon = 'images/RB_ico_16.png'
# html_css_files = [
#     'css/custom.css'
# ]

# -- Shared files ------------------------------------------------------------

templates_path = ['_templates']
html_static_path = ['_static']

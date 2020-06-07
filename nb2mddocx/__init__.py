# file __init__.py
import os
import os.path
import re

from traitlets.config import Config
from nbconvert.exporters.markdown import MarkdownExporter

class MdDocxExporter(MarkdownExporter):
    """
    Converter to Microsoft word pandoc-friendly markdown
    """

    def _file_extension_default(self):
        """
        The new file extension is `.md`
        """
        return '.md'

    @property
    def default_config(self):
        c = Config({
            'ExtractOutputPreprocessor': {'enabled': True},
            'SVG2PDFPreprocessor': {'enabled': False},
            'NbConvertBase': {
                'display_data_priority': ['text/markdown',
                                          'image/svg+xml',
                                          'text/html',
                                          'text/latex',
                                          'image/png',
                                          'image/jpeg',
                                          'text/plain'
                                          ]
            },
        })
        super().default_config.merge(c)

        # Configure our tag removal
        c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
        c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
        c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)
        return c

    @property
    def template_path(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'mddocx'

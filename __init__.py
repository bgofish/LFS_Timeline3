# SPDX-License-Identifier: GPL-3.0-or-later
"""Training Render Plugin for LichtFeld Studio."""

# Try importing from the internal 'studio' module
try:
    import studio
except ImportError:
    # Fallback for different versions
    import lfs_studio as studio

from .panels.training_render import setup_data_binding
from .operators.start import StartEditorOperator

def register():
    setup_data_binding()
    studio.register_class(StartEditorOperator)
    # The panel registration happens here once defined in panels

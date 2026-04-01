# SPDX-License-Identifier: GPL-3.0-or-later
from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    """
    Called by LichtFeld Studio on plugin load.
    We use the provided context to access the registry.
    """
    setup_data_binding(context)
    
    # Register the classes to the Studio registry via context
    context.registry.register_class(KeyframeSpreadsheetPanel)
    context.registry.register_class(StartEditorOperator)
    
    print("Spreadsheet Editor Plugin Loaded Successfully")

def unregister(context):
    context.registry.unregister_class(KeyframeSpreadsheetPanel)
    context.registry.unregister_class(StartEditorOperator)

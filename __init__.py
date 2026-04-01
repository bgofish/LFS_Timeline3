# SPDX-License-Identifier: GPL-3.0-or-later
from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    setup_data_binding(context)
    
    # Explicitly register as a panel to create the sidebar tab
    context.registry.register_panel(KeyframeSpreadsheetPanel)
    context.registry.register_operator(StartEditorOperator)
    
    print("Spreadsheet Panel Registered")

def initialize(context):
    register(context)

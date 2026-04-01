# SPDX-License-Identifier: GPL-3.0-or-later
from .panels.training_render import setup_spreadsheet_data, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    # Use the new renamed function here
    setup_spreadsheet_data(context)
    
    context.registry.register_class(KeyframeSpreadsheetPanel)
    context.registry.register_class(StartEditorOperator)
    print("Spreadsheet Editor Registered Successfully")

def initialize(context):
    register(context)

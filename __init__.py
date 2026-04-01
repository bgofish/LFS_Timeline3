from .panels.training_render import setup_spreadsheet_data, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    setup_spreadsheet_data(context)
    
    # Check if the registry has the specific 'register_panel' method
    if hasattr(context.registry, 'register_panel'):
        context.registry.register_panel(KeyframeSpreadsheetPanel)
    else:
        context.registry.register_class(KeyframeSpreadsheetPanel)
        
    context.registry.register_class(StartEditorOperator)
    print("Spreadsheet Panel Registered")

def initialize(context):
    register(context)

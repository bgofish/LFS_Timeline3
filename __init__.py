# SPDX-License-Identifier: GPL-3.0-or-later
from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    """Entry point for most versions."""
    setup_data_binding(context)
    context.registry.register_class(KeyframeSpreadsheetPanel)
    context.registry.register_class(StartEditorOperator)
    print("Spreadsheet Plugin Registered via register()")

def initialize(context):
    """Entry point for v0.5+ versions."""
    register(context)
    print("Spreadsheet Plugin Initialized via initialize()")

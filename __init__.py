# SPDX-FileCopyrightText: 2025
# SPDX-License-Identifier: GPL-3.0-or-later

"""Training Render Plugin for LichtFeld Studio."""
import lfs
from .panels.training_render import setup_data_binding, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register():
    setup_data_binding()
    lfs.registry.register_class(KeyframeSpreadsheetPanel)
    lfs.registry.register_class(StartEditorOperator)
    lfs.log.info("Spreadsheet Editor Registered")

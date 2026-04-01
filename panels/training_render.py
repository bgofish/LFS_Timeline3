def setup_data_binding(context):
    """Initializes data bindings for the spreadsheet."""
    pass

class KeyframeSpreadsheetPanel:
    """The UI panel definition for the spreadsheet."""
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    # Ensure this .rml file exists in your plugin folder
    panel_path = "training_render.rml" 

    def draw(self, context):
        # UI is defined in the RML file
        pass
pass

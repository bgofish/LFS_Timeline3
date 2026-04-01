class StartEditorOperator:
    """The operator that triggers spreadsheet actions."""
    id = "lichtfeld.start_editor"
    label = "Start Spreadsheet Editor"

    def execute(self, context):
        # Access scene data through the context object
        print("Spreadsheet Operator Executed")
        return True

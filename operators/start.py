class StartEditorOperator:
    id = "lichtfeld.start_editor"
    label = "Start Spreadsheet Editor"

    def execute(self, context):
        # 'context' allows you to access the scene data
        print("Spreadsheet Operator Executed")
        return True

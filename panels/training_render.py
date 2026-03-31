import lfs # This is the actual module provided by LichtFeld Studio

class CameraEditorModel:
    def __init__(self):
        self.keyframes = []

    def load_from_studio(self):
        # Get the active path from the scene state
        active_path = lfs.state.camera_path
        if active_path:
            self.keyframes = [
                {"x": round(p.position.x, 3), 
                 "y": round(p.position.y, 3), 
                 "z": round(p.position.z, 3)} 
                for p in active_path.keyframes
            ]

    def apply_to_studio(self):
        active_path = lfs.state.camera_path
        if active_path:
            for i, kf in enumerate(self.keyframes):
                if i < len(active_path.keyframes):
                    active_path.keyframes[i].position.x = float(kf['x'])
                    active_path.keyframes[i].position.y = float(kf['y'])
                    active_path.keyframes[i].position.z = float(kf['z'])
            # Trigger a redraw of the viewport
            lfs.core.renderer.request_redraw()

def setup_data_binding(context):
    model = CameraEditorModel()
    # Create the binding between Python and RML
    view_model = context.create_datamodel("camera_editor")
    view_model.bind("keyframes", model.keyframes)
    
    @view_model.on_event("refresh_path")
    def on_refresh(event):
        model.load_from_studio()
        view_model.dirty_variable("keyframes") # Force UI to update
        
    @view_model.on_event("save_path")
    def on_save(event):
        model.apply_to_studio()

    @view_model.on_event("goto_keyframe")
    def on_goto(event):
        idx = int(event.parameters['index'])
        pos = model.keyframes[idx]
        lfs.state.camera.position = lfs.math.Vector3(pos['x'], pos['y'], pos['z'])

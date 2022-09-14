import omni.ui as ui
from .utils import get_selection
# from .combo_box_model import ComboBoxModel
from pxr import Usd

class JointWindow(ui.Window):
    
    def __init__(self, title: str, **kwargs) -> None:
        super().__init__(title, **kwargs)
        
        self._source_prim_model_a = ui.SimpleStringModel()
        self._source_prim_model_b = ui.SimpleStringModel()
        
        self.frame.set_build_fn(self._build_fn)
        
    def _on_get_selection_a(self):
        """Called when the user presses the "Get From Selection" button"""
        self._source_prim_model_a.as_string = ", ".join(get_selection())
        
    def _on_get_selection_b(self):
        """Called when the user presses the "Get From Selection" button"""
        self._source_prim_model_b.as_string = ", ".join(get_selection())
            

    def _build_window(self):
        with self.frame:
            with ui.VStack():
                with ui.CollapsableFrame("Source"):
                    with ui.VStack(height=20, spacing=4):
                        with ui.HStack():
                            ui.Label("Prim A")
                            ui.StringField(model = self._source_prim_model_a)
                            ui.Button("S", clicked_fn=self._on_get_selection_a)
                        
                        ui.Spacer()
                        
                        with ui.HStack():
                            ui.Label("Prim B")
                            ui.StringField(model = self._source_prim_model_b)
                            ui.Button("S", clicked_fn=self._on_get_selection_b)
                        
                with ui.CollapsableFrame("Joints"):
                    with ui.VStack():
                        ui.Label
                        ui.ComboBox(1,"Revolute", "Blah2", "Blah3")
                        
                        
                        joint_type='Revolute',
                        
                        import omni.kit.commands
                    

                def on_click():
                    print("clicked!")
                    
                ui.Button("Create Joint", clicked_fn=lambda: on_click())
                         
    def _build_fn(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=10):
                self._build_window()
                
    def destroy(self) -> None:
        return super().destroy()                       
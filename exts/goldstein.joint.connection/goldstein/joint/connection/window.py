import omni.ui as ui
from .utils import get_selection
import omni.kit.commands
import omni.usd


JOINTS = ("D6", "Revolute", "Fixed", "Spherical", "Prismatic", "Distance", "Gear", "Rack and Pinion")

class JointWindow(ui.Window):
    
    def __init__(self, title: str, **kwargs) -> None:
        super().__init__(title, **kwargs)
        
        self._source_prim_model_a = ui.SimpleStringModel()
        self._source_prim_model_b = ui.SimpleStringModel()
        self._stage = omni.usd.get_context().get_stage()
        self.frame.set_build_fn(self._build_fn)
        self.combo_model = None
        self.current_joint = None
        
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
                        self.combo_model = ui.ComboBox(0,*JOINTS).model
                        
                        def combo_changed(item_model, item):
                            value_model = item_model.get_item_value_model(item)
                            self.current_joint = JOINTS[value_model.as_int]
                            # self.current_index = value_model.as_int
                        self._combo_changed_sub = self.combo_model.subscribe_item_changed_fn(combo_changed)                    
                                

                def on_click():
                    print("clicked!")
                   
                    omni.kit.commands.execute('CreateJointCommand',
                        stage = self._stage,                      
                        joint_type=self.current_joint,
                        from_prim = self._stage.GetPrimAtPath(self._source_prim_model_a.as_string),
                        to_prim = self._stage.GetPrimAtPath(self._source_prim_model_b.as_string))

                ui.Button("Create Joint", clicked_fn=lambda: on_click())
                         
    def _build_fn(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=10):
                self._build_window()
                
    def destroy(self) -> None:
        self._combo_changed_sub = None
        return super().destroy()                       
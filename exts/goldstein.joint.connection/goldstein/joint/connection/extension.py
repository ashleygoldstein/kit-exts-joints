import omni.ext
import omni.ui as ui
from .window import JointWindow

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class JointCreationExt(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[Joint.Creation.Ext] startup")

        self._window = JointWindow("Joint Creation", width=300, height=300)


    def on_shutdown(self):
        self._window.destroy()
        print("[Joint.Creation.Ext] shutdown")

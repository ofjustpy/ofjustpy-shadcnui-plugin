import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *


oj.set_style("un")

with writer_ctx:
    with SCUI.Alert.Root() as alert_box:
        with SCUI.Alert.Title():
            with oj.PD.Prose(text="Heads up!"):
                pass
            pass

        with SCUI.Alert.Description():
            with oj.PD.Prose(text="You can add components to your app using the cli."):
                pass

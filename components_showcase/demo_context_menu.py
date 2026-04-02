import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")


with writer_ctx:
    with SCUI.ContextMenu.Root() as context_menu_box:
        with SCUI.ContextMenu.Trigger():
            with oj.PD.Prose(text="Right click"):
                pass
        with SCUI.ContextMenu.Content():
            with SCUI.ContextMenu.Item():
                with oj.PD.Prose(text="Profile"):
                    pass
            with SCUI.ContextMenu.Item():
                with oj.PD.Prose(text="Billing"):
                    pass
            with SCUI.ContextMenu.Item():
                with oj.PD.Prose(text="Team"):
                    pass
            with SCUI.ContextMenu.Item():
                with oj.PD.Prose(text="Subscription"):
                    pass

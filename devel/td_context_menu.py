import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")


with writer_ctx:
    with SCUI.ContextMenu.Root() as context_menu_root:
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



app = oj.load_app()
adiv = oj.PC.Div(childs=[context_menu_root])

wp_endpoint = oj.create_endpoint(key="context_menu",
                                 childs = [
                                     adiv
                                           ],
                                 title="ContextMenu",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )

oj.add_jproute("/", wp_endpoint)
                
                

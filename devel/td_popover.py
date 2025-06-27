import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")


# Python example for Popover
with writer_ctx:
    with SCUI.Popover.Root() as popover_root:
        with SCUI.Popover.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        with SCUI.Popover.Content():
            with oj.PD.Prose(text="Place content for the popover here."):
                pass
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Popover",
                                 childs = [
                                     popover_root
                                           ],
                                 
                                 title="Popover",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    

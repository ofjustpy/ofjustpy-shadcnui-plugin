#TODO 
import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

aspan = kv.MC.Span(key="aspan", text="hello")
with MuCtx:
    # Main outer box layout
    with kv.HM.Div(classes="p-8 flex justify-center") as popover_box:

        # Card Root Definition
        with kv.AD.SCUI.divmutable.Popover.Root(key="xyz", classes="-my-4 w-full max-w-sm"):
            
            with kv.AD.SCUI.divmutable.Popover.Trigger(key="rtz"):
                with ChildComp(child=aspan):
                    pass
                pass 
            # Card Content
            with kv.AD.SCUI.divactive.Popover.Content():
                # Form structure containing fields
                with kv.PD.PlainText(text="Open"):
                    pass
                with kv.AD.Button(text="submit", key="abtn"):
                    pass 
                with kv.PD.Prose(text="popover content"):
                    pass
                pass
            

#print(popover_box.components)
wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[popover_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

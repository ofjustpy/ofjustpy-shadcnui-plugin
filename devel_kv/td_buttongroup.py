import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Outer wrapping container for layout placement
    with kv.PD.Div(classes="p-8 flex justify-center") as buttongroup1_box:

        # ButtonGroup Root Container
        with kv.AD.SCUI.divactive.ButtonGroup.Root(key="btn_group_demo"):
            
            # Button 1
            with SCUI.divactive.Button.Root(key="bg_btn_1"):
                with kv.PD.Prose(text="Button 1"):
                    pass
            
            # Button 2
            with SCUI.divactive.Button.Root(key="bg_btn_2"):
                with kv.PD.Prose(text="Button 2"):
                    pass


with MuCtx:
    # Outer wrapping container for layout placement
    with kv.PD.Div(classes="p-8 flex justify-center") as buttongroup2_box:

        # ButtonGroup Root Container
        with kv.AD.SCUI.divactive.ButtonGroup.Root(key="btn_group_actions"):
            
            # Copy Button
            with SCUI.divactive.Button.Root(variant="secondary", size="sm", key="bg_copy_btn"):
                with kv.PD.Prose(text="Copy"):
                    pass
            
            # Button Group Separator Element
            with SCUI.divactive.ButtonGroup.Separator():
                pass
            
            # Paste Button
            with SCUI.divactive.Button.Root(variant="secondary", size="sm", key="bg_paste_btn"):
                with kv.PD.Prose(text="Paste"):
                    pass
                
wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[buttongroup1_box, buttongroup2_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

#TODO 
import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

aspan = kv.PC.Span(text="hello")
with MuCtx:
    # Main outer box layout
    with kv.PD.Div(classes="p-8 flex justify-center") as popover_box:
        with ChildComp(child=aspan):
            pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[popover_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

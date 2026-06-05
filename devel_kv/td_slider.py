import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Outer layout container box
    with kv.PD.Div(classes="p-16 flex flex-col gap-4 w-full justify-center items-center") as slider_box:

        # Slider component using MuCtx block syntax
        with SCUI.divactive.Slider.Root(
            classes="w-full",
            extra_classes="max-w-[70%]",
            value=[50],  # Shadcn sliders typically expect an array/list for values
            step=1,
            max_=100,
            key="volume_slider"
        ):
            pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[slider_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)
    

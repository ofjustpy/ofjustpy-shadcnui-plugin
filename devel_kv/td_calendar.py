import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Outer layout box to anchor presentation structure
    with kv.PD.Div(classes="p-16 flex justify-center items-center w-full") as calendar_box:

        # Calendar component instantiated with mandatory context block
        with SCUI.divactive.Calendar.Root(
            classes="rounded-md border shadow-sm",
            captionLayout="dropdown",
            key="appointment_calendar"
        ):
            pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[calendar_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

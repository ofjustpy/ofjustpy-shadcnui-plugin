import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Outer wrapping container for layout placement
    with kv.PD.Div(classes="p-8 max-w-sm grid gap-2") as label_box:

        # Label Root component utilizing key instead of 'for' attribute mapping
        with SCUI.divactive.Label.Root(key="email_label"):
            with kv.PD.Prose(text="Your email address"):
                pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[label_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

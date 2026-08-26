import kavya as kv
from shadcnui_components import alert_dialog
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Main column wrapper
    with kv.PD.Div(classes="flex items-start gap-3") as debug_box:
        with SCUI.divactive.Badge.Root(key="badge_default"):
            with kv.PD.Span(text="Badge"):
                pass
                

                    

kv.set_style("un")

wp_endpoint = kv.create_endpoint(key="webpage_mutable_csr",
                                 childs =[debug_box],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 skeleton_data_theme = "mint",
                                 svelte_bundle_dir="csr",
                                 rendering_type="CSR"
                                 )
app = kv.load_app()
kv.add_route("/", wp_endpoint)



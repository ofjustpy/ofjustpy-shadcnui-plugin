import kavya as kv
from shadcnui_components import alert_dialog
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *



kv.set_style("un")
alert_dialog =  kv.AD.SCUI.divactive.AlertDialog.Root(key="alert_dialog_1")
trigger = kv.AD.SCUI.divactive.AlertDialog.Trigger(variant="outline")
#kv.AD.SCUI.divactive.AlertDialog(key="alert_dialog_1")

wp_endpoint = kv.create_endpoint(key="webpage_mutable_csr",
                                 childs =[alert_dialog],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 skeleton_data_theme = "mint",
                                 svelte_bundle_dir="csr",
                                 rendering_type="CSR"
                                 )
app = kv.load_app()
kv.add_route("/", wp_endpoint)



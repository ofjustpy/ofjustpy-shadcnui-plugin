import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *
import csr_components as CSRC

icon_color = "success-800"
# arrow_up_icon = CSRC.LucideIcon(key="li_1",
#                        label="arrow-up",
#                         width=6,
#                         stroke_color=icon_color
#                         )

with MuCtx:
    with kv.PD.Div(classes="flex flex-wrap items-center gap-2 md:flex-row") as button_box:
        
        # 1. Standard Outline Button
        with SCUI.divactive.Button.Root(variant="outline", key="btn_standard"):
            with kv.PD.Prose(text="Button"):
                pass

        # 2. Icon-Only Outline Button
        with SCUI.divactive.Button.Root(variant="outline", size="icon", aria_label="Submit", key="btn_icon"):
            # Rendering the ArrowUpIcon using the CSRC.LucideIcon format
            with CSRC.LucideIcon(key="li_1",
                       label="eye-off",
                        width=6,
                        stroke_color=icon_color
                        ):
                pass
            # with ChildComp(child = arrow_up_icon):
            #     pass

wp_endpoint = kv.create_endpoint(key="webpage_mutable_csr",
                                 childs =[button_box],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 skeleton_data_theme = "mint",
                                 svelte_bundle_dir="csr",
                                 rendering_type="CSR"
                                 )
app = kv.load_app()
kv.add_route("/", wp_endpoint)                    
            

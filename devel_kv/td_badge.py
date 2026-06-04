import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

# Assuming CSRC is imported for LucideIcon lookup
import csr_components as CSRC

icon_color = "currentColor"

with MuCtx:
    # Outer wrapping container
    with kv.PD.Div(classes="flex flex-col items-center gap-2") as badge_box:
        
        # --- First Row: Standard Variants ---
        with kv.PD.Div(classes="flex w-full flex-wrap gap-2"):
            
            with SCUI.divactive.Badge.Root(key="badge_default"):
                with kv.PD.Prose(text="Badge"):
                    pass
                    
            with SCUI.divactive.Badge.Root(variant="secondary", key="badge_secondary"):
                with kv.PD.Prose(text="Secondary"):
                    pass
                    
            with SCUI.divactive.Badge.Root(variant="destructive", key="badge_destructive"):
                with kv.PD.Prose(text="Destructive"):
                    pass
                    
            with SCUI.divactive.Badge.Root(variant="outline", key="badge_outline"):
                with kv.PD.Prose(text="Outline"):
                    pass

        # --- Second Row: Custom Layouts, Icons, and Counters ---
        with kv.PD.Div(classes="flex w-full flex-wrap gap-2"):
            
            # Verified Badge with BadgeCheckIcon
            with SCUI.divactive.Badge.Root(variant="secondary",
                                           classes="bg-blue-500 text-white dark:bg-blue-600",
                                           key="badge_verified"):
                with CSRC.LucideIcon(
                    key="li_badge_check",
                    label="badge-check",
                    width=4,
                    stroke_color=icon_color
                ):
                    pass
                

            # Numeric Badge Counter (Standard Variant)
            with SCUI.divactive.Badge.Root(classes="h-5 min-w-5 rounded-full px-1 font-mono ", extra_classes="tabular-nums",
                                           key="badge_count_8"):
                with kv.PD.Prose(text="8"):
                    pass

            # Numeric Badge Counter (Destructive Variant)
            with SCUI.divactive.Badge.Root(variant="destructive", classes="h-5 min-w-5 rounded-full px-1 font-mono ", extra_classes="tabular-nums", key="badge_count_99"):
                with kv.PD.Prose(text="99"):
                    pass

            # Numeric Badge Counter (Outline Variant)
            with SCUI.divactive.Badge.Root(variant="outline", classes="h-5 min-w-5 rounded-full px-1 font-mono", extra_classes="tabular-nums",  key="badge_count_20"):
                with kv.PD.Prose(text="20+"):
                    pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[badge_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

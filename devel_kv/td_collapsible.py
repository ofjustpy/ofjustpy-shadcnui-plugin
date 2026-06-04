import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

import csr_components as CSRC

icon_color = "currentColor"

with MuCtx:
    # Outer layout box
    with kv.PD.Div(classes="p-16 flex justify-center items-center w-full") as collapsible_box:

        # Collapsible Root Container
        with kv.AD.SCUI.divactive.Collapsible.Root(extra_classes="w-[350px] space-y-2", key="collapsible_demo"):
            
            # Header Row Wrapper
            with kv.PD.Div(classes="flex items-center justify-between space-x-4 px-4"):
                
                # Title Text
                with kv.PD.H4(classes="text-sm font-semibold"):
                    with kv.PD.Prose(text="@huntabyte starred 3 repositories"):
                        pass
                
                # Collapsible Trigger (styled with standard Button variant classes)
                with SCUI.divactive.Collapsible.Trigger(
                    classes="w-9 p-0  flex items-center justify-center rounded-sm",
                    extra_classes="hover:bg-slate-100",
                    key="col_trigger"
                ):
                    # Lucide Chevron Up/Down Icon
                    with CSRC.LucideIcon(
                        key="li_chevrons_up_down",
                        label="chevrons-up-down",
                        width=4,
                        stroke_color=icon_color
                    ):
                        pass
                    
                    # Screen reader context
                    with kv.PD.Span(classes="sr-only"):
                        with kv.PD.Prose(text="Toggle"):
                            pass

            # Static Always-Visible Repository Item
            with kv.PD.Div(classes="rounded-md border px-4 py-3 font-mono text-sm"):
                with kv.PD.Prose(text="@huntabyte/bits-ui"):
                    pass

            # Collapsible Content Area (Hidden by default until triggered)
            with SCUI.divactive.Collapsible.Content(classes="space-y-2"):
                
                # Collapsible Item 1
                with kv.PD.Div(classes="rounded-md border px-4 py-3 font-mono text-sm"):
                    with kv.PD.Prose(text="@melt-ui/melt-ui"):
                        pass
                
                # Collapsible Item 2
                with kv.PD.Div(classes="rounded-md border px-4 py-3 font-mono text-sm"):
                    with kv.PD.Prose(text="@sveltejs/svelte"):
                        pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[collapsible_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

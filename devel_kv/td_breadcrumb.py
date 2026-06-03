#TODO: 
import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    with kv.PD.Div(classes="p-8") as breadcrumb_box:

        # Breadcrumb Root Definition
        with kv.AD.SCUI.divactive.Breadcrumb.Root(key="breadcrumb_demo"):
            with SCUI.divactive.Breadcrumb.List():
                
                # 1. Home Link
                with SCUI.divactive.Breadcrumb.Item():
                    with SCUI.divactive.Breadcrumb.Link(href="/"):
                        with kv.PD.Prose(text="Home"):
                            pass
                
                with SCUI.divactive.Breadcrumb.Separator():
                    pass

                # 2. Dropdown / Ellipsis Menu Item
                with SCUI.divactive.Breadcrumb.Item():
                    with SCUI.divactive.DropdownMenu.Root(key="breadcrumb_dropdown"):
                        
                        # Trigger containing Ellipsis icon and screen-reader text
                        with SCUI.divactive.DropdownMenu.Trigger(classes="flex items-center gap-1"):
                            # Representing the size-4 Ellipsis icon via a custom component tag or a generic layout
                            with SCUI.divactive.Breadcrumb.Ellipsis(classes="size-4"):
                                pass
                            with kv.PD.Span(classes="sr-only"):
                                with kv.PD.Prose(text="Toggle menu"):
                                    pass
                        
                        # Dropdown Sub-menu items
                        with SCUI.divactive.DropdownMenu.Content(align="start"):
                            with SCUI.divactive.DropdownMenu.Item():
                                with kv.PD.Prose(text="Documentation"):
                                    pass
                            with SCUI.divactive.DropdownMenu.Item():
                                with kv.PD.Prose(text="Themes"):
                                    pass
                            with SCUI.divactive.DropdownMenu.Item():
                                with kv.PD.Prose(text="GitHub"):
                                    pass

                with SCUI.divactive.Breadcrumb.Separator():
                    pass

                # 3. Components Link
                with SCUI.divactive.Breadcrumb.Item():
                    with SCUI.divactive.Breadcrumb.Link(href="/docs/components"):
                        with kv.PD.Prose(text="Components"):
                            pass

                with SCUI.divactive.Breadcrumb.Separator():
                    pass

                # 4. Current Page (Active/Static Text)
                with SCUI.divactive.Breadcrumb.Item():
                    with SCUI.divactive.Breadcrumb.Page():
                        with kv.PD.Prose(text="Breadcrumb"):
                            pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[breadcrumb_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

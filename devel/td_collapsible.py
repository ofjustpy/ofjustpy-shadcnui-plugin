import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")

# with writer_ctx:
#     with SCUI.Collapsible.Root() as collapsible_box:
#         with SCUI.Collapsible.Trigger():
#             with oj.PD.Prose(text="Can I use this in my project?"):
#                 pass
        
#         with SCUI.Collapsible.Content():
#             with oj.PD.Prose(text="Yes. Free to use for personal and commercial projects. No attribution required."):
#                 pass
            
# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.Collapsible.Root(extra_classes="w-[350px] space-y-2") as collapsible_box:
        with oj.PD.Div(classes="flex items-center justify-between space-x-4 px-4"):
            with oj.PD.H4(classes="text-sm font-semibold"):
                with oj.PD.Prose(text="@huntabyte starred 3 repositories"):
                    pass
            with SCUI.Collapsible.Trigger(classes="w-9 p-0"): # Assuming buttonVariants translates to these classes
                # Representing ChevronsUpDownIcon as text for now
                with oj.PD.Prose(text="[ChevronsUpDownIcon]"):
                    pass
                with oj.PD.Span(classes="sr-only"):
                    with oj.PD.Prose(text="Toggle"):
                        pass
        with oj.PD.Div(classes="rounded-md border px-4 py-3 font-mono text-sm"):
            with oj.PD.Prose(text="@huntabyte/bits-ui"):
                pass
        with SCUI.Collapsible.Content(classes="space-y-2"):
            with oj.PD.Div(classes="rounded-md border px-4 py-3 font-mono text-sm"):
                with oj.PD.Prose(text="@melt-ui/melt-ui"):
                    pass
            with oj.PD.Div(classes="rounded-md border px-4 py-3 font-mono text-sm"):
                with oj.PD.Prose(text="@sveltejs/svelte"):
                    pass

app = oj.load_app()
adiv = oj.PC.Div(childs=[collapsible_box])

wp_endpoint = oj.create_endpoint(key="collapsible",
                                 childs = [
                                     adiv
                                           ],
                                 title="Collapsible",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )

oj.add_jproute("/", wp_endpoint)
                




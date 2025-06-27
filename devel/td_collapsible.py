import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")

with writer_ctx:
    with SCUI.Collapsible.Root() as collapsible_box:
        with SCUI.Collapsible.Trigger():
            with oj.PD.Prose(text="Can I use this in my project?"):
                pass
        
        with SCUI.Collapsible.Content():
            with oj.PD.Prose(text="Yes. Free to use for personal and commercial projects. No attribution required."):
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
                




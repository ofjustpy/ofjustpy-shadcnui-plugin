


import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

with writer_ctx:
    with SCUI.HoverCard.Root() as hovercard_box:
        
        with SCUI.HoverCard.Trigger():
            with oj.PD.Prose(text="Hover"):
                pass
        
        with SCUI.HoverCard.Content():
            with oj.PD.Prose(text="SvelteKit - Web development, streamlined"):
                pass

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="HoverCard",
                                 childs = [
                                     hovercard_box
                                           ],
                                 
                                 title="HoverCard",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                                

import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")

with writer_ctx:
    with SCUI.Avatar.Root() as avatar_box:
        with SCUI.Avatar.Image(src="https://avatars.githubusercontent.com/u/124599?v=4", alt="@shadcn"):
            pass
        with SCUI.Avatar.Fallback(text="CN"):
            pass
        
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     avatar_box
                                           ],
                                 
                                 title="Avatar",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    

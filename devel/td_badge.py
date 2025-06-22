import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")

with writer_ctx:
    with SCUI.Badge(variant="outline", text="Badge") as badge_box:
        pass
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="alert",
                                 childs = [
                                     badge_box
                                           ],
                                 
                                 title="Badge",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)


                



import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")
with writer_ctx:
    with oj.PD.Div(classes="flex items-center space-x-4") as skeleton_box:
        
        with SCUI.Skeleton(classes="h-12 w-12 rounded-full"):
            pass
        
        with oj.PD.Div(classes="space-y-2"):
            
            with SCUI.Skeleton(extra_classes="h-4 w-[400px]"):
                pass
            
            with SCUI.Skeleton(extra_classes="h-4 w-[400px]"):
                pass

            
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Skeleton",
                                 childs = [
                                     skeleton_box
                                           ],
                                 
                                 title="Skeleton",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                     

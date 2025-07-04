import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.Progress(value=33, max_=100, extra_classes="w-[60%]") as progress_box:
        
        pass



                    
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Progress",
                                 childs = [
                                     progress_box
                                           ],
                                 
                                 title="Progress",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    

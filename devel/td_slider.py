

import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.Slider(extra_classes="w-[400px]", value="[50]", max_=100, step=1) as slider_box:
        pass
        

            
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Slider",
                                 childs = [
                                     slider_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                     

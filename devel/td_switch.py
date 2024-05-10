

import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.Switch(classes="w-[400px]", checked=True) as switch_box:
        pass
        

            
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     switch_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                     

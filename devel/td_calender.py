import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

def valuechange_eh(dbref, msg, to_ms):
    print("yey we are at valuechange: ", msg.value)
    pass

# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.Calendar(key="cal1", on_valuechange=valuechange_eh) as calendar_box:
        pass

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Calendar",
                                 childs = [
                                     calendar_box
                                           ],
                                 
                                 title="Calendar",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

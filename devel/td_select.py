import ofjustpy as oj
import shadcnui_components as SCUI
from shadcnui_components.dsl import macros, writer_ctx
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

oj.set_style("un")

with writer_ctx:
    with SCUI.Select() as select_box:
        with SCUI.Select.Trigger(classes="w-[180px]"):
            
            with SCUI.Select.Value(placeholder="Theme"):
                pass
        
        with SCUI.Select.Content():
            
            with SCUI.Select.Item(value="light"):
                with oj.PD.Prose(text="Light"):
                    pass
            
            with SCUI.Select.Item(value="dark"):
                with oj.PD.Prose(text="Dark"):
                    pass
            
            with SCUI.Select.Item(value="system"):
                with oj.PD.Prose(text="System"):
                    pass
                


             

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="select",
                                 childs = [
                                     select_box
                                           ],
                                 
                                 title="Select"
                                 )
oj.add_jproute("/", wp_endpoint)
                




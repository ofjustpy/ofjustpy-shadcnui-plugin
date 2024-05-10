import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")
with writer_ctx:
    with SCUI.RadioGroup(value="comfortable") as radiogroup_box:
        
        with oj.PD.Div(class_="flex items-center space-x-2"):
            
            with SCUI.RadioGroup.Item(value="default", id="r1"):
                pass
            
            with oj.PD.Label(for_="r1"):
                with oj.PD.Prose(text="Default"):
                    pass
        
        with oj.PD.Div(class_="flex items-center space-x-2"):
            
            with SCUI.RadioGroup.Item(value="comfortable", id="r2"):
                pass
            
            with oj.PD.Label(for_="r2"):
                with oj.PD.Prose(text="Comfortable"):
                    pass
        
        with oj.PD.Div(class_="flex items-center space-x-2"):
            
            with SCUI.RadioGroup.Item(value="compact", id="r3"):
                pass
            
            with oj.PD.Label(for_="r3"):
                with oj.PD.Prose(text="Compact"):
                    pass
        
        with SCUI.RadioGroup.Input(name="spacing"):
            pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     radiogroup_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                            

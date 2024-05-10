import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.Tabs(value="password", class_="w-[400px]") as tabs_box:
        
        with SCUI.Tabs.List():
            
            with SCUI.Tabs.Trigger(value="account"):
                with oj.PD.Prose(text="Account"):
                    pass
            
            with SCUI.Tabs.Trigger(value="password"):
                with oj.PD.Prose(text="Password"):
                    pass
        
        with SCUI.Tabs.Content(value="account"):
            with oj.PD.Prose(text="Make changes to your account here."):
                pass
        
        with SCUI.Tabs.Content(value="password"):
            with oj.PD.Prose(text="Change your password here."):
                pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     tabs_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                                                    

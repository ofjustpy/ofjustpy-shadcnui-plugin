import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

with writer_ctx:
    with SCUI.Sheet() as sheet_box:
        
        with SCUI.Sheet.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        
        with SCUI.Sheet.Content():
            
            with SCUI.Sheet.Header():
                
                with SCUI.Sheet.Title():
                    with oj.PD.Prose(text="Are you sure absolutely sure?"):
                        pass
                
                with SCUI.Sheet.Description():
                    with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
                        pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     sheet_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                                        

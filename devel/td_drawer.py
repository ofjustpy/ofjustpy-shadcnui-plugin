import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")
with writer_ctx:
    with SCUI.Drawer.Root() as drawer_box:
        
        with SCUI.Drawer.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        
        with SCUI.Drawer.Content():
            
            with SCUI.Drawer.Header():
                
                with SCUI.Drawer.Title():
                    with oj.PD.Prose(text="Are you absolutely sure?"):
                        pass
                
                with SCUI.Drawer.Description():
                    with oj.PD.Prose(text="This action cannot be undone."):
                        pass
            
            with SCUI.Drawer.Footer():
                
                with SCUI.Button(key="abtn"):
                    with oj.PD.Prose(text="Submit"):
                        pass
                
                with SCUI.Drawer.Close():
                    with oj.PD.Prose(text="Cancel"):
                        pass


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Drawer",
                                 childs = [
                                     drawer_box
                                           ],
                                 
                                 title="Drawer",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

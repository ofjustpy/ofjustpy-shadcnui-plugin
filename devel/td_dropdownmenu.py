import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")
with writer_ctx:
    with SCUI.DropdownMenu.Root() as dropdown_menu_box:
        
        with SCUI.DropdownMenu.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        
        with SCUI.DropdownMenu.Content():
            
            with SCUI.DropdownMenu.Group():
                
                with SCUI.DropdownMenu.Label():
                    with oj.PD.Prose(text="My Account"):
                        pass
                
                with SCUI.DropdownMenu.Separator():
                    pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Profile"):
                        pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Billing"):
                        pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Team"):
                        pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Subscription"):
                        pass

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="DropdownMenu",
                                 childs = [
                                     dropdown_menu_box
                                           ],
                                 
                                 title="DropdownMenu",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

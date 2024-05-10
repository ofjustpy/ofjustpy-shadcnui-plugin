
import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

with writer_ctx:
    with SCUI.Menubar() as menubar_box:
        
        with SCUI.Menubar.Menu():
            
            with SCUI.Menubar.Trigger():
                with oj.PD.Prose(text="File"):
                    pass
            
            with SCUI.Menubar.Content():
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="New Tab"):
                        pass
                    with SCUI.Menubar.Shortcut():
                        with oj.PD.Prose(text="⌘T"):
                            pass
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="New Window"):
                        pass
                
                with SCUI.Menubar.Separator():
                    pass
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="Share"):
                        pass
                
                with SCUI.Menubar.Separator():
                    pass
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="Print"):
                        pass
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     menubar_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

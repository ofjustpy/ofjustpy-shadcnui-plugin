import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")


with writer_ctx:
    with SCUI.Dialog.Root() as dialog_box:
        
        with SCUI.Dialog.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        
        with SCUI.Dialog.Content():
            
            with SCUI.Dialog.Header():
                
                with SCUI.Dialog.Title():
                    with oj.PD.Prose(text="Are you absolutely sure?"):
                        pass
                
                with SCUI.Dialog.Description():
                    with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
                        pass


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Dialog",
                                 childs = [
                                     dialog_box
                                           ],
                                 
                                 title="Dialog",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    

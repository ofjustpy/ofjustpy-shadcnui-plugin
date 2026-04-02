import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *


oj.set_style("un")

with writer_ctx:
    with SCUI.AlertDialog.Root() as alertdialog_box:
        
        with SCUI.AlertDialog.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        
        with SCUI.AlertDialog.Content():
            
            with SCUI.AlertDialog.Header():
                
                with SCUI.AlertDialog.Title():
                    with oj.PD.Prose(text="Are you absolutely sure?"):
                        pass
                
                with SCUI.AlertDialog.Description():
                    with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
                        pass
            
            with SCUI.AlertDialog.Footer():
                
                with SCUI.AlertDialog.Cancel():
                    with oj.PD.Prose(text="Cancel"):
                        pass
                
                with SCUI.AlertDialog.Action():
                    with oj.PD.Prose(text="Continue"):
                        pass

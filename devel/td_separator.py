import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")


with writer_ctx:
    with oj.PD.Div() as separator_box:
        with oj.PD.Div(classes="space-y-1"):
            with oj.PD.H4(classes="text-sm font-medium leading-none"):
                with oj.PD.Prose(text="Radix Primitives"):
                    pass
            
            with oj.PD.P(classes="text-sm", extra_classes="text-muted-foreground"):
                with oj.PD.Prose(text="An open-source UI component library."):
                    pass
        
        with SCUI.Separator(classes="my-4"):
            pass
        
        with oj.PD.Div(classes="flex h-5 items-center space-x-4 text-sm"):
            
            with oj.PD.Div():
                with oj.PD.Prose(text="Blog"):
                    pass
            
            with SCUI.Separator(orientation="vertical"):
                pass
            
            with oj.PD.Div():
                with oj.PD.Prose(text="Docs"):
                    pass
            
            with SCUI.Separator(orientation="vertical"):
                pass
            
            with oj.PD.Div():
                with oj.PD.Prose(text="Source"):
                    pass
        
        pass

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     separator_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                    
                                    

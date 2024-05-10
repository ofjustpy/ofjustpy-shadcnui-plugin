import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.Resizable(direction="horizontal", extra_classes="min-h-[200px] max-w-md rounded-lg border") as resizable_box:
        with SCUI.Resizable.Pane(defaultSize=25):
            with oj.PD.Div(classes="flex h-full items-center justify-center p-6"):
                with oj.PD.Span(classes="font-semibold"):
                    with oj.PD.Prose(text="Sidebar"):
                        pass

        with SCUI.Resizable.Handle(withHandle=True):
            pass

        with SCUI.Resizable.Pane(defaultSize=75):
            with oj.PD.Div(classes="flex h-full items-center justify-center p-6"):
                with oj.PD.Span(classes="font-semibold"):
                    with oj.PD.Prose(text="Content"):
                        pass


        pass
    
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     resizable_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

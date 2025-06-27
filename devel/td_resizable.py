import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")


with writer_ctx:
    with SCUI.Resizable.PaneGroup(direction="horizontal",
                                  extra_classes="max-w-md rounded-lg border") as resizable_box:
        with SCUI.Resizable.Pane(defaultSize=50):
            with oj.PD.Div(extra_classes="flex h-[200px] items-center justify-center p-6"):
                with oj.PD.Span(extra_classes="font-semibold", text="One"):
                    pass
        with SCUI.Resizable.Handle():
            pass
        with SCUI.Resizable.Pane(defaultSize=50):
            with SCUI.Resizable.PaneGroup(direction="vertical"):
                with SCUI.Resizable.Pane(defaultSize=25):
                    with oj.PD.Div(extra_classes="flex h-full items-center justify-center p-6"):
                        with oj.PD.Span(extra_classes="font-semibold", text="Two"):
                            pass
                with SCUI.Resizable.Handle():
                    pass
                with SCUI.Resizable.Pane(defaultSize=75):
                    with oj.PD.Div(classes="flex h-full items-center justify-center p-6"):
                        with oj.PD.Span(extra_classes="font-semibold", text="Three"):
                            pass
                        

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Resizable",
                                 childs = [
                                     resizable_box
                                           ],
                                 
                                 title="Resizable",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

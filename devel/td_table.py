import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

with writer_ctx:
    with SCUI.Table.Root() as table_box:
        
        with SCUI.Table.Caption():
            with oj.PD.Prose(text="A list of your recent invoices."):
                pass
        
        with SCUI.Table.Header():
            
            with SCUI.Table.Row():
                
                with SCUI.Table.Head(extra_classes="w-[100px]"):
                    with oj.PD.Prose(text="Invoice"):
                        pass
                
                with SCUI.Table.Head():
                    with oj.PD.Prose(text="Status"):
                        pass
                
                with SCUI.Table.Head():
                    with oj.PD.Prose(text="Method"):
                        pass
                
                with SCUI.Table.Head(classes="text-right"):
                    with oj.PD.Prose(text="Amount"):
                        pass
        
        with SCUI.Table.Body():
            
            with SCUI.Table.Row():
                
                with SCUI.Table.Cell(classes="font-medium", extra_classes="w-[100px]"):
                    with oj.PD.Prose(text="INV001"):
                        pass
                
                with SCUI.Table.Cell():
                    with oj.PD.Prose(text="Paid"):
                        pass
                
                with SCUI.Table.Cell():
                    with oj.PD.Prose(text="Credit Card"):
                        pass
                
                with SCUI.Table.Cell(class_="text-right"):
                    with oj.PD.Prose(text="$250.00"):
                        pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Table",
                                 childs = [
                                     table_box
                                           ],
                                 
                                 title="Table",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                                        

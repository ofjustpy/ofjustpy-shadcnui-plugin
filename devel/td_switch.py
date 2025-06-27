

import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

# Python equivalent for the HTML snippet
with writer_ctx:
    with oj.PD.Div(classes="flex items-center space-x-2") as  switch_box:
        with SCUI.Switch(id="airplane-mode"):
            pass
        with SCUI.Label(html_for="airplane-mode"): 
            with oj.PD.Prose(text="Airplane Mode", twsty_tags=[bg/green/100]):
                pass

            
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Switch",
                                 childs = [
                                     switch_box
                                           ],
                                 
                                 title="Switch",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                     

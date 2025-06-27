import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")


with writer_ctx:
    with SCUI.Tooltip.Provider() as tooltip_box:
        with SCUI.Tooltip.Root():
            with SCUI.Tooltip.Trigger(class_name="buttonVariants_outline"): # Assuming buttonVariants({ variant: "outline" }) translates to this class name
                with oj.PD.Prose(text="Hover"):
                    pass
            with SCUI.Tooltip.Content():
                with oj.PD.Prose(text="Add to library"):
                    pass
                

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Tooltip",
                                 childs = [
                                     tooltip_box
                                           ],
                                 
                                 title="Tooltip",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                                                        

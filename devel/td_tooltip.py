import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")



with writer_ctx:
    with SCUI.Tooltip() as tooltip_box: 
        with SCUI.Tooltip.Trigger():
            with oj.PD.Prose(text="Hover"):
                pass
        
        with SCUI.Tooltip.Content():
            with oj.PD.P():
                with oj.PD.Prose(text="Add to library"):
                    pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Avatar",
                                 childs = [
                                     tooltip_box
                                           ],
                                 
                                 title="Avatar"
                                 )
oj.add_jproute("/", wp_endpoint)                                                        

import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.ScrollArea(classes="w-32 h-16", orientation="both") as scrollarea_box:
        with oj.PD.Prose(twtags_tags=W/"400px", text="Jokester began sneaking into the castle in the middle of the night and leaving jokes all over the place: under the king's pillow, in his soup, even    in the royal toilet. The king was furious, but he couldn't seem to stop Jokester. And then, one day, the people of the kingdom discovered that the jokes left by Jokester were so funny that they couldn't help but laugh. And    once they started laughing, they couldn't stop."):

        
            pass
    pass




                    
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="ScrollArea",
                                 childs = [
                                     scrollarea_box
                                           ],
                                 
                                 title="ScrollArea",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    


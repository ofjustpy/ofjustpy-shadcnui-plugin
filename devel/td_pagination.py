import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

with writer_ctx:
    with SCUI.Pagination.Root(count=100) as pagination_box:
        
        with SCUI.Pagination.Content():
            
            with SCUI.Pagination.Item():
                
                with SCUI.Pagination.PrevButton():
                    with oj.icons.FontAwesomeIcon(label="faSkull",
                                                  size="2x", 
                                                  fixedWidth=True,
                                                  class_="h-4 w-4"
                                                  ):
                        pass

                    with oj.PD.Span(class_="hidden sm:block"):
                        with oj.PD.Prose(text="Previous"):
                            pass

                        
            with SCUI.Pagination.Item():
                
                with SCUI.Pagination.Link():
                    with oj.PD.Prose(text="1"):
                        pass
            
            with SCUI.Pagination.Item():
                
                with SCUI.Pagination.Link():
                    with oj.PD.Prose(text="2"):
                        pass
            
            with SCUI.Pagination.Item():
                with SCUI.Pagination.NextButton():
                    with oj.icons.FontAwesomeIcon(label="faSkull",
                                                  size="2x", 
                                                  fixedWidth=True,
                                                  class_="h-4 w-4"
                                                  ):
                        pass
                    with oj.PD.Span(class_="hidden sm:block"):
                        with oj.PD.Prose(text="Next"):
                            pass



                    
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Pagination",
                                 childs = [
                                     pagination_box
                                           ],
                                 
                                 title="Pagination",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    

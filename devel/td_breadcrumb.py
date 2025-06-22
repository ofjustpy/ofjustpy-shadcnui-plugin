import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")

with writer_ctx:
    with SCUI.Breadcrumb.Root() as breadcrumb_box:
        with SCUI.Breadcrumb.List():
            with SCUI.Breadcrumb.Item():
                with SCUI.Breadcrumb.Link(href="/"):
                    with oj.PD.Prose(text="Home"):
                        pass
            
            with SCUI.Breadcrumb.Separator():
                pass
            
            with SCUI.Breadcrumb.Item():
                with SCUI.Breadcrumb.Link(href="/components"):
                    with oj.PD.Prose(text="Components"):
                        pass
            
            with SCUI.Breadcrumb.Separator():
                pass
            
            with SCUI.Breadcrumb.Item():
                with SCUI.Breadcrumb.Page():
                    with oj.PD.Prose(text="Breadcrumb"):
                        pass
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Breadcrumb",
                                 childs = [
                                     breadcrumb_box
                                           ],
                                 
                                 title="Avatar",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    

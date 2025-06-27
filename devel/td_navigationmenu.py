import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")


with writer_ctx:
    with SCUI.NavigationMenu.Root() as navigation_menu_root:
        with SCUI.NavigationMenu.List():
            with SCUI.NavigationMenu.Item():
                with SCUI.NavigationMenu.Trigger():
                    with oj.PD.Prose(text="Item One"):
                        pass
                with SCUI.NavigationMenu.Content():
                    with SCUI.NavigationMenu.Link():
                        with oj.PD.Prose(text="Link"):
                            pass
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="NavigationMenu",
                                 childs = [
                                     navigation_menu_root
                                           ],
                                 
                                 title="NavigationMenu",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    

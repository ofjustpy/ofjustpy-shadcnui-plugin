import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.Sheet.Root() as sheet_box: # The outer <Sheet.Root> is often implied or a wrapper
        with  SCUI.Sheet.Trigger():
            with oj.PD.Prose(text="Open"):
                pass
        with SCUI.Sheet.Content(side="right"):
            with SCUI.Sheet.Header():
                with SCUI.Sheet.Title():
                    with oj.PD.Prose(text="Edit profile"):
                        pass
                with SCUI.Sheet.Description():
                    with oj.PD.Prose(text="Make changes to your profile here. Click save when you're done."):
                        pass
            with oj.PD.Div(classes="grid flex-1 auto-rows-min gap-6 px-4"):
                with oj.PD.Div(classes="grid gap-3"):
                    with SCUI.Label(html_for="name", classes="text-right"):
                        with oj.PD.Prose(text="Name"):
                            pass
                    with SCUI.Input(key="name", value="Pedro Duarte"):
                        pass
                with oj.PD.Div(classes="grid gap-3"):
                    with SCUI.Label(html_for="username", classes="text-right"):
                        with oj.PD.Prose(text="Username"):
                            pass
                    with SCUI.Input(key="username", value="@peduarte"):
                        pass
            with SCUI.Sheet.Footer():
                with SCUI.Sheet.Close(classes="bg-green-100"): # Assuming buttonVariants({ variant: "outline" }) translates to this class name
                    with oj.PD.Prose(text="Save changes"):
                        pass

                    
# with writer_ctx:
#     with SCUI.Sheet.Root() as sheet_box:
        
#         with SCUI.Sheet.Trigger():
#             with oj.PD.Prose(text="Open"):
#                 pass
        
#         with SCUI.Sheet.Content():
            
#             with SCUI.Sheet.Header():
                
#                 with SCUI.Sheet.Title():
#                     with oj.PD.Prose(text="Are you sure absolutely sure?"):
#                         pass
                
#                 with SCUI.Sheet.Description():
#                     with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
#                         pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Sheet",
                                 childs = [
                                     sheet_box
                                           ],
                                 
                                 title="Sheet",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                                        

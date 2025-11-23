import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy import icons as Icons

oj.set_style("un")

with writer_ctx:
    with SCUI.Dialog.Root() as dialog_box:
        with SCUI.Dialog.Trigger(classes=""):  # Assuming buttonVariants translates to this class name: buttonVariants_outline
            with oj.PD.Prose(text="Edit Profile"):
                pass
        with SCUI.Dialog.Content(extra_classes="sm:max-w-[425px]"):
            with SCUI.Dialog.Header():
                with SCUI.Dialog.Title():
                    with oj.PD.Prose(text="Edit profile"):
                        pass
                with SCUI.Dialog.Description():
                    with oj.PD.Prose(text="Make changes to your profile here. Click save when you're done."):
                        pass
            with oj.PD.Div(classes="grid gap-4 py-4"):
                with oj.PD.Div(classes="grid grid-cols-4 items-center gap-4"):
                    with SCUI.Label(html_for="name", classes="text-right"):
                        with oj.PD.Prose(text="Name"):
                            pass
                    with SCUI.Input(key="name", value="Pedro Duarte", classes="col-span-3"):
                        pass
                with oj.PD.Div(classes="grid grid-cols-4 items-center gap-4"):
                    with SCUI.Label(html_for="username", classes="text-right"):
                        with oj.PD.Prose(text="Username"):
                            pass
                    with SCUI.Input(key="username", value="@peduarte", classes="col-span-3"):
                        pass
            with SCUI.Dialog.Footer():
                with SCUI.Button(key="abtn", type="submit"):
                    with oj.PD.Prose(text="Save changes"):
                        pass


                    
# with writer_ctx:
#     with SCUI.Dialog.Root() as dialog_box:
        
#         with SCUI.Dialog.Trigger():
#             with oj.PD.Prose(text="Open"):
#                 pass
        
#         with SCUI.Dialog.Content():
            
#             with SCUI.Dialog.Header():
                
#                 with SCUI.Dialog.Title():
#                     with oj.PD.Prose(text="Are you absolutely sure?"):
#                         pass
                
#                 with SCUI.Dialog.Description():
#                     with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
#                         pass


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Dialog",
                                 childs = [
                                     dialog_box
                                           ],
                                 
                                 title="Dialog",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    

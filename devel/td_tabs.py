import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

# with writer_ctx:
#     with SCUI.Tabs.Root(value="password", class_="w-[400px]") as tabs_box:
        
#         with SCUI.Tabs.List():
            
#             with SCUI.Tabs.Trigger(value="account"):
#                 with oj.PD.Prose(text="Account"):
#                     pass
            
#             with SCUI.Tabs.Trigger(value="password"):
#                 with oj.PD.Prose(text="Password"):
#                     pass
        
#         with SCUI.Tabs.Content(value="account"):
#             with oj.PD.Prose(text="Make changes to your account here."):
#                 pass
        
#         with SCUI.Tabs.Content(value="password"):
#             with oj.PD.Prose(text="Change your password here."):
#                 pass


# Python equivalent for the HTML snippet
with writer_ctx:
    with oj.PD.Div(classes="flex w-full max-w-sm flex-col gap-6") as tabs_box:
        with SCUI.Tabs.Root(value="account"):
            with SCUI.Tabs.List():
                with SCUI.Tabs.Trigger(value="account"):
                    with oj.PD.Prose(text="Account"):
                        pass
                with SCUI.Tabs.Trigger(value="password"):
                    with oj.PD.Prose(text="Password"):
                        pass
            with SCUI.Tabs.Content(value="account"):
                with SCUI.Card.Root():
                    with SCUI.Card.Header():
                        with SCUI.Card.Title():
                            with oj.PD.Prose(text="Account"):
                                pass
                        with SCUI.Card.Description():
                            with oj.PD.Prose(text="Make changes to your account here. Click save when you're done."):
                                pass
                    with SCUI.Card.Content(classes="grid gap-6"):
                        with oj.PD.Div(classes="grid gap-3"):
                            with SCUI.Label(html_for="tabs-demo-name"):
                                with oj.PD.Prose(text="Name"):
                                    pass
                            with SCUI.Input(key="tabs-demo-name", value="Pedro Duarte"):
                                pass
                        with oj.PD.Div(classes="grid gap-3"):
                            with SCUI.Label(html_for="tabs-demo-username"):
                                with oj.PD.Prose(text="Username"):
                                    pass
                            with SCUI.Input(key="tabs-demo-username", value="@peduarte"):
                                pass
                    with SCUI.Card.Footer():
                        with SCUI.Button(key="abtn"):
                            with oj.PD.Prose(text="Save changes"):
                                pass
            with SCUI.Tabs.Content(value="password"):
                with SCUI.Card.Root():
                    with SCUI.Card.Header():
                        with SCUI.Card.Title():
                            with oj.PD.Prose(text="Password"):
                                pass
                        with SCUI.Card.Description():
                            with oj.PD.Prose(text="Change your password here. After saving, you'll be logged out."):
                                pass
                    with SCUI.Card.Content(classes="grid gap-6"):
                        with oj.PD.Div(classes="grid gap-3"):
                            with SCUI.Label(html_for="tabs-demo-current"):
                                with oj.PD.Prose(text="Current password"):
                                    pass
                            with SCUI.Input(key="tabs-demo-current", type="password"):
                                pass
                        with oj.PD.Div(classes="grid gap-3"):
                            with SCUI.Label(html_for="tabs-demo-new"):
                                with oj.PD.Prose(text="New password"):
                                    pass
                            with SCUI.Input(key="tabs-demo-new", type="password"):
                                pass
                    with SCUI.Card.Footer():
                        with SCUI.Button(key="abtn"):
                            with oj.PD.Prose(text="Save password"):
                                pass
                            
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Tabs",
                                 childs = [
                                     tabs_box
                                 ],
                                 
                                 title="Tabs",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 
                                 )
oj.add_jproute("/", wp_endpoint)                                                    

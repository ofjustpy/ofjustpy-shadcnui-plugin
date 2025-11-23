import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *

oj.set_style("un")

# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.Drawer.Root() as drawer_box:
        with SCUI.Drawer.Trigger(classes=""): # Assuming buttonVariants translates to this class name
            with oj.PD.Prose(text="Open Drawer"):
                pass
        with SCUI.Drawer.Content():
            with oj.PD.Div(classes="mx-auto w-full max-w-sm"):
                with SCUI.Drawer.Header():
                    with SCUI.Drawer.Title():
                        with oj.PD.Prose(text="Move Goal"):
                            pass
                    with SCUI.Drawer.Description():
                        with oj.PD.Prose(text="Set your daily activity goal."):
                            pass
                with oj.PD.Div(classes="p-4 pb-0"):
                    with oj.PD.Div(classes="flex items-center justify-center space-x-2"):
                        with SCUI.Button(
                                key="abtn", 
                            variant="outline",
                            size="icon",
                            classes="size-8 shrink-0 rounded-full",
                            #onclick="handleClick(-10)", # Direct string for JS function call
                            disabled="goal <= 200" # Direct string for JS expression
                        ):
                            # Representing MinusIcon as text for now
                            with oj.PD.Prose(text="[MinusIcon]"):
                                pass
                            with oj.PD.Span(classes="sr-only"):
                                with oj.PD.Prose(text="Decrease"):
                                    pass
                        with oj.PD.Div(classes="flex-1 text-center"):
                            with oj.PD.Div(classes="text-7xl font-bold tracking-tighter"):
                                # Assuming 'goal' is a variable accessible in the context
                                with oj.PD.Prose(text="{goal}"):
                                    pass
                            with oj.PD.Div(extra_classes="text-muted-foreground text-[0.70rem] uppercase"):
                                with oj.PD.Prose(text="Calories/day"):
                                    pass
                        with SCUI.Button(
                                key="abtn",
                            variant="outline",
                            size="icon",
                            classes="size-8 shrink-0 rounded-full",
                            #onclick="handleClick(10)", # Direct string for JS function call
                            disabled="goal >= 400" # Direct string for JS expression
                        ):
                            # Representing PlusIcon as text for now
                            with oj.PD.Prose(text="[PlusIcon]"):
                                pass
                            with oj.PD.Span(classes="sr-only"):
                                with oj.PD.Prose(text="Increase"):
                                    pass
                    with oj.PD.Div(extra_classes="mt-3 h-[120px]"):
                        with oj.PD.Div(classes="h-full w-full"):
                            # BarChart component is ignored as requested
                            pass
                with SCUI.Drawer.Footer():
                    with SCUI.Button(key="footer"):
                        with oj.PD.Prose(text="Submit"):
                            pass
                    with SCUI.Drawer.Close(classes=""): # Assuming buttonVariants translates to this class name
                        with oj.PD.Prose(text="Cancel"):
                            pass
                        
# with writer_ctx:
#     with SCUI.Drawer.Root() as drawer_box:
        
#         with SCUI.Drawer.Trigger():
#             with oj.PD.Prose(text="Open"):
#                 pass
        
#         with SCUI.Drawer.Content():
            
#             with SCUI.Drawer.Header():
                
#                 with SCUI.Drawer.Title():
#                     with oj.PD.Prose(text="Are you absolutely sure?"):
#                         pass
                
#                 with SCUI.Drawer.Description():
#                     with oj.PD.Prose(text="This action cannot be undone."):
#                         pass
            
#             with SCUI.Drawer.Footer():
                
#                 with SCUI.Button(key="abtn"):
#                     with oj.PD.Prose(text="Submit"):
#                         pass
                
#                 with SCUI.Drawer.Close():
#                     with oj.PD.Prose(text="Cancel"):
#                         pass


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="Drawer",
                                 childs = [
                                     drawer_box
                                           ],
                                 
                                 title="Drawer",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    
                    

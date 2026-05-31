import kavya as kv
from kavya.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from kavya_components import LinearSelector

async def on_click(*args):
    pass

linear_selector = LinearSelector(key="linear_selector", num_iter=range(0,8), on_click = on_click)

kv.set_style("un")

alert = kv.AD.SCUI.divactive.Alert(key="alert_1")
alert.Title(childs = [kv.PC.Span(text="Heads up!")])
alert.Description(childs = [kv.PC.Span(text="You can add components to your app using the cli.")

                            ]
                            
                  )

carousel = kv.AD.SCUI.divactive.Carousel(key="carousel_1", twsty_tags=[W/"1/2"])
item1 = carousel.Item(childs = [kv.PD.Span(text="item1",
                                           classes="p-1")]

                      )
item2 = carousel.Item(childs = [kv.PD.Span(text="item2",
                                           classes="p-1")]

                      )

carousel.Content(childs=[item1, item2])
carousel.Previous()
carousel.Next()

# add a few server side components


wp_endpoint = kv.create_endpoint(key="webpage_mutable_csr",
                                 childs =[linear_selector, alert, carousel],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 skeleton_data_theme = "mint",
                                 svelte_bundle_dir="csr",
                                 rendering_type="CSR"
                                 )
app = kv.load_app()
kv.add_route("/", wp_endpoint)


# class ParentDummy:
#     def add_component(*args, **kwargs):
#         pass
#     pass

# parent_dummy = ParentDummy()

# alert_linked = alert.stub()(parent_dummy)
#print("".join(alert_linked.convert_object_to_json()))

# with MuCtx:
#     with SCUI.Alert.Root(key="alert_1"):
#         pass
    
    


# with MuCtx:
#     with SCUI.Alert.Root() as alert_box:
#         with SCUI.Alert.Title():
#             with oj.PD.Prose(text="Heads up!"):
#                 pass
#             pass

#         with SCUI.Alert.Description():
#             with oj.PD.Prose(text="You can add components to your app using the cli."):
#                 pass
                

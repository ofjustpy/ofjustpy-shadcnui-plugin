import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon

oj.set_style("un")

with writer_ctx:
    with SCUI.Card.Root() as card_root:
        with SCUI.Card.Header():
            with SCUI.Card.Title():
                with oj.PD.Prose(text="Card Title"):
                    pass
            with SCUI.Card.Description():
                with oj.PD.Prose(text="Card Description"):
                    pass
        with SCUI.Card.Content():
            with oj.PD.Prose(text="Card Content"):
                pass
        with SCUI.Card.Footer():
            with oj.PD.Prose(text="Card Footer"):
                pass
            
# card.set_slot_title(text="Create Project", classes="variant-filled")

# card.set_slot_description(text="Deploy your new project in one-click.", classes="variant-filled-primary"

#                            )

# content  = oj.PD.Div(classes="grid w-full items-center gap-4",
#                      childs = [oj.PD.Div(classes="flex flex-col space-y-1.5",
#                                childs= [Label(for_="/terms", text="Name",
#                                               classes=""),
#                                         Input(key="name", placeholder="Name of your project")
#                                ]
                               

#                                ),
#                      oj.PD.Div(classes="flex flex-col space-y-2",
#                                childs = [Label(for_="/framework", text="Framework",
#                                                classes=""),
#                                          select
                                   

#                                    ]
#                                )
#                                ]
#                      )
# card.set_slot_content(content
#     )

# card.set_slot_footer(Button(key="button1", text="Cancel", variant="outline", href="#", ),
#                      Button(key="button2", text="Deploy", variant="link", href="#", ),
#                      classes="flex justify-between",

#     )

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="cards",
                                 childs = [
                                     card_root
                                           ],
                                 
                                 title="Cards",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)
                




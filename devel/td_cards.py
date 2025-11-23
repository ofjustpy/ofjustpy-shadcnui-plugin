import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon

oj.set_style("un")

# rxy = SCUI.Card.Root()

with writer_ctx:
    with SCUI.Card.Root(classes="w-full max-w-sm") as card_root:
        with SCUI.Card.Header():
            with SCUI.Card.Title():
                with oj.PD.Prose(text="Login to your account"):
                    pass
            with SCUI.Card.Description():
                with oj.PD.Prose(text="Enter your email below to login to your account"):
                    pass
            with SCUI.Card.Action():
                # Assuming Button is a pre-defined SCUI component or a similar wrapper
                with SCUI.Button(key="abtn", variant="link"):
                    with oj.PD.Prose(text="Sign Up"):
                        pass
        with SCUI.Card.Content():
            with oj.AD.Form(key="aform"):
                with oj.PD.Div(classes="flex flex-col gap-6"):
                    with oj.PD.Div(classes="grid gap-2"):
                        # Assuming Label is a pre-defined SCUI component or a similar wrapper
                        with SCUI.Label(html_for="email"):
                            with oj.PD.Prose(text="Email"):
                                pass
                        # Assuming Input is a pre-defined SCUI component or a similar wrapper
                        with SCUI.Input(key="email", type="email", placeholder="m@example.com", required=True):
                            pass
                    with oj.PD.Div(classes="grid gap-2"):
                        with oj.PD.Div(classes="flex items-center"):
                            with SCUI.Label(key=="ainput", html_for="password"):
                                with oj.PD.Prose(text="Password"):
                                    pass
                            with oj.PD.A(href="##", classes="ml-auto inline-block text-sm underline-offset-4 hover:underline"):
                                with oj.PD.Prose(text="Forgot your password?"):
                                    pass
                        with SCUI.Input(key="password", type="password", required=True):
                            pass
        with SCUI.Card.Footer(classes="flex-col gap-2"):
            with SCUI.Button(key="abtn", type="submit", classes="w-full"):
                with oj.PD.Prose(text="Login"):
                    pass
            with SCUI.Button(key="abtn", variant="outline", classes="w-full"):
                with oj.PD.Prose(text="Login with Google"):
                    pass


# with writer_ctx:
#     with SCUI.Card.Root() as card_root:
#         with SCUI.Card.Header():
#             with SCUI.Card.Title():
#                 with oj.PD.Prose(text="Card Title"):
#                     pass
#             with SCUI.Card.Description():
#                 with oj.PD.Prose(text="Card Description"):
#                     pass
#         with SCUI.Card.Content():
#             with oj.PD.Prose(text="Card Content"):
#                 pass
#         with SCUI.Card.Footer():
#             with oj.PD.Prose(text="Card Footer"):
#                 pass
            
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
                




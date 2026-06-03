#TODO 
import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Main outer box layout
    with kv.PD.Div(classes="p-8 flex justify-center") as card_box:

        # Card Root Definition
        with kv.AD.SCUI.divactive.Card.Root(classes="-my-4 w-full max-w-sm", key="login_card"):
            
            # Card Header
            with SCUI.divactive.Card.Header():
                with SCUI.divactive.Card.Title():
                    with kv.PD.Prose(text="Login to your account"):
                        pass
                
                with SCUI.divactive.Card.Description():
                    with kv.PD.Prose(text="Enter your email below to login to your account"):
                        pass
                
                with SCUI.divactive.Card.Action():
                    with SCUI.divactive.Button(variant="link"):
                        with kv.PD.Prose(text="Sign Up"):
                            pass

            # Card Content
            with SCUI.divactive.Card.Content():
                # Form structure containing fields
                with kv.PD.Form():
                    with kv.PD.Div(classes="flex flex-col gap-6"):
                        
                        # Email Input Field Group
                        with kv.PD.Div(classes="grid gap-2"):
                            with SCUI.divactive.Label(for_id="email"): # using for_id to prevent python keyword collision
                                with kv.PD.Prose(text="Email"):
                                    pass
                            with SCUI.divactive.Input(id="email", type="email", placeholder="m@example.com", required=True):
                                pass

                        # Password Input Field Group
                        with kv.PD.Div(classes="grid gap-2"):
                            with kv.PD.Div(classes="flex items-center"):
                                with SCUI.divactive.Label(for_id="password"):
                                    with kv.PD.Prose(text="Password"):
                                        pass
                                with kv.PD.A(
                                    href="##", 
                                    classes="ms-auto inline-block text-sm underline-offset-4 hover:underline"
                                ):
                                    with kv.PD.Prose(text="Forgot your password?"):
                                        pass
                            with SCUI.divactive.Input(id="password", type="password", required=True):
                                pass

            # Card Footer
            with SCUI.divactive.Card.Footer(classes="flex-col gap-2"):
                with SCUI.divactive.Button(type="submit", classes="w-full"):
                    with kv.PD.Prose(text="Login"):
                        pass
                with SCUI.divactive.Button(variant="outline", classes="w-full"):
                    with kv.PD.Prose(text="Login with Google"):
                        pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[card_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

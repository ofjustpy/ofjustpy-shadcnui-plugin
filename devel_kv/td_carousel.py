import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *



with MuCtx:
    # Outer layout container
    with kv.PD.Div(classes="p-16 flex justify-center items-center w-full") as carousel_box:

        # Carousel Root Definition
        with kv.AD.SCUI.divactive.Carousel.Root(classes="w-full max-w-xs", key="carousel_demo"):
            
            # Carousel Content track wrapper
            with SCUI.divactive.Carousel.Content():
                
                # Slide Item 1
                with SCUI.divactive.Carousel.Item():
                    with kv.PD.Div(classes="p-1"):
                        with SCUI.divactive.Card.Root():
                            with SCUI.divactive.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                                with kv.PD.Span(classes="text-4xl font-semibold"):
                                    with kv.PD.Prose(text="1"):
                                        pass

                # Slide Item 2
                with SCUI.divactive.Carousel.Item():
                    with kv.PD.Div(classes="p-1"):
                        with SCUI.divactive.Card.Root():
                            with SCUI.divactive.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                                with kv.PD.Span(classes="text-4xl font-semibold"):
                                    with kv.PD.Prose(text="2"):
                                        pass

                # Slide Item 3
                with SCUI.divactive.Carousel.Item():
                    with kv.PD.Div(classes="p-1"):
                        with SCUI.divactive.Card.Root():
                            with SCUI.divactive.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                                with kv.PD.Span(classes="text-4xl font-semibold"):
                                    with kv.PD.Prose(text="3"):
                                        pass

            # Navigation Controls
            with SCUI.divactive.Carousel.Previous():
                pass
                
            with SCUI.divactive.Carousel.Next():
                pass
            


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[carousel_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)



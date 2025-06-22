import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *
import shadcnui_components as SCUI
oj.set_style("un")

with writer_ctx:
    with SCUI.Carousel.Root(classes="w-full max-w-xs") as carousel_box:
        with SCUI.Carousel.Content():
            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"1"):
                                    pass

            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"2"):
                                    pass                                

            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"3"):
                                    pass

            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"4"):
                                    pass
                                
        with SCUI.Carousel.Previous():
            pass
        
        with SCUI.Carousel.Next():
            pass
        
# carousel = Carousel(key="select")

             
# item1 = carousel.Item(value="light", text="Light")
# item2 = carousel.Item(value="dark", text="Dark")

# item3 = carousel.Item(value="light", text="Blue")
# item4 = carousel.Item(value="dark", text="Green")
             
# carousel.set_slot_content(item1, item2, item3, item4, classes="bg-pink-400")

app = oj.load_app()
adiv = oj.PC.Div(childs=[carousel_box])

wp_endpoint = oj.create_endpoint(key="carousel",
                                 childs = [
                                     carousel_box
                                           ],
                                 title="Carousel",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )

oj.add_jproute("/", wp_endpoint)
                




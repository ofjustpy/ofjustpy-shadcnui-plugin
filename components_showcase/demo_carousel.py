import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
from py_tailwind_utils import *
import shadcnui_components as SCUI
oj.set_style("un")
print("loading demo_carousel")
with writer_ctx:
    with SCUI.Carousel.Root(classes="w-full max-w-xs") as carousel_box:
        with SCUI.Carousel.Content():
            with SCUI.Carousel.Item(classes="basis-1/3"):
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"1"):
                                    pass

            with SCUI.Carousel.Item(classes="basis-1/3"):
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"2"):
                                    pass                                

            with SCUI.Carousel.Item(classes="basis-1/3"):
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card.Root():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"3"):
                                    pass

            with SCUI.Carousel.Item(classes="basis-1/3"):
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
        








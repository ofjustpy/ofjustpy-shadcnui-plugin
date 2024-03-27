import ofjustpy as oj
from shadcnui_components.components import Carousel, Card
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *


carousel = Carousel(key="select")

             
item1 = carousel.Item(value="light", text="Light")
item2 = carousel.Item(value="dark", text="Dark")

item3 = carousel.Item(value="light", text="Blue")
item4 = carousel.Item(value="dark", text="Green")
             
carousel.set_slot_content(item1, item2, item3, item4, classes="bg-pink-400")

app = oj.load_app()
adiv = oj.PC.Div(childs=[carousel])

wp_endpoint = oj.create_endpoint(key="carousel",
                                 childs = [
                                     adiv
                                           ],
                                 title="Carousel"
                                 )

oj.add_jproute("/", wp_endpoint)
                




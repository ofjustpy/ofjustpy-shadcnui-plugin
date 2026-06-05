from kavya.themes import ui_styles
from kavya.type_factory.static_type_factory import (
    ActiveDiv_StubWrappedTypeGen,
    PassiveDiv_StubWrappedTypeGen,
)
from .shadcn_type_factory import (
    CSR_comp_generator,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
)
vue_type = "shadcnui_component"
scui_comp_label = "carousel"


class CarouselMixin:

    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "carousel_root"


# Base generation pipeline wrapper
_Carousel = ActiveDiv_StubWrappedTypeGen(
    "Carousel",
    CarouselMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_carousel,
)

# Module-level component definitions
Root = CSR_comp_generator(_Carousel)

Content = gen_PassiveDiv_type_by_tag("Content", prefix="Carousel_")
Item = gen_PassiveDiv_type_by_tag("Item", prefix="Carousel_")
Previous = gen_PassiveDiv_type_by_tag("Previous", prefix="Carousel_")
Next = gen_PassiveDiv_type_by_tag("Next", prefix="Carousel_")




# Module-level registry mapping using the Carousel namespace container
kv_label_to_shadcn_comp_map = """
    'carousel_root': Carousel.Root,
    'carousel_content': Carousel.Content,
    'carousel_item': Carousel.Item,
    'carousel_previous': Carousel.Previous,
    'carousel_next': Carousel.Next
"""

import_stmt = """ import * as Carousel from "$lib/components/ui/carousel/index.js";"""

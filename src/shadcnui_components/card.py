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

scui_comp_label = "card"

vue_type = "shadcnui_component"
class CardMixin:

    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = vue_type
        self.domDict.html_tag = "card_root"


# Base generation pipeline wrapper
_Card = ActiveDiv_StubWrappedTypeGen(
    "Card",
    CardMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_card,
)

# Module-level component definitions
Root = CSR_comp_generator(_Card)

Header = gen_PassiveDiv_type_by_tag("Header", prefix="Card_")
Title = gen_PassiveDiv_type_by_tag("Title", prefix="Card_")
Description = gen_PassiveDiv_type_by_tag("Description", prefix="Card_")
Content = gen_PassiveDiv_type_by_tag("Content", prefix="Card_")
Footer = gen_PassiveDiv_type_by_tag("Footer", prefix="Card_")
Action = gen_PassiveDiv_type_by_tag("Action", prefix="Card_")




# Module-level registry mapping using the Card namespace container
kv_label_to_shadcn_comp_map = """
    'card_root': Card.Root,
    'card_header': Card.Header,
    'card_title': Card.Title,
    'card_description': Card.Description,
    'card_content': Card.Content,
    'card_footer': Card.Footer,
    'card_action': Card.Action
"""
import_stmt = """import * as Card from "$lib/components/ui/card/index.js";
"""

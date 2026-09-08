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
scui_comp_label = "hover-card"


class HoverCardMixin:

    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "hovercard_root"


# Base generation pipeline wrapper
_HoverCard = ActiveDiv_StubWrappedTypeGen(
    "HoverCard",
    HoverCardMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_hovercard,
)

# Module-level component definitions
Root = CSR_comp_generator(_HoverCard)

Trigger = gen_ActiveDiv_type_by_tag("Trigger", prefix="HoverCard_")
Content = gen_PassiveDiv_type_by_tag("Content", prefix="HoverCard_")


# Module-level registry mapping using the HoverCard namespace container
kv_label_to_shadcn_comp_map = """
    'hovercard_root': HoverCard.Root,
    'hovercard_trigger': HoverCard.Trigger,
    'hovercard_content': HoverCard.Content
"""

import_stmt = """ import * as HoverCard from "$lib/components/ui/hover-card/index.js";"""

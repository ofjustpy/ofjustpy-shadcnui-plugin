from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.themes import ui_styles
vue_type = "shadcnui_component"
scui_comp_label = "collapsible"


class CollapsibleMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "collapsible_root"


# Base generation pipeline wrapper
_Collapsible = ActiveDiv_StubWrappedTypeGen(
    "Collapsible",
    CollapsibleMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_collapsible,
)

# Module-level component definitions
Root = CSR_comp_generator(_Collapsible)

Trigger = gen_PassiveDiv_type_by_tag("Trigger", prefix="Collapsible_")
Content = gen_PassiveDiv_type_by_tag("Content", prefix="Collapsible_")




import_stmt = """import * as Collapsible from "$lib/components/ui/collapsible/index.js";
"""

# Module-level registry mapping using the Collapsible namespace container
kv_label_to_shadcn_comp_map = """
    'collapsible_root': Collapsible.Root,
    'collapsible_trigger': Collapsible.Trigger,
    'collapsible_content': Collapsible.Content,
"""

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

scui_comp_label = "popover"

vue_type = "shadcnui_component"
class PopoverMixin:

    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = vue_type
        self.domDict.html_tag = "popover_root"


# Base generation pipeline wrapper
_Popover = ActiveDiv_StubWrappedTypeGen(
    "Popover",
    PopoverMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_popover,
)

# Module-level component definitions
Root = CSR_comp_generator(_Popover)

Trigger = gen_PassiveDiv_type_by_tag("Trigger", prefix="Popover_")
Content = gen_PassiveDiv_type_by_tag("Content", prefix="Popover_")




# Module-level registry mapping using the Card namespace container
kv_label_to_shadcn_comp_map = """
    'popover_root': Popover.Root,
    'popover_trigger': Popover.Trigger,
    'popover_content': Popover.Content,
"""

import_stmt = """import * as Popover from "$lib/components/ui/popover/index.js";
"""

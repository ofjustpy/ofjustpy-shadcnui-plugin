from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles

scui_comp_label = "badge"


class BadgeMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "badge"

        if "variant" in kwargs:
            self.attrs["variant"] = kwargs.get("variant")


# Base generation pipeline wrapper (Using ActiveDiv to align with CSR_comp_generator pipeline)
_Badge = ActiveDiv_StubWrappedTypeGen(
    "Badge",
    BadgeMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_badge,
)

Root = CSR_comp_generator(_Badge)



import_stmt = """import { Badge } from "$lib/components/ui/badge/index.js";
"""

# Module-level registry mapping 
kv_label_to_shadcn_comp_map = """'badge': Badge
"""

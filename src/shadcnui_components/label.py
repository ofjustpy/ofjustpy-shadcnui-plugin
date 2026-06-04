from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles

scui_comp_label = "label"


class LabelMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "label"


# Base generation pipeline wrapper using ActiveDiv to match CSR_comp_generator setup
_Label = ActiveDiv_StubWrappedTypeGen(
    "Label",
    LabelMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_label,
)

Root = CSR_comp_generator(_Label)




import_stmt = """import { Label } from "$lib/components/ui/label/index.js";
"""

# Module-level registry mapping
kv_label_to_shadcn_comp_map = """'label': Label
"""

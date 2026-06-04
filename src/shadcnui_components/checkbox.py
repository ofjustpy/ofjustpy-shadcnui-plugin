from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles

scui_comp_label = "checkbox"


class CheckboxMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "checkbox"


# Base generation pipeline wrapper using ActiveDiv for interactive/form components
_Checkbox = ActiveDiv_StubWrappedTypeGen(
    "Checkbox",
    CheckboxMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_checkbox,
)

Root = CSR_comp_generator(_Checkbox)



import_stmt = """import { Checkbox } from "$lib/components/ui/checkbox/index.js";
"""

# Module-level registry mapping
kv_label_to_shadcn_comp_map = """'checkbox': Checkbox
"""

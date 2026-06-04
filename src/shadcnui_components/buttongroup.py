from .shadcn_type_factory import (PassiveDiv_StubWrappedTypeGen,
                                  ActiveDiv_StubWrappedTypeGen,
                                  gen_ActiveDiv_type_by_tag,
                                  gen_PassiveDiv_type_by_tag,
                                  CSR_comp_generator)
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles

scui_comp_label = "button-group"

class ButtonGroupMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "buttongroup_root"


    
_ButtonGroup = ActiveDiv_StubWrappedTypeGen(
    "ButtonGroup",
    ButtonGroupMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_buttongroup,
)
Root = CSR_comp_generator(_ButtonGroup)
Separator = gen_PassiveDiv_type_by_tag("Separator", prefix="ButtonGroup_")
import_stmt = """import * as ButtonGroup from "$lib/components/ui/button-group/index.js";
"""
        
kv_label_to_shadcn_comp_map = """'buttongroup_root':ButtonGroup.Root,
'buttongroup_separator':ButtonGroup.Separator"""

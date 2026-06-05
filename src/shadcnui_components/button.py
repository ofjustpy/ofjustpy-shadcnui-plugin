from .shadcn_type_factory import (PassiveDiv_StubWrappedTypeGen,
                                  ActiveDiv_StubWrappedTypeGen,
                                  gen_ActiveDiv_type_by_tag,
                                  gen_PassiveDiv_type_by_tag,
                                  CSR_comp_generator)
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles
vue_type = "shadcnui_component"
scui_comp_label = "button"

class ButtonMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "button"
        for attr in ["variant", "disabled", "href", "size"]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get(attr)

        if "type_" in kwargs:
            self.attrs["type"] = kwargs.get("type_")

        if "variant" in kwargs:
            self.attrs["variant"] = kwargs.get('variant')
        if "value" in kwargs:
            self.domDict["value"] = kwargs.get("value")

    @property
    def value(self):
        """
        The 'value' attribute of the <data> element specifies the machine-readable value associated with the element.
        """
        return self.domDict.get("value", None)

    
_Button = ActiveDiv_StubWrappedTypeGen(
    "Button",
    ButtonMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_button,
)
Root = CSR_comp_generator(_Button)
import_stmt = """import { Button } from "$lib/components/ui/button/index.js";
"""
        
kv_label_to_shadcn_comp_map = """'button':Button"""

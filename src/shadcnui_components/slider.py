from .shadcn_type_factory import (
    PassiveDiv_StubWrappedTypeGen,
    ActiveDiv_StubWrappedTypeGen,
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.themes import ui_styles

scui_comp_label = "slider"

vue_type = "shadcnui_bindvalue_component"

class SliderMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "shadcnui_bindvalue_component"
        self.domDict.html_tag = "slider"

        # Explicitly maps standard structural primitives
        for attr in ["value", "step"]:
            if attr in kwargs:
                self.attrs[attr] = kwargs.get(attr)
                
        # Remaps keyword protected max_ argument to html safe max attribute
        if "max_" in kwargs:
            self.attrs["max"] = kwargs.get("max_")


# Base generation pipeline wrapper using ActiveDiv for dynamic input components
_Slider = ActiveDiv_StubWrappedTypeGen(
    "Slider",
    SliderMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.scui_slider,
)

Root = CSR_comp_generator(_Slider)


import_stmt = """import { Slider } from "$lib/components/ui/slider/index.js";
"""

# Module-level registry mapping
kv_label_to_shadcn_comp_map = """
    'slider': Slider,
"""

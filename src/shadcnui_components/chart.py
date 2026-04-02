from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR
from addict_tracking_changes import Dict
from ofjustpy.htmlcomponents_impl import assign_id


from .components import gen_Div_type_by_tag

class ChartMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "chart"
        pass

    class ContainerMixin:
        def __init__(self, **kwargs):
            self.domDict.vue_type = "shadcnui_component"
            self.domDict.html_tag = "chart_container"

            if 'config' in kwargs:
                self.attrs["config"] = kwargs.get('config')


    Container =  gen_Div_type(HCType.passive,
                              "Chart_Container",
                              ContainerMixin,
                              stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_chart_container,
                              
    )
    
                
Chart = gen_Div_type(
    HCType.passive,
    "Chart",
    ChartMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_chart,
)



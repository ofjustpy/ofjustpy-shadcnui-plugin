
class AspectRatioMixin:
    def __init__(self, **kwargs):
        self.domDict["vue_type"] = "shadcnui_component"
        self.domDict["html_tag"] = "aspectratio"

        if 'ratio' in kwargs:
            self.attrs['ratio']= kwargs.get('ratio')

AspectRatio = PassiveDiv_StubWrappedTypeGen(
                     "AspectRatio",
                     AspectRatioMixin,
                     static_addon_mixins=[TR.HCTextMixin],
                     stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_aspectratio,
                     )

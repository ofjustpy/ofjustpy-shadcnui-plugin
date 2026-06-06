from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.type_factory.static_type_factory import ActiveDiv_StubWrappedTypeGen, PassiveDiv_StubWrappedTypeGen
from kavya.htmlcomponents import html_tag_mixins as HTM
from kavya.themes import ui_styles


class BindValueMixin:
    def __init__(self, *args, **kwargs):
        if "bindvalue" in kwargs:
            self.bindvalue = kwargs.get("bindvalue")

def gen_ActiveDiv_type_by_tag(tag,
                        prefix="",
                        attrs=None,
                        addon_mixins = None
                        ):
    """
    TODO: bind_value: implies that component is tied to a value e.g.
    <Menubar.RadioGroup bind:value={profileRadioValue}>
    """

    class Mixin:
        kv_label_to_shadcn_comp_map = ""
        scui_comp_label = ""
        html_tag = f"{prefix}{tag}".lower()
        def __init__(self, attrs=attrs, **kwargs):
            self.domDict.vue_type = "shadcnui_component"
            self.domDict.html_tag = f"{prefix}{tag}".lower()
            # TODO
            #self.domDict.js_eval_map = kwargs.get('js_eval_map', {})
            
            if attrs:
                for attr in attrs:
                    if attr in kwargs:
                        self.attrs[attr] = kwargs.get(attr)

                        pass
                    pass
                pass
            pass

    class_def = assign_id(ActiveDiv_StubWrappedTypeGen(f"{prefix}{tag}",
                                                       Mixin,
                                                       addon_mixins = addon_mixins,
                                                       stytags_getter_func=lambda m=ui_styles: getattr(m.sty,
                                                                                                       f"scui_{prefix.lower()}{tag.lower()}"
                                                                                                       )
                                                       )
                          )
    
    return class_def


def gen_PassiveDiv_type_by_tag(tag,
                        prefix="",
                        attrs=None,
                        addon_mixins = None
                        ):
    """
    TODO: bind_value: implies that component is tied to a value e.g.
    <Menubar.RadioGroup bind:value={profileRadioValue}>
    """

    class Mixin:
        kv_label_to_shadcn_comp_map = ""
        scui_comp_label = ""
        html_tag = f"{prefix}{tag}".lower()
        def __init__(self, attrs=attrs, **kwargs):
            self.domDict.vue_type = "shadcnui_component"
            self.domDict.html_tag = f"{prefix}{tag}".lower()
            # TODO
            #self.domDict.js_eval_map = kwargs.get('js_eval_map', {})
            
            if attrs:
                for attr in attrs:
                    if attr in kwargs:
                        self.attrs[attr] = kwargs.get(attr)

                        pass
                    pass
                pass
            pass

    # in order to reuse
    # html mixins like ImgMixin
    # that set the html_tag to img
    # we need to reset that 

    if addon_mixins == None:
        addon_mixins = []
        
    class SetHTMLTag:
        html_tag = f"{prefix}{tag}".lower()
        def __init__(self, *args, **kwargs):
            self.domDict.html_tag = f"{prefix}{tag}".lower()
            pass

        
    class_def = PassiveDiv_StubWrappedTypeGen(f"{prefix}{tag}",
                                              Mixin,
                                              addon_mixins = [*addon_mixins, SetHTMLTag],
                                              stytags_getter_func=lambda m=ui_styles: getattr(m.sty,
                                                                                                       f"scui_{prefix.lower()}{tag.lower()}"
                                                                                                       )
                                              )
                          
    
    return class_def



def CSR_comp_generator(scui_stub_wrapper):
    # override render html
    class _Comp(scui_stub_wrapper):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            pass

        def post_id_assign_callback(self):
            self.prepare_htmlRender()
            pass

        def build_renderHtml(self):
            self.htmlRender_open_tag = f'''<{self.html_tag} {" ".join(self.htmlRender_attr)}>'''
            self.htmlRender_close_tag =  f'''</{self.html_tag}>'''


        def prepare_htmlRender(self):
            # mutable shell's staticCore have
            # prepare_htmlRender which gets
            # updated after update to attrs
            # prepare_htmlRender is also called
            # by eventMixin following .on
            # event addition. 
            self.build_renderHtml()
        def to_html_iter(self):
            yield self.htmlRender_open_tag
            yield from self.htmlRender_body
            # for achild in self.components:
            #     yield from achild.to_html_iter()
            yield self.htmlRender_close_tag


    return assign_id(_Comp)



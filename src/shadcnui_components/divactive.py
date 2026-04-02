from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.type_factory.static_type_factory import ActiveDiv_StubWrappedTypeGen
from kavya.htmlcomponents import html_tag_mixins as HTM
from kavya.themes import ui_styles

def gen_Div_type_by_tag(tag,
                        prefix="",
                        attrs=None,
                        ):
    """
    TODO: bind_value: implies that component is tied to a value e.g.
    <Menubar.RadioGroup bind:value={profileRadioValue}>
    """

    class Mixin:
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
                                                       stytags_getter_func=lambda m=ui_styles: getattr(m.sty,
                                                                                                       f"scui_{prefix.lower()}{tag.lower()}"
                                                                                                       )
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
            print("id of the object = ", self.id)
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


class AppendChildMixin:
    def __init__(self, *args, **kwargs):
        # add title and description as children
        self.components = [None, None]



        
class AlertMixin:
    scui_comp_label = "Alert"
    def __init__(self, *args, **kwargs):
        self.domDict.vue_type= "shadcnui_component"
        self.domDict.html_tag = "alert_root"

        self.title = None
        self.description = None

    kv_label_to_shadcn_comp_map = """
    'alert_root': Alert.Root,
    'alert_title': Alert.Title,
    'alert_description': Alert.Description,
    """
    

    _Title = gen_Div_type_by_tag("Title", prefix="Alert_")
    _Description = gen_Div_type_by_tag("Description", prefix="Alert_")
        
    #Root = gen_Div_type_by_tag("Root", prefix="Alert_")
    def Title(self, *args, **kwargs):
        self.components[0] =  AlertMixin._Title(key = f"Title_{self.key}", *args, **kwargs)
        pass

    def Description(self, *args, **kwargs):
        self.components[1] =  AlertMixin._Description(key = f"Description_{self.key}", *args, **kwargs)

            

    # Root = gen_Div_type_by_tag("Root", prefix="Alert_")        
    # Title = gen_Div_type_by_tag("Title", prefix="Alert_")
    # Description = gen_Div_type_by_tag("Description", prefix="Alert_")
        

    
_Alert = ActiveDiv_StubWrappedTypeGen("Alert",
                                      AlertMixin,
                                      
                                      addon_mixins=[AppendChildMixin],
                                      stytags_getter_func=lambda m=ui_styles: m.sty.scui_alert,
                                               
                                       )


Alert = CSR_comp_generator(_Alert)

class CarouselMixin:
    scui_comp_label = "Carousel"
    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "shadcnui_component"
        self.domDict.html_tag = "carousel_root"
        # Initializing component slots if necessary
        
    # Internal definitions for sub-components
    _Content = gen_Div_type_by_tag("Content", prefix="Carousel_")
    _Item = gen_Div_type_by_tag("Item", prefix="Carousel_")
    _Previous = gen_Div_type_by_tag("Previous", prefix="Carousel_")
    _Next = gen_Div_type_by_tag("Next", prefix="Carousel_")

    kv_label_to_shadcn_comp_map = """
    'carousel_root': Carousel.Root,
    'carousel_content': Carousel.Content,
    'carousel_item': Carousel.Item,
    'carousel_previous': Carousel.Previous,
    'carousel_next': Carousel.Next,
    """
    def Content(self, *args, **kwargs):
        self.components[0] = CarouselMixin._Content(key=f"Content_{self.key}", *args, **kwargs)

    def Item(self, *args, **kwargs):
        return CarouselMixin._Item(key=f"Item_{self.key}", *args, **kwargs)


    def Previous(self, *args, **kwargs):
        self.components[1] = CarouselMixin._Previous(key=f"Previous_{self.key}", *args, **kwargs)

    def Next(self, *args, **kwargs):
        self.components[2] = CarouselMixin._Next(key=f"Next_{self.key}", *args, **kwargs)


# Carousel has 3 childs    
class AppendChildMixin:
    def __init__(self, *args, **kwargs):
        # add title and description as children
        self.components = [None, None, None]
        
# New generator call using the ActiveDiv_StubWrappedTypeGen factory
_Carousel = ActiveDiv_StubWrappedTypeGen("Carousel",
                                         CarouselMixin,
                                         addon_mixins=[AppendChildMixin],
                                         stytags_getter_func=lambda m=ui_styles: m.sty.scui_carousel,
 )
Carousel = CSR_comp_generator(_Carousel)

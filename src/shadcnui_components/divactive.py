
# def AppendChildMixinFactory(num_components=2):
#     class AppendChildMixin:
#         def __init__(self,  *args,  **kwargs):
#             # add title and description as children
#             self.components = [None] * num_components

#     return AppendChildMixin
from .shadcn_type_factory import (PassiveDiv_StubWrappedTypeGen,
                                  ActiveDiv_StubWrappedTypeGen,
                                  gen_ActiveDiv_type_by_tag,
                                  gen_PassiveDiv_type_by_tag,
                                  CSR_comp_generator)
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles
from .  import alert_dialog as   AlertDialog
from .  import avatar as   Avatar
from .  import carousel as Carousel
from .  import card as Card
from . import button as Button


#TBD: TODO: 
# class BadgeMixin:
#     def __init__(self, **kwargs):
#         self.domDict["vue_type"] = "shadcnui_component"
#         self.domDict["html_tag"] = "badge"

#         if 'variant' in kwargs:
#             self.attrs['variant']= kwargs.get('variant')

# Badge = gen_Div_type(HCType.passive,
#                      "Badge",
#                      BadgeMixin,
#                      static_addon_mixins=[TR.HCTextMixin],
#                      stytags_getter_func=lambda m=ui_styles: m.sty.shadcnui_badge,
#                      )



# class AlertMixin:
#     scui_comp_label = "Alert"
#     def __init__(self, *args, **kwargs):
#         self.domDict.vue_type= "shadcnui_component"
#         self.domDict.html_tag = "alert_root"

#         self.title = None
#         self.description = None

#     kv_label_to_shadcn_comp_map = """
#     'alert_root': Alert.Root,
#     'alert_title': Alert.Title,
#     'alert_description': Alert.Description,
#     """
    

#     _Title = gen_PassiveDiv_type_by_tag("Title", prefix="Alert_")
#     _Description = gen_PassiveDiv_type_by_tag("Description", prefix="Alert_")
        
#     #Root = gen_Div_type_by_tag("Root", prefix="Alert_")
#     def Title(self, *args, **kwargs):
#         self.components[0] =  AlertMixin._Title(key = f"Title_{self.key}", *args, **kwargs)
#         pass

#     def Description(self, *args, **kwargs):
#         self.components[1] =  AlertMixin._Description(key = f"Description_{self.key}", *args, **kwargs)
    
# _Alert = ActiveDiv_StubWrappedTypeGen("Alert",
#                                       AlertMixin,
                                      
#                                       addon_mixins=[AppendChildMixinFactory(num_components=2)],
#                                       stytags_getter_func=lambda m=ui_styles: m.sty.scui_alert,
                                               
#                                        )


# Alert = CSR_comp_generator(_Alert)




# class CarouselMixin:
#     scui_comp_label = "Carousel"
#     def __init__(self, *args, **kwargs):
#         self.domDict.vue_type = "shadcnui_component"
#         self.domDict.html_tag = "carousel_root"
#         # Initializing component slots if necessary
        
#     # Internal definitions for sub-components
#     _Content = gen_PassiveDiv_type_by_tag("Content", prefix="Carousel_")
#     _Item = gen_PassiveDiv_type_by_tag("Item", prefix="Carousel_")
#     _Previous = gen_PassiveDiv_type_by_tag("Previous", prefix="Carousel_")
#     _Next = gen_PassiveDiv_type_by_tag("Next", prefix="Carousel_")

#     kv_label_to_shadcn_comp_map = """
#     'carousel_root': Carousel.Root,
#     'carousel_content': Carousel.Content,
#     'carousel_item': Carousel.Item,
#     'carousel_previous': Carousel.Previous,
#     'carousel_next': Carousel.Next,
#     """
#     # def Content(self, *args, **kwargs):
#     #     self.components[0] = CarouselMixin._Content(key=f"Content_{self.key}", *args, **kwargs)

#     # def Item(self, *args, **kwargs):
#     #     return CarouselMixin._Item(key=f"Item_{self.key}", *args, **kwargs)


#     # def Previous(self, *args, **kwargs):
#     #     self.components[1] = CarouselMixin._Previous(key=f"Previous_{self.key}", *args, **kwargs)

#     # def Next(self, *args, **kwargs):
#     #     self.components[2] = CarouselMixin._Next(key=f"Next_{self.key}", *args, **kwargs)


        
# # New generator call using the ActiveDiv_StubWrappedTypeGen factory
# _Carousel = ActiveDiv_StubWrappedTypeGen("Carousel",
#                                          CarouselMixin,
#                                          #addon_mixins=[AppendChildMixinFactory(num_components=3)],
#                                          stytags_getter_func=lambda m=ui_styles: m.sty.scui_carousel,
#  )
# Carousel = CSR_comp_generator(_Carousel)

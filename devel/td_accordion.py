import ofjustpy as oj
from shadcnui_components.components import AccordionItem
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *
# with Accordion():
#     # first item
#     with AccordionItem():
#         with Header():
#             with Trigger():
#         with Content():
#             pass

#     # second item 
#     with AccordionItem():
#         with Header():
#             with Trigger():
#         with Content():
#             pass        
    
# accordion = Accordion()

# accordion.AccordionItem()

accordionitem = AccordionItem(value="value1")
accordionitem.set_slot_trigger(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                                               ),
                               classes = "flex w-full flex-1 items-center justify-between py-5 text-[15px] font-medium transition-all [&[data-state=open]>span>svg]:rotate-180"
                               
                            )

accordionitem.set_slot_content(oj.PD.Prose(text="What is Día de los Muertos?", classes="font-bold"),
                               transition="slide"
                            )


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="accordion",
                                 childs = [                                           
                                           accordionitem
                                           ],
                                 
                                 title="Accordion"
                                 )
oj.add_jproute("/", wp_endpoint)
                

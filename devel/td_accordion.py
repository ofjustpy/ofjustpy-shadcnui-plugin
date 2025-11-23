import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
from py_tailwind_utils import *
import shadcnui_components as SCUI
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

oj.set_style("un")

# with writer_ctx:
#     with SCUI.Accordion.Root() as accordion_box:
        
#         with SCUI.Accordion.Item(value="item-1"):
            
#             with SCUI.Accordion.Trigger():
#                 with oj.PD.Prose(text="Is it accessible?"):
#                     pass
            
#             with SCUI.Accordion.Content():
#                 with oj.PD.Prose(text="Yes. It adheres to the WAI-ARIA design pattern."):
#                     pass
                
# # with Accordion():
# #     # first item
# #     with AccordionItem():
# #         with Header():
# #             with Trigger():
# #         with Content():
# #             pass

# #     # second item 
# #     with AccordionItem():
# #         with Header():
# #             with Trigger():
# #         with Content():
# #             pass        
    
# # accordion = Accordion()

# # accordion.AccordionItem()

# accordionitem = AccordionItem(value="value1")
# accordionitem.set_slot_trigger(FontAwesomeIcon(label="faSkull", size="1x", 
#                                             classes="text-xl w-6 text-center",
                                            
#                                                ),
#                                classes = "flex w-full flex-1 items-center justify-between py-5 text-[15px] font-medium transition-all [&[data-state=open]>span>svg]:rotate-180"
                               
#                             )

# accordionitem.set_slot_content(oj.PD.Prose(text="What is Día de los Muertos?", classes="font-bold"),
#                                transition="slide"
#                             )

# Python equivalent for the HTML snippet
with writer_ctx:
    with SCUI.Accordion.Root(type="single", extra_classes="w-full sm:max-w-[70%]", value="item-1") as accordion_box: 
        with SCUI.Accordion.Item(value="item-1"):
            with SCUI.Accordion.Trigger():
                with oj.PD.Prose(text="Product Information"):
                    pass
            with SCUI.Accordion.Content(classes="flex flex-col gap-4 text-balance"):
                with oj.PD.P():
                    with oj.PD.Prose(text="""Our flagship product combines cutting-edge technology with sleek design.
        Built with premium materials, it offers unparalleled performance and
        reliability."""):
                        pass
                with oj.PD.P():
                    with oj.PD.Prose(text="""Key features include advanced processing capabilities, and an intuitive
        user interface designed for both beginners and experts."""):
                        pass
        with SCUI.Accordion.Item(value="item-2"):
            with SCUI.Accordion.Trigger():
                with oj.PD.Prose(text="Shipping Details"):
                    pass
            with SCUI.Accordion.Content(classes="flex flex-col gap-4 text-balance"):
                with oj.PD.P():
                    with oj.PD.Prose(text="""We offer worldwide shipping through trusted courier partners. Standard
        delivery takes 3-5 business days, while express shipping ensures
        delivery within 1-2 business days."""):
                        pass
                with oj.PD.P():
                    with oj.PD.Prose(text="""All orders are carefully packaged and fully insured. Track your shipment
        in real-time through our dedicated tracking portal."""):
                        pass
        with SCUI.Accordion.Item(value="item-3"):
            with SCUI.Accordion.Trigger():
                with oj.PD.Prose(text="Return Policy"):
                    pass
            with SCUI.Accordion.Content(classes="flex flex-col gap-4 text-balance"):
                with oj.PD.P():
                    with oj.PD.Prose(text="""We stand behind our products with a comprehensive 30-day return policy.
        If you're not completely satisfied, simply return the item in its
        original condition."""):
                        pass
                with oj.PD.P():
                    with oj.PD.Prose(text="""Our hassle-free return process includes free return shipping and full
        refunds processed within 48 hours of receiving the returned item."""):
                        pass

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="accordion",
                                 childs = [                                           
                                           accordion_box
                                           ],
                                 
                                 title="Accordion",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)
                

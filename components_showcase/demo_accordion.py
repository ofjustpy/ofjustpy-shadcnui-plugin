
import kavya as kv
from py_tailwind_utils import *
from shadcnui_components.dsl import macros, MuCtx
#import shadcnui_components as SCUI
import shadcnui_components as SCUI

with MuCtx:
    with kv.AD.SCUI.divactive.Accordion(type="single", extra_classes="w-full sm:max-w-[70%]", value="item-1") as accordion_box: 
        with SCUI.Accordion.Item(value="item-1"):
            with SCUI.Accordion.Trigger():
                with kv.PD.Prose(text="Product Information"):
                    pass
            with SCUI.Accordion.Content(classes="flex flex-col gap-4 text-balance"):
                with kv.PD.P():
                    with kv.PD.Prose(text="""Our flagship product combines cutting-edge technology with sleek design.
        Built with premium materials, it offers unparalleled performance and
        reliability."""):
                        pass
                with kv.PD.P():
                    with kv.PD.Prose(text="""Key features include advanced processing capabilities, and an intuitive
        user interface designed for both beginners and experts."""):
                        pass
        with SCUI.Accordion.Item(value="item-2"):
            with SCUI.Accordion.Trigger():
                with kv.PD.Prose(text="Shipping Details"):
                    pass
            with SCUI.Accordion.Content(classes="flex flex-col gap-4 text-balance"):
                with kv.PD.P():
                    with kv.PD.Prose(text="""We offer worldwide shipping through trusted courier partners. Standard
        delivery takes 3-5 business days, while express shipping ensures
        delivery within 1-2 business days."""):
                        pass
                with kv.PD.P():
                    with kv.PD.Prose(text="""All orders are carefully packaged and fully insured. Track your shipment
        in real-time through our dedicated tracking portal."""):
                        pass
        with SCUI.Accordion.Item(value="item-3"):
            with SCUI.Accordion.Trigger():
                with kv.PD.Prose(text="Return Policy"):
                    pass
            with SCUI.Accordion.Content(classes="flex flex-col gap-4 text-balance"):
                with kv.PD.P():
                    with kv.PD.Prose(text="""We stand behind our products with a comprehensive 30-day return policy.
        If you're not completely satisfied, simply return the item in its
        original condition."""):
                        pass
                with kv.PD.P():
                    with kv.PD.Prose(text="""Our hassle-free return process includes free return shipping and full
        refunds processed within 48 hours of receiving the returned item."""):
                        pass

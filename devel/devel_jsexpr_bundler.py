import jsexprs.macro_module as mm
from jsexprs.macro_module import macros, writer_ctx
from py_tailwind_utils import *                    

with writer_ctx:
    with ImportVar(module="d3-scale", var_label="scaleUtc") as d3_scale_var:
        pass


    
def on_input_change(dbref, msg, to_ms):
    print("invoked")
    pass


add_new_svelte_component(svelte_code="""
<script lang="ts">
 import CalendarIcon from "@lucide/svelte/icons/calendar";
 import {
  DateFormatter,
  type DateValue,
  getLocalTimeZone
 } from "@internationalized/date";
 import { cn } from "$lib/utils.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 import { Calendar } from "$lib/components/ui/calendar/index.js";
 import * as Popover from "$lib/components/ui/popover/index.js";
 
 const df = new DateFormatter("en-US", {
  dateStyle: "long"
 });
 
 let value = $state<DateValue | undefined>();
 let contentRef = $state<HTMLElement | null>(null);
</script>
 
<Popover.Root>
 <Popover.Trigger
  class={cn(
   buttonVariants({
    variant: "outline",
    class: "w-[280px] justify-start text-left font-normal"
   }),
   !value && "text-muted-foreground"
  )}
 >
  <CalendarIcon />
  {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
 </Popover.Trigger>
 <Popover.Content bind:ref={contentRef} class="w-auto p-0">
  <Calendar type="single" bind:value />
 </Popover.Content>
</Popover.Root>
"""

    )

import ofjustpy as oj
#from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")


slider_box  =  oj.PD.Valign(oj.PD.Halign(SCUI.Slider(key="myslider",
                                                     on_change=on_input_change,
                                                     extra_classes="w-[400px]",  max_=100, step=1),
                                         twsty_tags=[W/screen]),
                           height_tag=H/screen
                        )
        

            
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Slider",
                                 childs = [
                                     slider_box
                                           ],
                                 
                                 title="Slider",
                                 csr_bundle_dir="svelte_bundler",
                                 )
oj.add_jproute("/", wp_endpoint)                    


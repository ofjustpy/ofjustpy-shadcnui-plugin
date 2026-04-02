# <script lang="ts">
#   import { AspectRatio } from "$lib/components/ui/aspect-ratio/index.js";
# </script>
 
# <AspectRatio ratio={16 / 9} class="bg-muted">
#   <img
#     src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
#     alt="Gray by Drew Beamer"
#     class="h-full w-full rounded-md object-cover"
#   />
# </AspectRatio>

import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *


oj.set_style("un")

with writer_ctx:
    with SCUI.AspectRatio(ratio=16/9) as aspectratio_box:
        with oj.PD.Img(src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80", alt="Gray by Drew Beamer",
                       classes="h-full w-full rounded-md object-cover"
                       ):
            
            pass

        pass
            

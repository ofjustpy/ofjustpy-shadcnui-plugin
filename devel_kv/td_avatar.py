import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *


with MuCtx:
    with kv.PD.Div(classes="flex flex-row flex-wrap items-center gap-12") as avatar_box:

        # First Avatar (Standard)
        with kv.AD.SCUI.divactive.Avatar.Root(key="avatar_1"):
            with SCUI.divactive.Avatar.Image(src="https://github.com/shadcn.png", alt="@shadcn"):
                pass
            with SCUI.divactive.Avatar.Fallback():
                with kv.PD.Prose(text="CN"):
                    pass

        # Second Avatar (Rounded-lg Custom Style)
        with kv.AD.SCUI.divactive.Avatar.Root(classes="rounded-lg", key="avatar_2"):
            with SCUI.divactive.Avatar.Image(src="https://github.com/evilrabbit.png", alt="@evilrabbit"):
                pass
            with SCUI.divactive.Avatar.Fallback():
                with kv.PD.Prose(text="ER"):
                    pass

        # Inner Flex Wrapper for Overlapping Group
        with kv.PD.Div(
            extra_classes="*:data-[slot=avatar]:ring-background flex -space-x-2 *:data-[slot=avatar]:ring-2 *:data-[slot=avatar]:grayscale"
        ):
            # Grouped Avatar 1
            with kv.AD.SCUI.divactive.Avatar.Root(key="avatar_3"):
                with SCUI.divactive.Avatar.Image(src="https://github.com/shadcn.png", alt="@shadcn"):
                    pass
                with SCUI.divactive.Avatar.Fallback():
                    with kv.PD.Prose(text="CN"):
                        pass

            # Grouped Avatar 2
            with kv.AD.SCUI.divactive.Avatar.Root(key="avatar_4"):
                with SCUI.divactive.Avatar.Image(src="https://github.com/leerob.png", alt="@leerob"):
                    pass
                with SCUI.divactive.Avatar.Fallback():
                    with kv.PD.Prose(text="LR"):
                        pass

            # Grouped Avatar 3
            with kv.AD.SCUI.divactive.Avatar.Root(key="avatar_5"):
                with SCUI.divactive.Avatar.Image(src="https://github.com/evilrabbit.png", alt="@evilrabbit"):
                    pass
                with SCUI.divactive.Avatar.Fallback():
                    with kv.PD.Prose(text="ER"):
                        pass

wp_endpoint = kv.create_endpoint(key="webpage_mutable_csr",
                                 childs =[avatar_box],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 skeleton_data_theme = "mint",
                                 svelte_bundle_dir="csr",
                                 rendering_type="CSR"
                                 )
app = kv.load_app()
kv.add_route("/", wp_endpoint)                    

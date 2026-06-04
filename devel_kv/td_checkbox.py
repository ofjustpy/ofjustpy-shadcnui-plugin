import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Main column wrapper
    with kv.PD.Div(classes="flex flex-col gap-6 p-8") as checkbox_demo:
        
        # 1. Basic Checkbox with Label
        with kv.PD.Div(classes="flex items-center gap-3"):
            with SCUI.divactive.Checkbox.Root(key="terms"):
                pass
            with SCUI.divactive.Label.Root(key="label_terms"):
                with kv.PD.Prose(text="Accept terms and conditions"):
                    pass

        # 2. Checked Checkbox with Description
        with kv.PD.Div(classes="flex items-start gap-3"):
            with SCUI.divactive.Checkbox.Root(checked=True, key="terms-2"):
                pass 
            with kv.PD.Div(classes="grid gap-2"):
                with SCUI.divactive.Label.Root(key="label_terms_2"):
                    with kv.PD.Prose(text="Accept terms and conditions"):
                        pass
                with kv.PD.P(classes="text-sm", extra_classes="text-muted-foreground"):
                    with kv.PD.Prose(text="By clicking this checkbox, you agree to the terms and conditions."):
                        pass

        # 3. Disabled Checkbox
        with kv.PD.Div(classes="flex items-start gap-3"):
            with SCUI.divactive.Checkbox.Root(disabled=True, key="toggle"):
                pass
            with SCUI.divactive.Label.Root(key="label_toggle"):
                with kv.PD.Prose(text="Enable notifications"):
                    pass
                pass
            

        # 4. Fancy Label Wrapper with State-based styling in extra_classes
        with SCUI.divactive.Label.Root(
            classes=" flex items-start gap-3 rounded-lg border p-3",
            extra_classes="hover:bg-accent/50 has-[[aria-checked=true]]:border-blue-600 has-[[aria-checked=true]]:bg-blue-50 dark:has-[[aria-checked=true]]:border-blue-900 dark:has-[[aria-checked=true]]:bg-blue-950",
            key="label_toggle_2"
        ):
            with SCUI.divactive.Checkbox.Root(
                checked=True,
                key="toggle-2",
                extra_classes="data-[state=checked]:border-blue-600 data-[state=checked]:bg-blue-600 data-[state=checked]:text-white dark:data-[state=checked]:border-blue-700 dark:data-[state=checked]:bg-blue-700"
            ):
                pass
            with kv.PD.Div(classes="grid gap-1.5 font-normal"):
                with kv.PD.P(classes="text-sm leading-none font-medium"):
                    with kv.PD.Prose(text="Enable notifications"):
                        pass
                with kv.PD.P(classes="text-sm", extra_classes="text-muted-foreground"):
                    with kv.PD.Prose(text="You can enable or disable notifications at any time."):
                        pass
                    pass
                pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[checkbox_demo],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

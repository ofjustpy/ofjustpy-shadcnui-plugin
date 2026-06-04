import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

# Assuming CSRC is imported for LucideIcon lookup
import csr_components as CSRC

icon_color = "currentColor"

with MuCtx:
    # Outer layout structure box
    with kv.PD.Div(classes="p-16 flex justify-center items-center w-full") as command_box:

        # Command Root Box
        with kv.AD.SCUI.divactive.Command.Root(classes="rounded-lg border shadow-md ",
                                               extra_classes="md:min-w-[450px]",
                                               key="command_demo"):
            
            # 1. Search Bar / Input field
            with SCUI.divactive.Command.Input(placeholder="Type a command or search...", key="cmd_input"):
                pass
            
            # 2. Results List Wrapper
            with SCUI.divactive.Command.List():
                
                # Fallback Empty State
                with SCUI.divactive.Command.Empty():
                    with kv.PD.Prose(text="No results found."):
                        pass
                
                # --- Group 1: Suggestions ---
                with SCUI.divactive.Command.Group(heading="Suggestions"):
                    
                    # Item: Calendar
                    with SCUI.divactive.Command.Item(key="item_calendar"):
                        with CSRC.LucideIcon(key="li_calendar", label="calendar", width=4, stroke_color=icon_color):
                            pass
                        with kv.PD.Span():
                            with kv.PD.Prose(text="Calendar"):
                                pass
                                
                    # Item: Search Emoji
                    with SCUI.divactive.Command.Item(key="item_emoji"):
                        with CSRC.LucideIcon(key="li_smile", label="smile", width=4, stroke_color=icon_color):
                            pass
                        with kv.PD.Span():
                            with kv.PD.Prose(text="Search Emoji"):
                                pass
                                
                    # Item: Calculator (Disabled)
                    with SCUI.divactive.Command.Item(disabled=True, key="item_calculator"):
                        with CSRC.LucideIcon(key="li_calculator", label="calculator", width=4, stroke_color=icon_color):
                            pass
                        with kv.PD.Span():
                            with kv.PD.Prose(text="Calculator"):
                                pass

                # Content Separator Line
                with SCUI.divactive.Command.Separator():
                    pass

                # --- Group 2: Settings ---
                with SCUI.divactive.Command.Group(heading="Settings"):
                    
                    # Item: Profile
                    with SCUI.divactive.Command.Item(key="item_profile"):
                        with CSRC.LucideIcon(key="li_user", label="user", width=4, stroke_color=icon_color):
                            pass
                        with kv.PD.Span():
                            with kv.PD.Prose(text="Profile"):
                                pass
                        with SCUI.divactive.Command.Shortcut():
                            with kv.PD.Prose(text="⌘P"):
                                pass
                                
                    # Item: Billing
                    with SCUI.divactive.Command.Item(key="item_billing"):
                        with CSRC.LucideIcon(key="li_credit_card", label="credit-card", width=4, stroke_color=icon_color):
                            pass
                        with kv.PD.Span():
                            with kv.PD.Prose(text="Billing"):
                                pass
                        with SCUI.divactive.Command.Shortcut():
                            with kv.PD.Prose(text="⌘B"):
                                pass
                                
                    # Item: Settings
                    with SCUI.divactive.Command.Item(key="item_settings"):
                        with CSRC.LucideIcon(key="li_settings", label="settings", width=4, stroke_color=icon_color):
                            pass
                        with kv.PD.Span():
                            with kv.PD.Prose(text="Settings"):
                                pass
                        with SCUI.divactive.Command.Shortcut():
                            with kv.PD.Prose(text="⌘S"):
                                pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[command_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

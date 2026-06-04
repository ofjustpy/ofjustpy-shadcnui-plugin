import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *

with MuCtx:
    # Outer layout container
    with kv.PD.Div(classes="p-16 flex justify-center items-center w-full") as contextmenu_box:

        # Context Menu Root Container
        with SCUI.divactive.ContextMenu.Root(key="ctx_menu_demo"):
            
            # Context Menu Area Trigger
            with SCUI.divactive.ContextMenu.Trigger(
                classes="flex items-center justify-center rounded-md border border-dashed text-sm",
                extra_classes="h-[150px] w-[300px]",
                key="ctx_trigger"
            ):
                with kv.PD.Prose(text="Right click here"):
                    pass

            # Context Menu Content Window
            with SCUI.divactive.ContextMenu.Content(classes="w-52"):
                
                # --- Standard Menu Items ---
                with SCUI.divactive.ContextMenu.Item(inset=True, key="item_back"):
                    with kv.PD.Prose(text="Back"):
                        pass
                    with SCUI.divactive.ContextMenu.Shortcut():
                        with kv.PD.Prose(text="⌘["):
                            pass

                with SCUI.divactive.ContextMenu.Item(inset=True, disabled=True, key="item_forward"):
                    with kv.PD.Prose(text="Forward"):
                        pass
                    with SCUI.divactive.ContextMenu.Shortcut():
                        with kv.PD.Prose(text="⌘]"):
                            pass

                with SCUI.divactive.ContextMenu.Item(inset=True, key="item_reload"):
                    with kv.PD.Prose(text="Reload"):
                        pass
                    with SCUI.divactive.ContextMenu.Shortcut():
                        with kv.PD.Prose(text="⌘R"):
                            pass

                # --- Sub Menu Cascade ---
                with SCUI.divactive.ContextMenu.Sub():
                    with SCUI.divactive.ContextMenu.SubTrigger(inset=True, key="sub_trigger_tools"):
                        with kv.PD.Prose(text="More Tools"):
                            pass
                    
                    with SCUI.divactive.ContextMenu.SubContent(classes="w-48"):
                        with SCUI.divactive.ContextMenu.Item(key="sub_item_save"):
                            with kv.PD.Prose(text="Save Page As..."):
                                pass
                            with SCUI.divactive.ContextMenu.Shortcut():
                                with kv.PD.Prose(text="⇧⌘S"):
                                    pass
                        
                        with SCUI.divactive.ContextMenu.Item(key="sub_item_shortcut"):
                            with kv.PD.Prose(text="Create Shortcut..."):
                                pass
                                
                        with SCUI.divactive.ContextMenu.Item(key="sub_item_name_win"):
                            with kv.PD.Prose(text="Name Window..."):
                                pass
                        
                        with SCUI.divactive.ContextMenu.Separator():
                            pass
                            
                        with SCUI.divactive.ContextMenu.Item(key="sub_item_dev_tools"):
                            with kv.PD.Prose(text="Developer Tools"):
                                pass

                with SCUI.divactive.ContextMenu.Separator():
                    pass

                # --- Checkbox Toggles ---
                with SCUI.divactive.ContextMenu.CheckboxItem(checked=False, key="ctx_cb_bookmarks"):
                    with kv.PD.Prose(text="Show Bookmarks"):
                        pass

                with SCUI.divactive.ContextMenu.CheckboxItem(checked=True, key="ctx_cb_urls"):
                    with kv.PD.Prose(text="Show Full URLs"):
                        pass

                with SCUI.divactive.ContextMenu.Separator():
                    pass

                # --- Radio Group Items ---
                with SCUI.divactive.ContextMenu.RadioGroup(value="pedro", key="ctx_radio_people"):
                    with SCUI.divactive.ContextMenu.Group():
                        with SCUI.divactive.ContextMenu.GroupHeading(inset=True):
                            with kv.PD.Prose(text="People"):
                                pass
                        
                        with SCUI.divactive.ContextMenu.RadioItem(value="pedro", key="radio_pedro"):
                            with kv.PD.Prose(text="Pedro Duarte"):
                                pass
                                
                        with SCUI.divactive.ContextMenu.RadioItem(value="colm", key="radio_colm"):
                            with kv.PD.Prose(text="Colm Tuite"):
                                pass


wp_endpoint = kv.create_endpoint(
    key="webpage_mutable_csr",
    childs=[contextmenu_box],
    skeleton_data_theme="mint",
    svelte_bundle_dir="csr",
    rendering_type="CSR"
)

app = kv.load_app()
kv.add_route("/", wp_endpoint)

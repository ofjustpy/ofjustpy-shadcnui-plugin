import kavya as kv
from shadcnui_components.dsl import macros, MuCtx
import shadcnui_components as SCUI
from py_tailwind_utils import *



kv.set_style("un")
with MuCtx:
    with kv.AD.SCUI.divactive.AlertDialog.Root(key="alert_dialog_1") as alert_dialog_box:
        # Trigger Button
        with kv.AD.SCUI.divactive.AlertDialog.Trigger(variant="outline"):
            with kv.PD.Prose(text="Show Dialog"):
                pass

        # Content Slot
        with SCUI.divactive.AlertDialog.Content():

            # Header Layout Block
            with SCUI.divactive.AlertDialog.Header():
                with SCUI.divactive.AlertDialog.Title():
                    with kv.PD.Prose(text="Are you absolutely sure?"):
                        pass

                with SCUI.divactive.AlertDialog.Description():
                    with kv.PD.Prose(
                        text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."
                    ):
                        pass

            # Footer Layout Block
            with SCUI.divactive.AlertDialog.Footer():
                with SCUI.divactive.AlertDialog.Cancel():
                    with kv.PD.Prose(text="Cancel"):
                        pass

                with SCUI.divactive.AlertDialog.Action():
                    with kv.PD.Prose(text="Continue"):
                        pass



wp_endpoint = kv.create_endpoint(key="webpage_mutable_csr",
                                 childs =[alert_dialog_box],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 skeleton_data_theme = "mint",
                                 svelte_bundle_dir="csr",
                                 rendering_type="CSR"
                                 )
app = kv.load_app()
kv.add_route("/", wp_endpoint)


# class ParentDummy:
#     def add_component(*args, **kwargs):
#         pass
#     pass

# parent_dummy = ParentDummy()

# alert_linked = alert.stub()(parent_dummy)
#print("".join(alert_linked.convert_object_to_json()))

# with MuCtx:
#     with SCUI.Alert.Root(key="alert_1"):
#         pass
    
    


# with MuCtx:
#     with SCUI.Alert.Root() as alert_box:
#         with SCUI.Alert.Title():
#             with oj.PD.Prose(text="Heads up!"):
#                 pass
#             pass

#         with SCUI.Alert.Description():
#             with oj.PD.Prose(text="You can add components to your app using the cli."):
#                 pass
                

import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
oj.set_style("un")

# with writer_ctx:
#     with SCUI.ScrollArea(classes="w-32 h-16", orientation="both") as scrollarea_box:
#         with oj.PD.Prose(twtags_tags=W/"400px", text="Jokester began sneaking into the castle in the middle of the night and leaving jokes all over the place: under the king's pillow, in his soup, even    in the royal toilet. The king was furious, but he couldn't seem to stop Jokester. And then, one day, the people of the kingdom discovered that the jokes left by Jokester were so funny that they couldn't help but laugh. And    once they started laughing, they couldn't stop."):

        
#             pass
#     pass



# with writer_ctx:
#     # Define 'tags' list for the example, as it's used in a loop
#     tags = ["@radix-ui/primitives", "@lucide/lucide", "@sveltejs/svelte", "shadcn/ui"]

#     with SCUI.ScrollArea(classes="h-72 w-48 rounded-md border") as scrollarea_box:
#         with oj.PD.Div(classes="p-4"):
#             with oj.PD.H4(classes="mb-4 text-sm font-medium leading-none"):
#                 with oj.PD.Prose(text="Tags"):
#                     pass
#             for tag in tags:
#                 with oj.PD.Div(classes="text-sm"):
#                     with oj.PD.Prose(text=tag):
#                         pass
#                 with SCUI.Separator(classes="my-2"):
#                     pass

# tags = ["@radix-ui/primitives", "@lucide/lucide", "@sveltejs/svelte", "shadcn/ui"]
# with writer_ctx:
#     # Define 'tags' list for the example, as it's used in a loop


#     with SCUI.ScrollArea(classes="h-72 w-48 rounded-md border") as scrollarea_box:
#         with oj.PD.Div(classes="p-4"):
#             with oj.PD.H4(classes="mb-4 text-sm font-medium leading-none"):
#                 with oj.PD.Prose(text="Tags"):
#                     pass
#             # Replaced the for loop with explicit declarations
#             with oj.PD.Div(classes="text-sm"):
#                 with oj.PD.Prose(text=tags[0]):
#                     pass
#             with SCUI.Separator(classes="my-2"):
#                 pass
#             with oj.PD.Div(classes="text-sm"):
#                 with oj.PD.Prose(text=tags[1]):
#                     pass
#             with SCUI.Separator(classes="my-2"):
#                 pass
#             with oj.PD.Div(classes="text-sm"):
#                 with oj.PD.Prose(text=tags[2]):
#                     pass
#             with SCUI.Separator(classes="my-2"):
#                 pass
#             with oj.PD.Div(classes="text-sm"):
#                 with oj.PD.Prose(text=tags[3]):
#                     pass
#             with SCUI.Separator(classes="my-2"): # Added for the last item as well
#                 pass

# Define the artwork data
works = [
    {
        "artist": "Ornella Binni",
        "art": "https://images.unsplash.com/photo-1465869185982-5a1a7522cbcb?auto=format&fit=crop&w=300&q=80"
    },
    {
        "artist": "Tom Byrom",
        "art": "https://images.unsplash.com/photo-1548516173-3cabfa4607e9?auto=format&fit=crop&w=300&q=80"
    },
    {
        "artist": "Vladimir Malyavko",
        "art": "https://images.unsplash.com/photo-1494337480532-3725c85fd2ab?auto=format&fit=crop&w=300&q=80"
    }
]


with writer_ctx:
    with SCUI.ScrollArea(classes="w-96 whitespace-nowrap rounded-md border", orientation="horizontal") as scrollarea_box:
        with oj.PD.Div(classes="flex w-max space-x-4 p-4"):
            # First artwork
            with oj.PD.Figure(classes="shrink-0"):
                with oj.PD.Div(classes="overflow-hidden rounded-md"):
                    with oj.PD.Img(
                        src=works[0]["art"],
                        alt=f"Photo by {works[0]['artist']}",
                        extra_classes="aspect-[3/4] h-fit w-fit object-cover",
                        width=300,
                        height=400
                    ):
                        pass
                with oj.PD.Figcaption(extra_classes="text-muted-foreground pt-2 text-xs"):
                    with oj.PD.Prose(text="Photo by "):
                        pass
                    with oj.PD.Span(classes="text-foreground font-semibold"):
                        with oj.PD.Prose(text=works[0]["artist"]):
                            pass
            # Second artwork
            with oj.PD.Figure(classes="shrink-0"):
                with oj.PD.Div(classes="overflow-hidden rounded-md"):
                    with oj.PD.Img(
                        src=works[1]["art"],
                        alt=f"Photo by {works[1]['artist']}",
                        extra_classes="aspect-[3/4] h-fit w-fit object-cover",
                        width=300,
                        height=400
                    ):
                        pass
                with oj.PD.Figcaption(extra_classes="text-muted-foreground pt-2 text-xs"):
                    with oj.PD.Prose(text="Photo by "):
                        pass
                    with oj.PD.Span(classes="text-foreground font-semibold"):
                        with oj.PD.Prose(text=works[1]["artist"]):
                            pass
            # Third artwork
            with oj.PD.Figure(classes="shrink-0"):
                with oj.PD.Div(classes="overflow-hidden rounded-md"):
                    with oj.PD.Img(
                        src=works[2]["art"],
                        alt=f"Photo by {works[2]['artist']}",
                        extra_classes="aspect-[3/4] h-fit w-fit object-cover",
                        width=300,
                        height=400
                    ):
                        pass
                with oj.PD.Figcaption(extra_classes="text-muted-foreground pt-2 text-xs"):
                    with oj.PD.Prose(text="Photo by "):
                        pass
                    with oj.PD.Span(classes="text-foreground font-semibold"):
                        with oj.PD.Prose(text=works[2]["artist"]):
                            pass


with writer_ctx:
    with SCUI.ScrollArea(extra_classes="h-[200px] w-[350px] rounded-md border p-4", orientation="both") as scrollarea_box_both_orientation:
        with oj.PD.Div(extra_classes="w-[400px]"):
            with oj.PD.Prose(text="""Jokester began sneaking into the castle in the middle of the night and
    leaving jokes all over the place: under the king's pillow, in his soup, even
    in the royal toilet. The king was furious, but he couldn't seem to stop
    Jokester. And then, one day, the people of the kingdom discovered that the
    jokes left by Jokester were so funny that they couldn't help but laugh. And
    once they started laughing, they couldn't stop."""):
                pass
            
                    
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="ScrollArea",
                                 childs = [
                                     scrollarea_box,
                                     scrollarea_box_both_orientation
                                           ],
                                 
                                 title="ScrollArea",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                    
                    


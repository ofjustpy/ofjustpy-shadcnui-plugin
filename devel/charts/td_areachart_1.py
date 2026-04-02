import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
import layerchart_components as LCUI
from py_tailwind_utils import *
from ofjustpy.icons import LucideIcon
from datetime import date

# Set the UI style
oj.set_style("un")

# 1. Define the chart data, similar to the Svelte example
# The dates are Python date objects.
chart_data = [
    {"date": date(2024, 1, 1), "desktop": 186},
    {"date": date(2024, 2, 1), "desktop": 305},
    {"date": date(2024, 3, 1), "desktop": 237},
    {"date": date(2024, 4, 1), "desktop": 73},
    {"date": date(2024, 5, 1), "desktop": 209},
    {"date": date(2024, 6, 1), "desktop": 214},
]

# 2. Define the chart configuration
chart_config = {
    "desktop": {"label": "Desktop", "color": "var(--chart-1)"},
}

# 3. Define the series data for the chart
# This tells the chart which keys from the data to use.
series = [
    {
        "key": "desktop",
        "label": "Desktop",
        "color": chart_config["desktop"]["color"],
    }
]

# 4. Define properties for chart rendering and formatting
# This corresponds to the `props` in the Svelte example.
# Note: Formatting functions are represented as strings that the frontend can interpret.
chart_props = {
    "area": {
        "curve": "curveNatural",  # Use d3-shape curve function by name
        "fill-opacity": 0.4,
        "line": {"class": "stroke-1"},
        "motion": "tween",
    },
    "xAxis": {
        # Format date object to show the short month name (e.g., "Jan")
        "format": "lambda v: new Date(v).toLocaleDateString('en-US', { month: 'short' })",
    },
}


# 5. Build the UI using the writer context
with writer_ctx:
    with SCUI.Card.Root(classes="w-full max-w-2xl") as card_box:
        with SCUI.Card.Header():
            with SCUI.Card.Title():
                with oj.PD.Prose(text="Area Chart"):
                    pass
            with SCUI.Card.Description():
                with oj.PD.Prose(text="Showing total visitors for the last 6 months"):
                    pass
        with SCUI.Card.Content(classes="p-0"):
            with SCUI.Chart.Container(config=chart_config, extra_classes="h-[200px]",
                                      classes="w-full"):
                # Create the AreaChart component with data and configuration
                with LCUI.AreaChart(
                        data=JSGlobalVar("chart_data"),
                    x="date",
                        #xScale="scaleUtc",  # Specify the scale type for dates
                    #series=series,
                    axis="x",
                    #props=chart_props,
                ) as area_chart:
                    # Define the tooltip within the chart's context
                    # with SCUI.Chart.Tooltip(
                    #     labelFormatter="lambda v: new Date(v).toLocaleDateString('en-US', { month: 'long' })",
                    #     indicator="line",
                    # ):
                    #     pass
                    pass
                pass
        with SCUI.Card.Footer():
            with oj.PD.Div(classes="flex w-full items-start gap-2 text-sm"):
                with oj.PD.Div(classes="grid gap-2"):
                    with oj.PD.Div(classes="flex items-center gap-2 font-medium leading-none"):
                        with oj.PD.Prose(text="Trending up by 5.2% this month"):
                            pass
                        # Use LucideIcon for the trending-up icon
                        with LucideIcon(icon="trending-up", classes="size-4"):
                            pass
                    with oj.PD.Div(extra_classes="text-muted-foreground", 
                        classes="flex items-center gap-2 leading-none"
                    ):
                        with oj.PD.Prose(text="January - June 2024"):
                            pass

# Create the web page endpoint
app = oj.load_app()
webpage = oj.create_endpoint(
    "demo",
    childs=[
        oj.PC.Div(
            childs=[card_box],
            classes="flex h-screen w-full items-center justify-center",
        )
    ],
    title="Area Chart Example",
    csr_bundle_dir="skeleton_shadcn_uibundle",
    head_html = """<script src="/static/dummy_utils.js"></script>"""


)
oj.add_jproute("/", webpage)

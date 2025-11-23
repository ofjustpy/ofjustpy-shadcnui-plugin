import ofjustpy as oj
from shadcnui_components.dsl import macros, writer_ctx
import shadcnui_components as SCUI
import layerchart_components as LCUI
from py_tailwind_utils import *
from datetime import datetime
oj.set_style("un")

chart_config = """{
    desktop: { label: "Desktop", color: "var(--chart-1)" },
  }"""


chart_config = """{
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
}"""

chartConfig = """{
    desktop: {
      label: "Desktop",
      color: "#2563eb"
    },
    mobile: {
      label: "Mobile",
      color: "#60a5fa"
    }
  }""";

  
# chartData = [
#     { month: "January", desktop: 186, mobile: 80 },
#     { month: "February", desktop: 305, mobile: 200 },
#     { month: "March", desktop: 237, mobile: 120 },
#     { month: "April", desktop: 73, mobile: 190 },
#     { month: "May", desktop: 209, mobile: 130 },
#     { month: "June", desktop: 214, mobile: 140 }
#   ]
chart_data = [
    {"month": "January", "desktop": 186, "mobile": 80},
    {"month": "February", "desktop": 305, "mobile": 200},
    {"month": "March", "desktop": 237, "mobile": 120},
    {"month": "April", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "June", "desktop": 214, "mobile": 140},
]

# chartData = [
#     {"date": datetime(2023, 1, 1), "desktop": 100, "mobile": 50},
#     {"date": datetime(2023, 2, 1), "desktop": 120, "mobile": 60},
#     {"date": datetime(2023, 3, 1), "desktop": 90, "mobile": 45},
#     {"date": datetime(2023, 4, 1), "desktop": 150, "mobile": 75},
# ]

# 1. Define a sample chart_config dictionary for the example to work.
chart_config = {
    "desktop": {
        "label": "Desktop",
        "color": "hsl(210, 40%, 96.1%)"  # Example color
    },
    "mobile": {
        "label": "Mobile",
        "color": "hsl(346.8, 77.2%, 49.8%)" # Example color
    }
}

# 2. Here is the converted Python dictionary.
# It's a dictionary containing one key, "series", whose value is a list of other dictionaries.
series = [
        {
            "key": "desktop",
            "label": "Desktop",
            "color": "hsl(210, 40%, 96.1%)"
        },
        {
            "key": "mobile",
            "label": "Mobile",
            "color": "hsl(346.8, 77.2%, 49.8%)" # Example color
        }
    ]



    
with writer_ctx:
    with SCUI.Chart.Container(config=chart_config) as chart_box:
        with LCUI.BarChart(#data=chart_data,
                x="month",
                axis="x",
                    seriesLayout="group",
                    series = series,
                    data=chart_data
                            ):
            pass
        
        pass
                

    
# with writer_ctx:
#     with SCUI.Chart.Container(config=chart_config) as chart_box:
#         with LCUI.AreaChart(data=chartData,
#                             x="date",
#                             series=[
#                                 {
#                                     "key": "desktop",
#                                     "label": "Desktop",
#                                     "color": "var(--chart-1)"
#                                 },
#                             ],
#                             axis="x",
#                             props={
#                                 "area": {
#                                     "curve": LCUI.D3.curveNatural,
#                                     "fill-opacity": 0.4,
#                                     "line": {"class": "stroke-1"},
#                                     "motion": "tween",
#                                 },
#                                 "xAxis": {
#                                     "format": LCUI.JSExpr("""(v: Date) => v.toLocaleDateString("en-US", { month: "short" })"""), # Pass the Python function here
#                                 },
#                             }):
#             pass
        
#         pass
                

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="Chart",
                                 childs = [
                                     chart_box
                                           ],
                                 
                                 title="Chart",
                                 csr_bundle_dir="skeleton_shadcn_uibundle",
                                 )
oj.add_jproute("/", wp_endpoint)                                                        

import   jsexprs
import shadcnui_components as SCUI
import layerchart_components as LCUI
from shadcnui_components.dsl import macros, writer_ctx

import ofjustpy as oj
oj.set_style("un")
curve_natural = jsexprs.JSVar("d3-shape", "curveNatural")


with writer_ctx:
    with SCUI.Chart.Container() as chart_box:
        with LCUI.AreaChart(
                props = {
    
                    "area": {
                        "curve": curve_natural,
                        "fill-opacity": 0.4,
                        "line": { "class": "stroke-1" },
                        "motion": "tween",
                    },
                    
                }
                            ):
            pass
        
        pass
                

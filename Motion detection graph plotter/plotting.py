from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

coldatasrc = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_both', title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(
    tooltips=[
        ("Start", "@Start{%Y-%m-%d %H:%M:%S}"),
        ("End", "@End{%Y-%m-%d %H:%M:%S}")
    ],
    formatters={
        "@Start": "datetime",
        "@End": "datetime"
    }
)
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color='green', source=coldatasrc)

output_file("Graph1.html")

show(p)

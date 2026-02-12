from shiny import App, ui

# app_ui = ui.page_fillable(
#     ui.layout_columns(
#         ui.card("Summary of Crime Statistics in Vancouver"),
#         ui.card("Distribution of Crime Types in Vancouver"),
#         ui.card("Crime Severity Rate Across Neighborhoods in Vancouver"),
#         col_widths=(2, 4, 6),
#     ),
# )

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("neighbourhood", "Neighbourhood",
            ["All", "Milestone 1", "Milestone 2"]),
        ui.input_select("crime_type", "Crime Type",
            ["All teams", "Team 01", "Team 02"]),
        ui.input_select("month", "Month",
            ["All", "January", "February", "March", "April", "May"]),
    ),
    ui.layout_columns(
        ui.value_box("Reported Incidents", "259"),
        ui.value_box("Crime Rate", "9%"),
        ui.value_box("Average Comparison", "2%"),
        ui.value_box("MoM Change", "4%"),
        fill=False,
    ),
    ui.layout_columns(
        ui.card(ui.card_header("Crime Map by Neigbourhood"), full_screen=True),
        ui.card(ui.card_header("Count of Crime Type"), full_screen=True),
        col_widths=[7, 5],
    ),
    title="Team Activity Tracker", fillable=True,
)





def server(input, output, session):
    pass


app = App(app_ui, server=server)
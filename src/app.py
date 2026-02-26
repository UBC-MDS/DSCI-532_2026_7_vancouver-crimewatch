from shiny import App, ui, reactive, render
import pandas as pd

crime_df = pd.read_csv("data/processed/processed_vancouver_crime_data_2025.csv")
population_df = pd.read_csv("data/raw/van_pop_2016.csv")

# Input options for the dropdowns
neighbourhoods = ["All"] + sorted(crime_df["NEIGHBOURHOOD"].unique())
crime_types = ["All"] + sorted(crime_df["TYPE"].unique())
months = ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
time_of_day = ["All", "Morning", "Afternoon", "Evening"]

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("nb", "Neighbourhood",
            neighbourhoods),
        ui.input_select("crime_type", "Crime Type",
            crime_types),
        ui.input_select("month", "Month",
            months),
        ui.input_select("daily_time", "Time of Day",
            time_of_day),
        full_screen=True
    ),
    ui.layout_columns(
        ui.value_box("Reported Incidents", ui.output_text("crime_count")),
        ui.value_box("Crime Rate", "9%"),
        ui.value_box("Average Comparison", "2%"),
        ui.value_box("MoM Change", "4%"),
        fill=False,
    ),
    ui.layout_columns(
        ui.card(
            ui.card_header(ui.strong("Crime Map by Neigbourhood")), 
            full_screen=True
            ),
        ui.layout_columns(
            ui.card(
                ui.card_header(ui.strong("Count of Crime Type")), 
                full_screen=True,
                ),
            ui.card(
                ui.card_header(ui.strong("Crime by Time of Day")), 
                full_screen=True,
                ),
            col_widths=[12,12],
            fill=True
        ),
        col_widths=[7, 5],
        ),
    title=ui.tags.h2("Vancouver Neighbourhood Safety", style="font-weight: bold;"), fillable=True,
)

def server(input, output, session):
    @reactive.calc
    def filtered_data():
        nb = input.nb()
        crime_type = input.crime_type()
        month = input.month()
        daily_time = input.daily_time()
        df = crime_df.copy()
        if nb != "All":
            df = df[df["NEIGHBOURHOOD"] == nb]
        if crime_type != "All":
            df = df[df["TYPE"] == crime_type]
        if month != "All":
            df = df[df["MONTH_NAME"] == month]
        if daily_time != "All":
            df = df[df["TIME_OF_DAY"] == daily_time]
        return df
    
    @render.text
    def crime_count():
        return str(len(filtered_data()))

app = App(app_ui, server=server)

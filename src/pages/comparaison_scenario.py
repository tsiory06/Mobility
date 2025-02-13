from dash import dcc, Dash, html
import dash_bootstrap_components as dbc

from src.components.comparaison_scenario.scenario_header import create_header_scenario
def scenario():
    return dbc.Container([
        html.Div(create_header_scenario()),
        html.Div(id='dynamic-content-comparaison_scenario'),  # Conteneur pour le contenu dynamique
    ], fluid=True, className="container-custom")



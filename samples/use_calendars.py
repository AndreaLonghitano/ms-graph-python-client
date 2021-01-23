from pprint import pprint

from ms_graph.client import MicrosoftGraphClient
from configparser import ConfigParser


scopes = [
    'Calendars.ReadWrite'
]

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('configs/config.ini')

# Get the specified credentials.
client_id = config.get('graph_api', 'client_id')
client_secret = config.get('graph_api', 'client_secret')
redirect_uri = config.get('graph_api', 'redirect_uri')

# Initialize the Client.
graph_client = MicrosoftGraphClient(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scopes,
    credentials='configs/ms_graph_state.jsonc'
)

# Login to the Client.
graph_client.login()

# Grab the Event Object.
calendar_object = graph_client.calendar()


pprint(calendar_object.get_all_calendars())
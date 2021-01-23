from pprint import pprint



from ms_graph.client import MicrosoftGraphClient
from configparser import ConfigParser


scopes = [
    'Mail.Read',
    'Mail.Read.Shared',
    'Mail.ReadBasic',
    'Mail.ReadWrite',
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

# Grab the Drive Services.
mail_services = graph_client.mail()

# List the Root Drive.
 #pprint(mail_services.list_my_messages())

pprint(mail_services.get_important_messages())

mail_services.send_my_mail(message_id=None)
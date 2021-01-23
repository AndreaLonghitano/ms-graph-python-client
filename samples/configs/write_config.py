from configparser import ConfigParser
import yaml


with open(file = 'credentials.yaml', mode='r') as f:
    credentials = yaml.safe_load(f)

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section('graph_api')

# Set the Values.
config.set('graph_api', 'client_id', credentials['client_id'])
config.set('graph_api', 'client_secret', credentials['client_secret'])
config.set('graph_api', 'redirect_uri', credentials['redirect_uri'])

# Write the file.
with open(file='samples/configs/config.ini', mode='w+') as f:
    config.write(f)

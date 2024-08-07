from temba_client.v2 import TembaClient
import os

client = TembaClient('rapidpro.io', os.environ.get('API_TOKEN'))
for contact_batch in client.get_contacts(group='Reporters').iterfetches(retry_on_rate_exceed=True):
    for contact in contact_batch:
        print(contact.name)

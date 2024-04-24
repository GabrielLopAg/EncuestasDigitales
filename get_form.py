# form_id: 1GEsjWKisZGbfpLPsnhQ7Wdx6IdkU706cC6k3sNVClKw
from pprint import pprint
from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json',
    SCOPES
)

http=creds.authorize(Http())

form_service = discovery.build(
    "forms",
    "v1",
    http=http,
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)

formId = "1GEsjWKisZGbfpLPsnhQ7Wdx6IdkU706cC6k3sNVClKw"

# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=formId).execute()
pprint(get_result)
print('\n')
#pprint(get_result['items'])
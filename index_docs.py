from io import open
from json.decoder import JSONDecoder
# install elastic_workplace_search package
try:
    from elastic_workplace_search import Client
except ImportError as e:
    pass  # module not installed, fix that
    print("Error {}, installing".format(e))
    import pip
    pip.main(['install', 'elastic_workplace_search', '--upgrade'])
    from elastic_workplace_search import Client

# Create a deployment of Elastic Enterprise Search
# https://cloud.elastic.co/deployments/create
#
# Choose Workplace Search
# From Elastic Cloud Workplace Search Setup =>
# copy Enterprise Search API endpoint (remove '/login' if present)
enterprise_search_endpoint = ''

# From the Workplace Search Deployment =>
# From Create Custom Source Dialogue =>
# copy Custom API Source Access Token
custom_api_source_access_token = ''
# copy Custom API Source Access Key
custom_api_source_key = ''

# create a Client to access the service
client = Client(custom_api_source_access_token,
                enterprise_search_endpoint + "/api/ws/v1")

# Custom Source Documents
# An Array of Documents as JSON Key/Value pairs
file = "video_games.json"
with open(file,"r") as docs:
    print("Document indexing results {}".format(
        client.documents.index_documents(custom_api_source_key,
                                         JSONDecoder().decode(docs.read())['docs'])))

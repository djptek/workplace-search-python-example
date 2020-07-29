# Create a deployment of Elastic Enterprise Search
# https://cloud.elastic.co/deployments/create
#
# Choose Workplace Search
# From Elastic Cloud Workplace Search Setup =>
# copy Enterprise Search API endpoint
enterprise_search_endpoint = ''

# From the Workplace Search Deployment =>
# From Create Custom Source Dialogue =>
# copy Custom API Source Access Token
custom_api_source_access_token = ''
# copy Custom API Source Access Key
custom_api_source_key = ''

# install elastic_workplace_search package
try:
    from elastic_workplace_search import Client
except ImportError as e:
    pass  # module not installed, fix that
    print("Error {}, installing".format(e))
    import pip
    pip.main(['install', 'elastic_workplace_search', '--upgrade'])
    from elastic_workplace_search import Client

# create a Client to access the service
client = Client(custom_api_source_access_token,
                enterprise_search_endpoint + "/api/ws/v1")

# Custom Source Documents
# An Array of Documents as JSON Key/Value pairs
documents = [
    {
        'url':
            'https://github.com/elastic/workplace-search-python#getting-started-',
        'title':
            'Getting started',
        'body':
            """Supports Python 2.7 and Python 3.4+.
        Installed with pip <http://pypi.python.org/pypi/pip>:
        $ python -m pip install elastic_workplace_search
        You can also download and install the project source:
        $ python setup.py install
        Depends on requests for making HTTP requests."""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#creating-a-new-client',
        'title':
            'Creating a new Client',
        'body':
            """Creating a new Client
  from elastic_workplace_search import Client
  authorization_token = 'authorization token'
  client = Client(authorization_token)
Retrieve your access token and a content source key after creating your content source."""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#change-api-endpoint',
        'title':
            'Change API endpoint',
        'body':
            """client = Client(authorization_token, "https://your-server.example.com/api/ws/v1")"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#custom-source-documents',
        'title':
            'Custom Source Documents',
        'body':
            """Document API features are found in the client.documents module."""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#deleting-documents',
        'title':
            'Deleting Documents',
        'body':
            """Deleting a document from a custom content source:

  content_source_key = 'content source key'
  ids = ['1234']

  client.documents.delete_documents(content_source_key, ids)"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#permissions',
        'title':
            'Permissions',
        'body':
            """Permissions API features are found in the client.permissions module."""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#listing-all-permissions',
        'title':
            'Listing all permissions',
        'body':
            """content_source_key = 'content source key'

client.permissions.list_all_permissions(content_source_key)
"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#creating-a-new-client',
        'title':
            'Creating a new Client',
        'body':
            """."""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#listing-all-permissions-with-paging',
        'title':
            'Listing all permissions with paging',
        'body':
            """content_source_key = 'content source key'

client.permissions.list_all_permissions(content_source_key, size=20, current=2)"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#retrieve-a-users-permissions',
        'title':
            'Retrieve a User\'s permissions',
        'body':
            """content_source_key = 'content source key'
user = 'enterprise_search'

client.permissions.get_user_permissions(content_source_key, user)"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#add-permissions-to-a-user',
        'title':
            'Add permissions to a User',
        'body':
            """content_source_key = 'content source key'
user = 'enterprise_search'
permissions = ['permission1']

client.permissions.add_user_permissions(content_source_key, 'enterprise_search', { 'permissions': permissions })"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#update-a-users-permissions',
        'title':
            'Update a User\'s permissions',
        'body':
            """content_source_key = 'content source key'
user = 'enterprise_search'
permissions = ['permission2']

client.permissions.update_user_permissions(content_source_key, 'enterprise_search', { 'permissions': permissions })
"""
    },
    {
        'url':
            'https://github.com/elastic/workplace-search-python#remove-permissions-from-a-user',
        'title':
            'Remove permissions from a User',
        'body':
            """content_source_key = 'content source key'
user = 'enterprise_search'
permissions = ['permission2']

client.permissions.remove_user_permissions(content_source_key, 'enterprise_search', { 'permissions': permissions })
"""
    }
]

print("Document indexing results {}".format(
    client.documents.index_documents(custom_api_source_key, documents)))
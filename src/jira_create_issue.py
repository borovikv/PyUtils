import requests


JIRA_PROJECT_KEY = 'abc'


def get_jira_auth():
    return 'login', 'password'


response = requests.post(
    'https://datalabmd.atlassian.net/rest/api/2/issue/',
    json={
        'fields': dict(
            project={
                'key': JIRA_PROJECT_KEY
            }, summary='abc',
            description="Creating of an issue using project keys and issue type names using the REST API",
            issuetype={
                "name": "Bug"
            })
    },
    auth=get_jira_auth()
)

print(response)

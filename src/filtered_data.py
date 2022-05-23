import api
from _globals import *

def get_filtered_data(team_lead=False, teamlead_id=None):
    '''
    [1:] -- Removes first character from string
    [:-1] -- Removes last character from string
    '''
    url_build = ""
    client_id = ""
    project_id = ""
    status_id = ""
    _dept = ""
    if G_CLIENTS_ID_LIST:
        for client in G_CLIENTS_ID_LIST:
            client_id = client_id + str(client) + '|'
        url_build = url_build + '&client_id=' + client_id[:-1]
    if G_PROJECTS_ID_LIST:
        for project in G_PROJECTS_ID_LIST:
            project_id = project_id + str(project) + '|'
        url_build = url_build + '&project_id=' + project_id[:-1]
    if G_STATUS_ID_LIST:
        for status in G_STATUS_ID_LIST:
            status_id = status_id + str(status) + '|'
        url_build = url_build + '&status=' + status_id[:-1]
    if G_CLIENTS_ID_LIST or G_PROJECTS_ID_LIST or G_STATUS_ID_LIST:
        if G_DEPARTMENT_LIST:
            for dept in G_DEPARTMENT_LIST:
                _dept = _dept + str(dept) + '|'
            url_build = url_build + '&dept=' + _dept[:-1]

    if team_lead:
        if G_CLIENTS_ID_LIST or G_PROJECTS_ID_LIST or G_STATUS_ID_LIST:
            url_build = url_build +'&lead='+ str(teamlead_id)
        _team_data = api.get_leads_data(url_build[1:])
        _final_data = []
        for _tdata in _team_data:
            _final_data.append(_tdata['shot'])
        _data = _final_data
    else:
        _data = api.get_shots_data(url_build[1:])
    return _data
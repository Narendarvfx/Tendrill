import configparser
import time

import requests
import urllib3

urllib3.disable_warnings()
config = configparser.ConfigParser()
# TODO: Change config file location while building
config.read(r'D:\Repo_Settings\settings.ini')

base_url = "{}{}".format(config['API']['hostname'], config['API']['port'])
token = config['API']['token']

session = requests.Session()

def getUserById(userId):
    userUrl = base_url + "/api/users/" + userId
    user_data = session.get(userUrl, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return user_data.json()

def get_all_employees():
    employee_url = base_url + "/api/hrm/employee/"
    employee_data = session.get(employee_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return employee_data.json()

def get_employees_by_status(status=None):
    if status is not None:
        employee_url = base_url + "/api/hrm/employee/?status=" + status
    else:
        employee_url = base_url + "/api/hrm/employee/"
    employee_data = session.get(employee_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return employee_data.json()

def get_employees_by_dept(dept=None, role=None):
    if dept is not None and role is not None:
        employee_url = base_url + "/api/hrm/employee/?dept=" + dept + "&role=" + role
    else:
        employee_url = base_url + "/api/hrm/employee/"
    employee_data = session.get(employee_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return employee_data.json()

def get_employee_data(profile_id):
    employee_url = base_url + "/api/hrm/employee/"
    url = employee_url + str(profile_id) + "/"
    employee_data = session.get(url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return employee_data.json()

def get_employee_user_name(user_id):
    user_url = base_url + "/api/users/" + user_id
    user_data = session.get(user_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return user_data.json()

def rolePermissions(role_id):
    role_url = base_url + "/api/hrm/role/role_permissions/{}".format(role_id)
    role_data = session.get(role_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return role_data.json()


def get_all_status():
    status_url = base_url + "/api/production/status/"
    status_data = session.get(status_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return status_data.json()


def get_Localities():
    locality_url = base_url + "/api/production/localities/"
    locality_data = session.get(locality_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return locality_data.json()


def get_all_clients():
    clients_url = base_url + "/api/production/clients/"
    clients_data = session.get(clients_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return clients_data.json()


def save_client(data):
    clients_url = base_url + "/api/production/clients/"
    post_data = session.post(clients_url, data=data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return post_data


def get_all_projects():
    projects_url = base_url + "/api/production/projects/"
    projects_data = session.get(projects_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return projects_data.json()


def save_project(data):
    project_url = base_url + "/api/production/projects/"
    post_data = session.post(project_url, data=data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return post_data


def get_client_projects():
    projects_url = base_url + "/api/production/projects/"
    projects_data = session.get(projects_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return projects_data.json()


def get_seq_projects(project_id):
    sequence_url = base_url + "/api/production/projects/sequence/" + str(project_id) + "/"
    sequence_data = session.get(sequence_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return sequence_data.json()


def create_seq(data):
    seq_create_url = base_url + "/api/production/projects/sequence/"
    response = session.post(seq_create_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response.json()


def create_shots(data):
    shot_create_url = base_url + "/api/production/shots/"
    response = session.post(shot_create_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def postShotLogs(data):
    shot_logs_url = base_url + "/api/production/shotlogs/"
    response = session.post(shot_logs_url, data=data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def get_artist_shots(artistId):
    get_shots_url = base_url + "/api/production/mytask/artist/" + str(artistId) + "/"
    response = session.get(get_shots_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_shotByid(shotId):
    shotByid_url = base_url + "/api/production/shots/" + shotId + "/"
    response = session.get(shotByid_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def update_ShotStatus(shotId, data):
    shot_update_url = base_url + "/api/production/shots/" + str(shotId) + "/"
    response = session.put(shot_update_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response


def update_MyTaskShotStatus(taskId, data):
    task_update_url = base_url + "/api/production/mytask/" + taskId + "/"
    response = session.put(task_update_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response.json()


def get_groupId(groupName):
    groupId_url = base_url + "/api/production/groups/" + groupName + "/"
    response = session.get(groupId_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_shotMessages(shotId):
    group_url = base_url + "/api/production/channels/" + str(shotId) + "/"
    response = session.get(group_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def createShot_group(data):
    post_group_url = base_url + "/api/production/groups/"
    response = session.post(post_group_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def post_shotMessages(data):
    post_message_url = base_url + "/api/production/channels/"
    response = session.post(post_message_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def get_qc_Assignment():
    qc_get_url = base_url + "/api/production/qc/qc/"
    response = session.get(qc_get_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def post_qc_Assignment(data):
    qc_assign_url = base_url + "/api/production/qc/qc/"
    response = session.post(qc_assign_url, data=data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def get_qc_AssignmentByTeam(teamId):
    qc_assign_url = base_url + "/api/production/qc/" + str(teamId) + "/"
    response = session.get(qc_assign_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def update_qcById(qcId, data):
    qc_update_url = base_url + "/api/production/update_qc/" + qcId + "/"
    response = session.put(qc_update_url, data=data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def post_hqc_Assignment(data):
    hqc_assign_url = base_url + "/api/production/head_qc/qc/"
    response = session.post(hqc_assign_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def get_hqc_Assignment():
    hqc_assign_url = base_url + "/api/production/head_qc/qc/"
    response = session.get(hqc_assign_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_hqc_AssignmentByHQCID(hqcId):
    hqc_assign_url = base_url + "/api/production/head_qc/" + str(hqcId) + "/"
    response = session.get(hqc_assign_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def update_hqcById(hqcId, data):
    hqc_update_url = base_url + "/api/production/update_head_qc/" + hqcId + "/"
    response = session.put(hqc_update_url, data=data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_hqcTeam():
    hqc_team_url = base_url + "/api/production/head_qc_list/"
    response = session.get(hqc_team_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_permission_groups():
    perm_group_url = base_url + "/api/production/permissions_groups/"
    response = session.get(perm_group_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def allShotsData(status_list, dept=None):
    if dept is not None:
        all_shots_url = base_url + "/api/production/shots/?status=" + status_list + '&dept=' + dept
    else:
        all_shots_url = base_url + "/api/production/shots/?status=" + status_list
    response = session.get(all_shots_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_all_shots(project_id=None):
    if project_id:
        all_shots_url = base_url + "/api/production/shots/?project_id=" + str(project_id)
    else:
        all_shots_url = base_url + "/api/production/shots/"
    response = session.get(all_shots_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def getArtlistByShotId(shotId):
    art_list_url = base_url + "/api/production/mytask/shot/" + str(shotId) + "/"
    response = session.get(art_list_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def getAllArtists():
    all_artists_url = base_url + "/api/hrm/employee/?employment_status=Active"
    response = session.get(all_artists_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()

def getGrades():
    grade_urls = base_url + "/api/hrm/grades/"
    response = session.get(grade_urls, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()

def assign_shot(post_data):
    assign_shot_url = base_url + '/api/production/mytask/'
    response = session.post(assign_shot_url, post_data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def updateTask(task_id, update_data):
    task_update_url = base_url + "/api/production/mytask/" + task_id + "/"
    response = session.put(task_update_url, data=update_data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response


def post_lead_assignment(shot_data):
    post_lead_url = base_url + '/api/production/shot/assignments/'
    response = session.post(post_lead_url, shot_data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def get_lead_shots(lead_id, status_list):
    get_lead_shot_url = base_url + '/api/production/leads/shots/?lead_id=' + lead_id + '&status=' + status_list
    response = session.get(get_lead_shot_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def get_team_list():
    team_url = base_url + '/api/hrm/teams/'
    response = session.get(team_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def getShotVersions(shotId):
    ver_url = base_url + "/api/production/shotversions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def postShotVersions(data):
    post_url = base_url + '/api/production/shotversions/'
    response = session.post(post_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def updateShotVersions(verId, data):
    put_url = base_url + '/api/production/allshotversions/' + verId + '/'
    response = session.put(put_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def getAllShotVersions(shotId):
    ver_url = base_url + "/api/production/allshotversions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def getQcVersions(shotId):
    ver_url = base_url + "/api/production/qcversions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def postQcVersions(data):
    post_url = base_url + '/api/production/qcversions/'
    response = session.post(post_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def updateQcVersions(verId, data):
    put_url = base_url + '/api/production/allqcversions/' + verId + '/'
    response = session.put(put_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def getAllQcVersions(shotId):
    ver_url = base_url + "/api/production/allqcversions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def getClientVersions(shotId):
    ver_url = base_url + "/api/production/client_versions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def postClientVersions(data):
    post_url = base_url + '/api/production/client_versions/'
    response = session.post(post_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def updateClientVersions(verId, data):
    put_url = base_url + '/api/production/all_client_versions/' + verId + '/'
    response = session.put(put_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def getAllClientVersions(shotId):
    ver_url = base_url + "/api/production/all_client_versions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response

def getHQCVersions(shotId):
    ver_url = base_url + "/api/production/hqcversions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def postHQCVersions(data):
    post_url = base_url + '/api/production/hqcversions/'
    response = session.post(post_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def updateHQCVersions(verId, data):
    put_url = base_url + '/api/production/allhqcversions/' + verId + '/'
    response = session.put(put_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def getAllHQCVersions(shotId):
    ver_url = base_url + "/api/production/allhqcversions/" + shotId + "/"
    response = session.get(ver_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def getNotifications(userId):
    notification_endpoint = base_url + "/api/notifications/" + userId + "/"
    response = session.get(notification_endpoint, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def getunreadNotifications(userId):
    notification_endpoint = base_url + "/api/notifications/unread/" + userId + "/"
    response = session.get(notification_endpoint, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def postNotification(data):
    post_url = base_url + '/api/notifications/'
    response = session.post(post_url, data, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response


def getRequestedTaskHelps():
    get_taskHelp_url = base_url + "/api/production/taskhelp_main/"
    response = session.get(get_taskHelp_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def request_TaskHelp(post_data):
    request_taskHelp_url = base_url + '/api/production/taskhelp_main/'
    response = session.post(request_taskHelp_url, post_data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def assign_TaskHelp(post_data):
    assign_taskHelp_url = base_url + '/api/production/taskhelp_artist/'
    response = session.post(assign_taskHelp_url, post_data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def update_ParentStatus(parentId, data):
    parent_update_url = base_url + "/api/production/taskhelp_main/" + str(parentId) + "/"
    response = session.put(parent_update_url, data=data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response


def get_all_task_help_art_shots(artistId):
    task_help_art_shots_url = base_url + "/api/production/taskhelp_artist/artist/" + str(artistId) + "/"
    response = session.get(task_help_art_shots_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def updateTaskHelpArtist(task_id, update_data):
    task_update_url = base_url + "/api/production/taskhelp_artist/" + task_id + "/"
    response = session.put(task_update_url, data=update_data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response


def last_day_log(shot_id):
    day_log_url = base_url + "/api/production/daylogs/?shot_id=" + str(shot_id)
    response = session.get(day_log_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def post_day_logs(post_data):
    day_log_url = base_url + "/api/production/daylogs/"
    response = session.post(day_log_url, data=post_data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response


def update_day_logs(update_data, logId):
    day_log_url = base_url + "/api/production/daylogs/?log_id=" + str(logId)
    response = session.put(day_log_url, data=update_data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response

def update_password(pwd_data, user_id):
    upd_pwd_url = base_url + "/api/user/password_change/"+str(user_id)
    response = session.put(upd_pwd_url, data=pwd_data, headers={'Authorization': 'token {}'.format(token)},
                           verify=False)
    return response

def get_shots_data(url_build):
    filter_url = '/api/production/shots_filter/?' + url_build
    filtr = base_url + filter_url
    response = session.get(filtr, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()

def get_leads_data(url_build):
    filter_url = '/api/production/shots/leads_filter/?' + url_build
    filtr = base_url + filter_url
    response = session.get(filtr, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()
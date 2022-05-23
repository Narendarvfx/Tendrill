import configparser
import datetime

import requests
import urllib3

urllib3.disable_warnings()
config = configparser.ConfigParser()

# TODO: Change config file location while building
config.read(r'\\172.16.3.151\ofxstorage\Repo_Settings\settings.ini')
# config.read(r'D:\Repo_Settings\settings.ini')

base_url = "{}{}".format(config['API']['hostname'], config['API']['port'])
token = config['API']['token']

session = requests.Session()


def get_team_leads_shots(lead_id, start_date=None, end_date=None):
    get_lead_shot_url = base_url + '/api/production/leads/shots/?lead_id=' + lead_id + \
                        '&start_date=' + start_date + '&end_date=' + end_date
    response = session.get(get_lead_shot_url, headers={'Authorization': 'token {}'.format(token)}, verify=False)
    return response.json()


def post_lead_reports(post_data):
    lead_report_url = base_url + '/api/production/teamleadreports/'
    response = session.post(lead_report_url, data=post_data, headers={'Authorization': 'token {}'.format(token)},
                            verify=False)
    return response.json()


def generate_teamlead():
    # TODO: Enable below code while deploying to Production
    yesterday = datetime.datetime.today().date() - datetime.timedelta(days=1)
    # yesterday = datetime.datetime.today().date()
    dates = [yesterday + datetime.timedelta(days=i) for i in range(-1 - yesterday.weekday(), 6 - yesterday.weekday())]
    # start_date = str(dates[0]) + "T00:00:00"
    # end_date = str(dates[-1]) + "T23:59:59"
    start_date = "2022-02-28T00:00:00"
    end_date = "2022-03-06T00:00:00"
    data = get_team_leads_shots(str(26), start_date=start_date, end_date=end_date)
    assigned_mandays = 0
    achieved_mandays = 0
    for dat in data:
        assigned_mandays += dat['shot']['bid_days']
        achieved_mandays += dat['shot']['achieved_mandays']

    post_data = {
        "team_lead": "Kiran Kumar Musku",
        "backlog_mandays": 0,
        "assigned_mandays": round(assigned_mandays, 2),
        "achieved_mandays": round(achieved_mandays, 2),
        "forwarded_mandays": round(assigned_mandays - achieved_mandays, 2),
        "from_date": dates[0],
        "to_date": dates[-1]
    }

    post_lead_reports(post_data)


generate_teamlead()

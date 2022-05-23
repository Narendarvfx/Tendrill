import datetime
import api

class LVersions():
    def __init__(self):
        super(LVersions, self).__init__()

    def create_version(self):
        api_response = api.getQcVersions(str(self.shot_details['id']))
        existing_ver = api_response.json()
        if existing_ver['shot'] is not None:
            version = int(existing_ver['version'].split("V")[1])
            version += 1
        else:
            version = 1
        data = {
            'shot': self.shot_details['id'],
            'version': 'V%03d' % (version),
            'sent_by': self.main_window.employee_details['id'],
            'status': "LAP"
        }
        api.postQcVersions(data)
        # shot_data = {
        #     'version': 'V%03d' % (version),
        #     'submitted_date': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        # }
        # api.update_ShotStatus(str(self.shot_details['id']), shot_data)

    def update_ver_status(self, status):
        api_response = api.getQcVersions(str(self.shot_details['id']))
        existing_ver = api_response.json()
        data = {
            'verified_by': self.main_window.employee_details['id'],
            'verified_date': datetime.datetime.now(),
            'status': status
        }
        api.updateQcVersions(str(existing_ver['id']),data)

if __name__ == '__main__':
    LVersions()
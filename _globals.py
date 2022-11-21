import getpass
import os

G_CLIENTS_ID_LIST = []
G_CLIENTS_LIST = []
G_PROJECTS_LIST = []
G_PROJECTS_ID_LIST = []
G_STATUS_LIST = []
G_STATUS_ID_LIST = []
G_DEPARTMENT_ID_LIST = []
G_DEPARTMENT_LIST = []
G_TEAM_LEAD = False
G_TEAM_LEAD_ID = None

userName = getpass.getuser()


FILTERS_FOLDER = r"P:/Tendrill_configs/"+userName


if not os.path.exists(FILTERS_FOLDER):
    os.makedirs(FILTERS_FOLDER)
FILTERS_FILE = FILTERS_FOLDER+"\\filters.yml"


# NUKE_VERSION = r"C:\Program files\Nuke13.0v2\Nuke13.0.exe"
NUKE_VERSION = r"P:\Nuke13.1.bat"

LOCAL_DRIVE = 'D'

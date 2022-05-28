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

# TODO: Change path before deploying
# FILTERS_FOLDER = "\\\\10.0.0.102\\justvfx_data\\testing\\PipelineTendrill_configs\\"+userName
FILTERS_FOLDER = "C:\\ofxbox\\OFX_ShotBuzz\\shotbuzz_configs\\"+userName

if not os.path.exists(FILTERS_FOLDER):
    os.makedirs(FILTERS_FOLDER)
FILTERS_FILE = FILTERS_FOLDER+"\\filters.yml"

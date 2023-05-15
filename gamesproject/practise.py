import os
import pdb;pdb.set_trace()
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(SETTINGS_PATH, "templates")
import json
with open('user_data.json', 'r') as infile:
    users = json.load(infile)

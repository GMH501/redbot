import os

from redminelib import Redmine


redmine_url = os.getenv('REDMINE_URL')
user = os.getenv('REDMINE_USER')
pwd = os.getenv('REDMINE_PASSWORD')

app = Flask(__name__)
redmine = Redmine(redmine_url, username=user, password=pwd)
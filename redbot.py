import os
import sys
from redminelib import Redmine

if len(sys.argv) > 1:
    if (sys.argv[1] == '--help') or (sys.argv[1] == '-h'):
        print("\nSystem Environment Variable to set before executing redbot.py\n")
        print("URL : Redmine URL to connect to.")
        print("USER : Redmine username to use.")
        print("PASSWORD : Redmine username to use.")
        print("PROJECT: Project on which open the issue.")
        print("ISSUE: Name for the issue to open.")
        print("FILEPATH: Path of the file to attach with the issue.")
        print("FILENAME: Name for the attached file.\n")
        sys.exit(0)

URL = os.getenv('URL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PROJECT = os.getenv('PROJECT')
ISSUE = os.getenv('ISSUE')
FILEPATH = os.getenv('FILEPATH')
FILENAME = os.getenv('FILENAME')

print("==>Connecting to redmine url: {}..".format(URL))
redmine = Redmine(URL, username=USER, password=PASSWORD)
print("   Connected.")

print("==>Creating issue : {}..".format(ISSUE))
try:
    issue = redmine.issue.create(
        project_id=PROJECT,
        subject=ISSUE,
        tracker_id=1,
        description='foo',
        uploads=[{'path': FILEPATH, "filename": FILENAME}]
    )
    print("   Issue created.")
    sys.exit(0)
except Exeception as e:
    print("   ERROR Creating issue: {}".format(e))
    sys.exit(1)
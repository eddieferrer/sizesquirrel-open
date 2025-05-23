import subprocess
import datetime
import sys

from batch_process_feeds import batch_argument_list

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

currentDate = datetime.datetime.today()
print(currentDate)
print("Processing Missing Items...")
for arguments in batch_argument_list:
    subprocess.call(['python', process, 'missing_items', arguments])
    print("Finished:" + arguments)

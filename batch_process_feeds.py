import subprocess
import datetime
import sys

from batch_arguments import BATCH_ARGUMENTS

# create argument list from BATCH_ARGUMENTS
batch_argument_list = []
for feedArgument in BATCH_ARGUMENTS:
    batch_argument_list.append(feedArgument)

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

currentDate = datetime.datetime.today()
print(currentDate)
print("Making Item List...")
subprocess.call(['python', process, 'make_item_list'])
for arguments in batch_argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments])
    print("Finished:" + arguments)
subprocess.call(['python', process, 'make_outfile'])
if len(sys.argv) == 3 and sys.argv[2] == 'cron':
    print("Sending Email Log...")
    subprocess.call(['python', process, 'email_process_log'])


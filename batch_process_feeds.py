import subprocess
import datetime
import sys

from backend.datafeeds import DATA_FEED_INFO_ARRAY

# create argument list from DATA_FEED_INFO_ARRAY
batch_argument_list = []
for feedinfo in DATA_FEED_INFO_ARRAY:
    batch_argument_list.append('--feed=' + feedinfo['retailer_short_name'])

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


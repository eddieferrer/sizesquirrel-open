import subprocess
import datetime

import sys

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

argument_list = [
    '--feed=backcountry',
    '--feed=bentgate', 
    '--feed=blackdiamondequipment',
    '--feed=campsaver',     
    '--feed=lasportiva', 
    '--feed=outdoorgearexchange',
    '--feed=rei',     
]

currentDate = datetime.datetime.today()
print(currentDate)
print("Making Item List...")
subprocess.call(['python', process, 'make_item_list'])
for arguments in argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments])
    print("Finished:" + arguments)
subprocess.call(['python', process, 'make_outfile'])
if sys.argv[2] == 'cron':
    print("Sending Email Log...")
    subprocess.call(['python', process, 'email_process_log'])


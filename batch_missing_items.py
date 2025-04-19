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
print("Processing Missing Items...")
for arguments in argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments, '--sendMissingItems=True'])
    print("Finished:" + arguments)

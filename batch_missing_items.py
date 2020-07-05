import subprocess
import datetime
import sys

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

argument_list = [
    '--feed=adidas_outdoor', 
    '--feed=backcountry',
    '--feed=blackdiamondequipment',
    '--feed=bentgate', 
    '--feed=campsaver',     
    '--feed=ems', 
    '--feed=lasportiva', 
    '--feed=leftlanesports',     
    '--feed=moosejaw', 
    '--feed=rei',     
    '--feed=theclymb'
]

currentDate = datetime.datetime.today()
print(currentDate)
print("Processing Missing Items...")
for arguments in argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments, '--sendMissingItems=True'])
    print("Finished:" + arguments)

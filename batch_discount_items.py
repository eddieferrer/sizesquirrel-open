import subprocess
import datetime
import sys

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

argument_list = [
    '--feed=backcountry',
    '--feed=blackdiamondequipment',
    '--feed=bentgate', 
    '--feed=campsaver',     
    '--feed=ems', 
    '--feed=lasportiva', 
    '--feed=moosejaw', 
    '--feed=rei',     
]

currentDate = datetime.datetime.today()
print(currentDate)
print("Processing Discount Items...")
for arguments in argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments, '--sendDiscountItems=True'])
    print("Finished:" + arguments)

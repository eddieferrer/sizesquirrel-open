import subprocess
import datetime
import sys

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

argument_list = [
    '--feed=adidas_outdoor --sendMissingItems=True', 
    '--feed=backcountry --sendMissingItems=True',
    '--feed=blackdiamondequipment --sendMissingItems=True',
    '--feed=bentgate --sendMissingItems=True', 
    '--feed=campsaver --sendMissingItems=True',     
    '--feed=ems --sendMissingItems=True', 
    '--feed=lasportiva --sendMissingItems=True', 
    '--feed=leftlanesports --sendMissingItems=True',     
    '--feed=moosejaw --sendMissingItems=True', 
    '--feed=rei --sendMissingItems=True',     
    '--feed=theclymb --sendMissingItems=True'
]

currentDate = datetime.datetime.today()
print(currentDate)
print("Processing Missing Items...")
for arguments in argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments])
    print("Finished:" + arguments)

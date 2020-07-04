import subprocess
import datetime
import sys

if sys.argv[1] == 'dev':
    process = 'manage.py'
else:
    process = 'production_manage.py'

argument_list = [
    '--feed=adidas_outdoor --sendDiscountItems=True', 
    '--feed=backcountry --sendDiscountItems=True',
    '--feed=blackdiamondequipment --sendDiscountItems=True',
    '--feed=bentgate --sendDiscountItems=True', 
    '--feed=campsaver --sendDiscountItems=True',     
    '--feed=ems --sendDiscountItems=True', 
    '--feed=lasportiva --sendDiscountItems=True', 
    '--feed=leftlanesports --sendDiscountItems=True',     
    '--feed=moosejaw --sendDiscountItems=True', 
    '--feed=rei --sendDiscountItems=True',     
    '--feed=theclymb --sendDiscountItems=True'
]

currentDate = datetime.datetime.today()
print(currentDate)
print("Processing Missing Items...")
for arguments in argument_list:
    subprocess.call(['python', process, 'process_feeds', arguments])
    print("Finished:" + arguments)

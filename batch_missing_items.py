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
print("Processing Missing Items...")
for arguments in batch_argument_list:
    subprocess.call(['python', process, 'missing_items', arguments])
    print("Finished:" + arguments)

import os
import time

source = ['C:\\Users\Administrator\Pictures\Screenshots', 'C:\\Users\Administrator\Contacts']
target_dir = 'E:\\Backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print (zip_command)
if os.system(zip_command) == 0:
    print ('Backup succesfully created at', target)
else:
    print ('Backup doesnt created')

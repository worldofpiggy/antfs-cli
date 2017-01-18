import subprocess as sp
import getpass as gp
import os 

ACTIVITIES_FOLDER = '~/garmin_activities/*'

get_activities_cmd = 'antfs-cli --pair -a'
upload_cmd = 'gupload -u %s -p %s '+ ACTIVITIES_FOLDER

get_ok = raw_input('Getting new activities from device? y/n \n')
if get_ok in ('y', 'yes', 'ok'):
    print('Getting activities from device')
    sp.call(get_activities_cmd.split(' '))

upload_ok = raw_input('Do you want to upload to Garmin Connect? y/n \n')
if upload_ok in ('y', 'yes', 'ok'):
    username = raw_input('Username:')
    passwd = gp.getpass()
    up_cmd = upload_cmd%(username, passwd)
    os.system(up_cmd)


print('Done. Thanks and goodbye')

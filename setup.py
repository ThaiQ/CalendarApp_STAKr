import platform
import os

print('Installing Required Libraries!\n')
user_os = platform.system()
print('Detected OS: {}'.format(user_os))

if user_os == 'Darwin' or user_os == 'Linux':
    os.system('chmod +x+u+r ./Setup/setup.sh')
    setup_status = os.system('./Setup/setup.sh')
    os.system('chmod -x ./Setup/setup.sh')
elif user_os == 'Windows':
    setup_status = os.system('Setup\setup.bat')

if setup_status == 0:
    print('\nSetup successful! Bye!\n')
else:
    print('\nAn error occured somewhere during the process. Post in the \
#development channel on Slack for help.\n')
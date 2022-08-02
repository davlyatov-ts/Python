#!/usr/bin/env python3

import os

bash_command = ["cd ~/repo/netology/python", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
print(result_os)
for result in result_os.split('\n'):
    if result.find('modified')  != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(directory + '/' + prepare_result)

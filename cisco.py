#!/usr/bin/env python3

import os, sys


paramv = sys.argv[0]
bash_command = [f'cd {paramv}', "git status"]
result_os = os.popen(' && '.join(bash_command)).read()


for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:    ','')
        print(f'{paramv}/{prepare_result}')
    

Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач".<br>

# Обязательная задача 1

```
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```
# Ответ

Вопрос  |Ответ
:-------|:-----
Какое значение будет присвоено переменной ``c``|сложение произвести не получится str нельзя складывать с int
Как получить для переменной ``c`` значение 12?|c = str(a) + b
Как получить для переменной ``c`` значение 3?|a + int(b)
_______________
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать,<br>
какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство,<br>
потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся.<br>
Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?<br>

```
#!/usr/bin/env python3

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```
#Ответ
```
#!/usr/bin/env python3
  
import os

bash_command = ["cd ~/repo/netology/python", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()


for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:    ','')
        print(f'/home/pi/repo/netology/python/{prepare_result}')
```
#Вывод
```
➜  python git:(master) ✗ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   file1

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file1
        modified:   file2.txt
        modified:   file3.txt
        modified:   readme.md

➜  python git:(master) ✗ ./cisco.py
/home/pi/repo/netology/python/  modified:   file1
/home/pi/repo/netology/python/  modified:   file2.txt
/home/pi/repo/netology/python/  modified:   file3.txt
/home/pi/repo/netology/python/  modified:   readme.md
➜  python git:(master) ✗ 
```
_________________________________
Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории,<br>
а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем,<br>
что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.<br>

#Скрипт
```
#!/usr/bin/env python3
  
import os, sys


paramv = sys.argv[1]
bash_command = [f'cd {paramv}', "git status"]
result_os = os.popen(' && '.join(bash_command)).read()


for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:    ','')
        print(f'{paramv}/{prepare_result}')
```
#Вывод скрипта
```
~ cd repo/netology/python 
➜  python git:(master) ✗ 
➜  python git:(master) ✗ git status 
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   cisco.py
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  python git:(master) ✗ cd
➜  ~ ./cisco.py repo/netology/python
repo/netology/python/   modified:   cisco.py
repo/netology/python/   modified:   readme.md
➜  ~ 
```
_________________________________
Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки,<br>
кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел,<br>
занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю,<br>
при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера<br>
не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт,<br>
который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>.<br>
Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки.<br>
Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch:<br>
<старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.<br>

#Скрипт
```
#!/usr/bin/env python3

import socket
import os
import pickle
import json
import yaml

def check_dns(hosts):
    dictionary = {}
    for hostname in hosts:
        dictionary[hostname] = socket.gethostbyname(hostname)
    return(dictionary)

def write_to_pickle(data, filename):
    with open(filename,'wb') as f:
        pickle.dump(data, f)

def write_to_json(data, filename):
    with open(filename,'w') as js:
        js.write(json.dumps(data))

def write_to_yaml(data, filename):
    with open(filename,'w') as ym:
        ym.write(yaml.dump(data, default_flow_style=False))

def read_from_file():
    with open('data.pickle','rb') as f:
        data = pickle.load(f)
        return data

def delimeter():
    print("="*50)

SITES = ("drive.google.com", "mail.google.com", "google.com")
PICKLE_FILE = "data.pickle"
JSON_FILE = "data.json"
YAML_FILE = "data.yml"


delimeter()

if os.path.isfile(PICKLE_FILE):

    old_dict = read_from_file()
    new_dict = check_dns(SITES)

    for host in SITES:
        if old_dict[host] == new_dict[host]:
            print('{:>11} {:>0} - {:>10}'.format("",host, old_dict[host]))
        else:
            print('[ERROR] {:>20} IP mismatch [OLD]: {:>10} [NEW]: {:>10}'.format(host, old_dict[host], new_dict[host]))
            write_to_json(new_dict, 'data.json')
            write_to_yaml(new_dict, 'data.yaml')
    delimeter()
else:
    temp = check_dns(SITES)
    print(temp)
    write_to_pickle(temp, PICKLE_FILE)
    print("File 'data.pickle' is created.")
    print("This file is template fo tests")
```
#Вывод скрипта
```
➜  ~ vim test.py
➜  ~ ./test.py 
==================================================
{'drive.google.com': '173.194.73.194', 'mail.google.com': '173.194.222.18', 'google.com': '74.125.131.100'}
File 'data.pickle' is created.
This file is template fo tests
➜  ~ 
➜  ~ ./test.py
==================================================
            drive.google.com - 173.194.73.194
[ERROR]      mail.google.com IP mismatch [OLD]: 173.194.222.18 [NEW]: 173.194.222.19
[ERROR]           google.com IP mismatch [OLD]: 74.125.131.100 [NEW]: 74.125.131.139
==================================================
``` 

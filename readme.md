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


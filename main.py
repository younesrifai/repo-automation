from os import listdir
from os.path import isfile, join
from getpass import getpass
import sys
import readme
import desc
import create

path = r'C:\Users\youne\OneDrive\Bureau\Code\Repo Automation'

usr=getpass('Enter Email Id:') 
pwd=getpass('Enter Password:') 

try:
    repo_name = sys.argv[1]
except IndexError as e:
    repo_name = 'to-be-determined'

try:
    if sys.argv[2].lower() == 'private':
        privacy = 'private'
    else:
        privacy = 'public'
except IndexError as e:
    privacy = 'public'


#Creating definition and readme file
files = [f for f in listdir() if isfile(join(path,f))]
total_content = ''
file_num = 1

for f in files:
    filepath = join(path,f)
    content = open(filepath).read()
    total_content += f'file {file_num} {f}: {content}\n\n'
    file_num += 1

rme = readme.readme(total_content)
description = desc.desc(total_content)

new_file = open( 'README.md', 'w' )
new_file.write(rme)
new_file.close()

create.create_repo(usr, pwd, repo_name, privacy, path, description)
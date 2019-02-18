#!/usr/bin/env python3
# initialize and setup github
# commit

# echo "alias agit='agit.py'" >> ~/.bash_aliases && source ~/.bash_aliases

help_txt = '''
_________________________________________


Agit version 0.0.2

initialize repo and push to remote repo:
> agit init <<remote Repo>>

Commit and push changes:
> agit commit

_________________________________________


'''
def now():
    return (str(datetime.now().isoformat(timespec='minutes')))


def exe(cmd=""):
    print("agit :[ " + cmd + " ]")
    pe = subprocess.getoutput(cmd)
    return (str(pe))


def commit():
    cm = "git add ."
    print(exe(cm))
    no = now()
    cm = 'git commit -m "' + no + '"'
    print(exe(cm))
    cm = "git push"
    print(exe(cm))


def init(rem=""):
    cm = "echo '# _powered by **Agit**_' >ReadMe.md"
    print(exe(cm))
    cm = "git init"
    print(exe(cm))
    cm = "git add ."
    print(exe(cm))
    no = now()
    cm = 'git commit -m "' + no + '"'
    print(exe(cm))
    cm = 'git remote add origin ' + rem + ''
    print(exe(cm))
    cm = "git push -u origin master"
    print(exe(cm))


if __name__ == "__main__":
    from datetime import datetime
    import sys
    import subprocess
    import os

    dr = os.path.dirname(os.path.realpath(__file__))
    try:
        args = sys.argv[1::]
        if args[0] == "commit":
            commit()
        elif args[0] == "init":
            repo = args[1]
            init(repo)
        elif args[0] == "help":
            print(help_txt)
    except Exception as e:
        print(help_txt)

    print("updating ....")
    cmds = "cd " + dr + " ;" + " git pull"
    print(exe(cmds))

#!/usr/bin/env python3

help_txt = '''
♖ Agit version 0.0.2

Usage:

initialize repo and push to remote repo:
> agit init <<remote Repo>>

Commit and push changes:
> agit commit

Realtime Commit and push changes:
> agit Serve

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
    cm = "echo '# ♖ Agit' >ReadMe.md"
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


def serve():
    di=str(subprocess.getoutput("echo $PWD"))
    print("♖ SERVING ",di," ...")
    while True:
        cmd="git add ."
        ep = str(subprocess.getoutput(cmd))
        cmd='git commit -m "'+now()+'"'
        pe = str(subprocess.getoutput(cmd))
        if pe[0:5]=="On br":
            pass
        else:
            print("♖ Detected changes...")
            print(pe)
            cmd="git push"
            print(exe(cmd))
            print("")
            print("♖ SERVING...")
            print("")
        time.sleep(1)
        

if __name__ == "__main__":
    from datetime import datetime
    import sys
    import subprocess
    import os
    import time

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
        elif args[0] == "serve":
            serve()
    except Exception as e:
        print(help_txt)

    print("updating ....")
    cmds = "cd " + dr + " ;" + " git pull"
    print(exe(cmds))

#!/usr/local/bin/python
# initialize and setup github
# commit
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

def init(rem = ""):
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

    args = sys.argv[1::]
    print(args)
    if args[0] == "commit":
        commit()
    elif args[0] == "init":
        repo = args[1]
        init(repo)

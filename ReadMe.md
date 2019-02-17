

![enter image description here](https://raw.githubusercontent.com/nicodemus-opon/agit/master/log.png)

**Automate git processes**

## installation

Mac

    brew install agit

Linux

    apt-get install agit
   
   

## Usage
### initialize repo and push to remote repo
    agit init https://github.com/username/reponame.git
   equivalent to:

    git init
    git add .
    git commit -m "commit time"
    git remote add origin https://github.com/username/reponame.git
    git push -u origin master

### Commit and push changes

    agit commit

   equivalent to:

    
    git add .
    git commit -m "commit time"
    git push 
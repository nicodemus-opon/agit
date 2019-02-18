**Automate git processes**

## installation

#### Mac/Linux


    git clone https://github.com/nicodemus-opon/agit.git ~/agit
    echo "alias agit='agit.py'" >> ~/.bash_aliases && source ~/.bash_aliases
    echo 'export PATH="$PATH:~/agit"' >> ~/.bashrc && source ~/.bashrc
   
   

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

**Automate git processes**

## installation

#### Linux


    git clone https://github.com/nicodemus-opon/agit.git ~/agit
    cd ~/agit && chmod +x agit.py
    echo "alias agit='agit.py'" >> ~/.profile && source ~/.profile
    echo 'export PATH="$PATH:~/agit"' >> ~/.profile && source ~/.profile
   
   
#### Mac


    git clone https://github.com/nicodemus-opon/agit.git ~/agit
    cd ~/agit && chmod +x agit.py
    echo "alias agit='agit.py'" >> ~/.bash_profile && source ~/.bash_profile
    echo 'export PATH="$PATH:~/agit"' >> ~/.bash_profile && source ~/.bash_profile
   
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

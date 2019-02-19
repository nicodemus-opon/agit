# **Automate git processes**

## installation

#### Linux


    git clone https://github.com/nicodemus-opon/agit.git ~/agit
    cd ~/agit && chmod +x agit.py
    echo "alias agit='python3 ~/agit/agit.py'" >> ~/.bash_aliases
    source ~/.bash_aliases
    
   
   
#### Mac


    git clone https://github.com/nicodemus-opon/agit.git ~/agit
    cd ~/agit && chmod +x agit.py
    echo "alias agit='agit.py'" >> ~/.bash_profile && source ~/.bash_profile
    echo 'export PATH="$PATH:~/agit"' >> ~/.bash_profile && source ~/.bash_profile

#### Windows


    ¯\_(ツ)_/¯
    
   
## Usage
### initialize repo and push to remote repo
    
    agit init https://github.com/username/reponame.git


### Commit and push changes

    agit commit

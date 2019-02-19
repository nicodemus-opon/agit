# **♖ AGIT**

Foobar is a Python library for dealing with word pluralization.


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


### Realtime Commit and push changes

    agit serve

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate .

## License
[MIT](https://choosealicense.com/licenses/mit/)
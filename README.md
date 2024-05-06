# notally2md
Convert any notally backup to markdown files. (beta, still WIP)

## Requirements
- python3
- exported notally backup database
- sqlitebrowser
- MacOS, Debian, Ubuntu or any linux distro (Sorry windows users)

##  Usage
- Install sqlitebrowser from repo on debian based distro, such as Ubuntu.
```
sudo apt-get install sqlitebrowser
```
- open the exported notally backup to sqlitebrowser
- export the BaseNote table to csv and renmame it to "notally_backup.csv"
- Download the python script provided here "notally2md.py"
- open the terminal
- open the folder containing both "notally2md.py" and "notally_backup.csv"
  - type
  ```
  python3 notally2md.py "notally_backup.csv"
  ```
  - the exported md files will be in "markdown_notes" folder.

# vsatak
This is an API developed in Python with Flask and connection to Mysql to handle some tasks.


Prerequisites


Python3.6:

-Ubuntu 16.10 and 17.04

  If you are using Ubuntu 16.10 or 17.04, then Python 3.6 is in the universe repository, so you can just run:

  sudo apt-get update
  sudo apt-get install python3.6

-After installation for Ubuntu 14.04, 16.04, 16.10 and 17.04

  To invoke the Python 3.6 interpreter, run python3.6.
 
-Ubuntu 17.10, 18.04 (Bionic) and onwards

  Ubuntu 17.10 and 18.04 already come with Python 3.6 as default. Just run python3 to invoke it.


Pip3:

The first procedure you followed is correct

sudo apt-get -y install python3-pip

But before installing try to update using command

sudo apt-get update

If first did not work then you can also do this using curl

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3 get-pip.py --user

Then to verify installation try

pip3 --help 

For checking version :

pip3 --version 


MySQL:

pip3 install mysql-connector-python


Flask:

pip3 install flask


Creating the API:

mkdir ~/projects/api
cd ~/projects/api

Copy the file api.py to the folder api. (~/projects/api/api.py)


Run the server:

python3 api.py








References:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get

















 
 

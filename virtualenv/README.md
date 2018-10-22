# virtualenv

[virtualenv](https://pypi.org/project/virtualenv/) is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

## Install virtualenv from pip

    $ pip install virtualenv


## Create the virtual environment

    $ virtualenv -p python3 venv

![virtualenv_create screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_create.png)

Once the virtual env is created, it will create a directory with the name used to create the virtualenv. This directory structure will contain bin, include, lib directories.

### bin
![venv_bin screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/venv_bin.png)

### lib

![venv_lib screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/venv_lib.png)


## Activate the virtual environment

Just creating the virtualenv will not activate the environment. There are explicit commands to activate and deactivate the virtual environment. Once activated the pip commands will work in context to the virtual environment created, unless deactivated

    $ source venv/bin/activate

![virtualenv_activate screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_activate.png)


## List pip dependencies

    $ pip list

This virtual env comes with bare minimum packages, displayed in the screenshot below

![virtualenv_pip_list screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_pip_list.png)


You may now procced to install packages which you need in virtualenv.

    $ pip install requests

Once, requests is installed, running the command pip list now lists the specific dependency set requirements for the virtual environment

![virtualenv_pip_install_requests screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_pip_install_requests.png)


## Freeze and output pip dependencies to a file

Using the pip freeze command we can generate a requirements.txt file to list out the dependencies required for executing the python app in concern. This file may be committed to the repository for other devs/ machine to setup similar env

    $ pip freeze --local > requirements.txt

![virtualenv_pip_freeze screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_pip_freeze.png)


## Install dependencies from requirements.txt

    $ pip install -r requirements.txt

![virtualenv_pip_install screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_pip_install.png)


## Deactivate the virtual environment

    $ deactivate

![virtualenv_deactivate screenshot](https://raw.githubusercontent.com/sumeetsarkar/art-of-python/master/virtualenv/media/virtualenv_deactivate.png)

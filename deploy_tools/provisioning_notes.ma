Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.9
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3.9 python3.9-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace DOMAIN with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── DOMAIN1
            ├── database
            ├── source
            ├── static
            └── virtualenv

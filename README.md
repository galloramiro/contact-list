# contact-list

This is an app with a CRUD of a contacts lists, the idea is that you can doit over the endpoints or by the front privided

## Environment
To run this project you need to install [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/)

Then you can go into the command line
```bash
$ git clone https://github.com/galloramiro/contact-list.git
$ cd contact-list
$ cp contact-list/.env.template contact-list/.env 
$ docker-compose up --build
``` 

You can also populate the db with example data by running the following command:
```bash
$ docker-compose exec contact-list python3 manage.py loaddata example_data.json
```
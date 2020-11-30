# WorkWithDatabase

### Description
The fourth task of course. In this task program needs connect to database, insert data from json file, make some select queries,create indexes, serialize results to json or xml and write to files
SOLID, OOP are required. Can't use ORM.

## Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).


## Installation

You should clone repository:

```console
$ git clone https://github.com/VladKharkevich/WorkWithDatabase.git
```

Enter to folder with project

You should create you virtual enviroment using command

```console
$ virtualenv venv
```

Then you should activate it

```console
$ source venv/bin activate
```

Install dependencies of this app

```console
$ pip install -r requirements.txt
```

Then you should run you database in your docker.

```console
$ docker-compose up -d
```

Now you are ready to run project locally.

To run project you should enter to src folder and run main.py

```console
$ cd src
$ python3 main.py [enter command-line arguments] 
```

To close docker container you should write this command
```console
$ docker-compose down
```

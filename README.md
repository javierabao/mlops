# MLOps Class API

This is the repository with the incremental API project of the MLOps class.

## Getting Started

### Dependencies

* python ≥ 3.10  
* poetry

### Installing

* Clone the repository
* Run `poetry install  --no-root`
* Make sure you are using a python version >=3.10
    * If you don't have such a version, install it
    * Then run `poetry env use python3.12` (or the version of your preference)

### Usage

#### Running the API locally
* In your terminal run `poetry run uvicorn main:app --reload`
* The API should be exposed at http://127.0.0.1:8000/

#### Running the API using Docker
* In your terminal, build the docker image by running `docker build -t mlops-api .`
* Then run the container `docker run -p 8000:8000 mlops-api`
* The API should be exposed at http://127.0.0.1:8000/

## Authors

Javiera Bao


## Version History

* 0.1.1
    * Dockerized API
        * Added Dockerfile and instructions to run the API with Docker
* 0.1.0
    * API exposure with a single integer
        * Function to return the integer just to start modularizing the code (educational purposes)
        * The integer is shown in the "home" page, that is the initial URL, because additional path elements aren't really explanatory, as we don't have context for the class project

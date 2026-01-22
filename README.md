# MLOps Class API

This is the repository with the incremental API project of the MLOps class.

## Getting Started

### Dependencies

* poetry

### Installing

* Clone the repository
* Run `poetry install`
* Make sure you are using a python version >=3.10
    * If you don't have such a version, install it
    * Then run `poetry env use python3.12` (or the version of your preference)

### Usage

#### Exposing the API
* In your terminal run `poetry run uvicorn main:app --reload`
* The API should be exposed in http://127.0.0.1:8000/

## Authors

Javiera Bao


## Version History

* 0.1
    * API exposure with a single integer
        * Function to return the integer just to start modularizing the code (educational purposes)
        * The integer is shown in the "home" page, that is the initial URL, because additional path elements aren't really explanatory, as we don't have context for the class project

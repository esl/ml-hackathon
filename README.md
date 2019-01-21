# ml-hackathon

This is an example of retraining and claficiation of an images based on official tensorflow [tutorial](https://www.tensorflow.org/hub/tutorials/image_retraining).

## Requirements

- [pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- python (tested on 3.6, but migth also work on 3.7)
- make

## Usage

Before you start, it's advised to install all packages within a virtual environment. `pipenv` should be able to create virtual environment and install all necessary packages:

    $ pipenv shell

### Retrain model

Run `make` to fetch all images and start model retraining:

    $ make

Once retraining is over, graph will be available at `assets/tf/retrained_graph.pb`.

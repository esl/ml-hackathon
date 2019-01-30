# ml-hackathon

This is an example of retraining and claficiation of an images based on official tensorflow [tutorial](https://www.tensorflow.org/hub/tutorials/image_retraining).

## Requirements

- [pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- python (tested on 3.6, but migth also work on 3.7)
- make

## Usage

Before you start, it's advised to install all packages within a virtual environment. `pipenv` should be able to create virtual environment and install all necessary packages:

    $ pipenv shell


## NixPkg (very optional)

If you are running NixPkg the packages mentioned in the machine
learning will be available in the included nix-shell. Just run
`nix-shell` in the root of the repository.

One thing that is not included is guildai (because it was not
available as a nix package). It can be installed by:

```shell
> nix-shell
(wait a bit)
nix-shell> virtualenv guild
nix-shell> source guild/bin/activate
nix-shell> pip install guildai
```

This should give you everything you need to run the examples while you
are in the nix-shell.

### Retrain model

Run `make` to fetch all images and start model retraining:

    $ make

Once retraining is over, graph will be available at `assets/tf/retrained_graph.pb`.

### Label image

    $ IMAGE_PATH=assets/images/cats/100833971_a33a86031f.jpg make label_image

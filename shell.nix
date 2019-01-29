with import <nixpkgs> {};

let
  my-python-packages = python36-packages: with python36-packages; [
    nose
    numpy
    tensorflow
    six
    pip
    virtualenvwrapper
    setuptools
    matplotlib
    h5py
  ];
  python-with-my-packages = python36.withPackages my-python-packages;
in
  stdenv.mkDerivation {
    name = "machine_learning_setup";
    buildInputs = [
      python-with-my-packages
    ];
  }

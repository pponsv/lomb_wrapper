# Mirnov viewer

## Installation

Instructions for linux

### Requirements

#### QT

This program uses the QT6 library, and the PyQt6 python bindings to it.
In ubuntu based distributions, you can install it via:

```
sudo apt install qt6-base-dev
```

Older distributions do not provide this package.
In that case, there's a qt5 branch that should work without installing anything.

```
git checkout qt5
```

It also requires libxcb-cursor0, that can be installed using:

```
sudo apt-get install libxcb-cursor0
```

#### Python:

Install the requirements using the provided 'Makefile' and 'requirements.txt'.
This creates a virtual environment in 'env/' and installs all required packages.

```
make configure
```

#### TJII library

The python package to access the TJII library needs to be compiled with gfortran.
The easiest way is using the provided makefile.
This is done automatically in the previous step, but can be repeated if needed using:

```
make build
```

## Running

From the main folder, running

```
make
```

should be enough.

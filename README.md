# Mirnov viewer

## Installation

Instructions for linux

### Requirements

#### QT

This program uses the QT6 library, and the PySide6 python bindings to it.
In ubuntu based distributions, you can install it via:

```
sudo apt install qt6-base-dev
```

It also requires libxcb-cursor0, that can be installed using:

```
sudo apt-get install libxcb-cursor0
```

#### Python:

Some python dependencies need to be compiled with gfortran.
The easiest way is using the provided makefile.

```
make configure
```

## Running

From the main folder, running

```
make
```

should be enough.

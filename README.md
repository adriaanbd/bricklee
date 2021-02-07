# Bricklee

## Install

You can either get it from PyPI or clone it from this repository. Installing it via pip is the easiest.

**From PyPI**

This is preferred.

```shell
$ pip install -i https://test.pypi.org/simple/ bricklee
```

**From GitHub**

If you installed via pip the following isn't necessary and you can go straight to Usage section.

```shell
$ git clone https://github.com/adriaanbd/bricklee.git
```

*with Makefile*
```shell
$ make install
```

*without Makefile*

```shell
$ pip install poetry
$ poetry install -vvv
```

## Usage

Issue a generic greeting:

```shell
$ bricklee hello
Hello Panama, Panama City.
```

Issue a custom greeting:

```shell
$ bricklee hello --name Adriaan
Hello Adriaan.
$ bricklee hello --name Carolina
Hello Carolina.
```


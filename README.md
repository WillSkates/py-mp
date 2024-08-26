# PYMP

An example multithreaded pub-sub Python program.

## Warning

This is a demonstration project only. It is not ready to be used in production.

## Reading

To read the code top-down from the highest entry point, please start in `src/py_mp.py`.

## Why?

I wanted to demonstrate that I know how to:

1. Write a solution to a multithreaded problem.
2. Use pub-sub architectures.
3. Add in dependencies with PIP and venv.
4. Write PEP8 compatible code.
5. Improve code using static analysis tools like Bandit, Mypy and pycodestyle.
6. Create python development environments using Docker (and podman).
7. (Hopefully) write a decent README :).

## Installation

### Prerequisites

You will need these installed:

- [podman](https://podman.io/) (optional, you'll need python3 and pip without it.) (and set up to use 'Rootless' containers).
- [curl](https://curl.se/)
- [gpg](https://gnupg.org/)

### How

To install, first clone the repository and then run the build script:

```bash
git clone https://github.com/WillSkates/py-mp.git
bash ./build
```

## Usage

### Without podman

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./py3 ./check
./py3 python src/py_mp.py
```

### Running the script

```bash
./py3 python src/py_mp.py
```

### Running standards checks

```bash
./py3 ./check
```

## License

This project is published under the MIT license.

Full details can be found in the "LICENSE" file.

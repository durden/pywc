# Script, Library, or Executable: You can have it all!

This repository is a sample application used during the [PyconDE talk titled
Script, Library, or Executable: You can have it all!](https://pyvideo.org/pycon-de-2018/script-library-or-executable-you-can-have-it-all.html).

## Requirements

- Python 3.6 and above
- See [requirements.txt](requirements.txt) for additional requirements
  installable via `pip`

## Setup

### 1. Create virtual environment

- `git clone https://github.com/durden/pywc`
- `python3 -m venv <directory>`

### 2. Install pywc into environment

- `cd` into checked out folder
- `pip install . ` or `make install`

## Usage

- `python -m pywc -h`
    - This works from any current working directory if installed in step 2
      otherwise it will only work when in the checked out directory.

### Entry points

- `python -m pywc`
- `python -m pywc --gui`
- `pywc` (when installed)
- `pywc --gui` (when installed)
- `python cli.py`
- `python gui.py`
- `pywc.exe` (when exe is built)
- `pywcg.exe` (when exe is built)

## Creating executables

- See [Makefile](Makefile)
- The resulting exes will go in the `dist/` folder

## References/feedback

- [Gist link](http://bit.ly/pyconde_pywc_refs)

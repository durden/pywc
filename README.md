# Script, Library, or Executable: You can have it all!

This repository is a sample application used during the [PyconDE talk titled
Script, Library, or Executable: You can have it all!](https://de.pycon.org/schedule/talks/script-library-or-executable-you-can-have-it-all/).

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
- `pip install . `

## Usage
- `python -m pywc -h`
    - This works from any current working directory if installed in step 2
      otherwise it will only work when in the checked out directory.

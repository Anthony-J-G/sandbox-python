# Python Template

This is a template Python repository to bootstrap development and playing around with various python functionality.



## Getting Started

To start working with the repo, here are a few commands to get started.


1. Initialize the virtual environment. This will make a seperate version of python than the 
system version to help keep your module modular and make the rebuilding process easier.

```
$ python -m venv .venv
```


2. Depending on your operating system and shell, the next command might be different.

**Command Prompt.**
```
$ .venv/Scripts/activate.bat
```

**PowerShell**
```
$ .venv/Scripts/activate.ps1
```

**Mac OS**
```
$ source ./.venv/Scripts/activate
```


3. Once you have the virtual environment working you can install the module's dependencies with this:

```
$ pip install -r requirements.txt
```
![Logo of computer with crossed swords and stylized NGenMud with caption: C and Python Hybrid Mud Engone](https://i.imgur.com/dfli5ij.png)
# NGenMUD

This is a mud server written in C with Python (current support 2.x with no plans to upgrade yet). It is a derivative of NakedMud 3.8.1 written by Geoff Hollis. Please see CREDITS and doc/README for details. NakedMud was left in a very workable state with some bugs and some design decisions that needed to be dressed up and this is considered a continuation on that line. The goal is to 
continue the work of removing existing bugs while continuing the common-sense
segregation of some of the core 'world' functionality. I will try to keep a 
full set of backwards compatibility where possible, while providing easy routes of migration where not.

Latest Release:
    (https://github.com/LimpingNinja/ngenmud/releases/latest)
    
# Compiling and Running

Python 2.x is now deprecated, it is getting harder to manage dependencies and ensure that you are building with the correct version of python. The best way do do that now is to use **pyenv**, the installation of PyEnv is relatively simple, follow the instructions on the Github project or basic instructions below. After you install PyEnv then simply doing the following:

1. `pyenv install 2.7.18`
2. Untar/Unzip the package into the directory of your choice and `cd ./ngenmud/src`
3. `pip install scons` 
4. `scons`.
5. Wait for compilation to finish, if there are errors come back here and open an issue!
6. *Optional* `rm ../lib/muddata` - all the settings in here will be recreated off of the default settings, this can be good unless my tests slip in.  
7. From the src/ directory run `./ngenmud &`: This will start the mud running on the port defined in `../lib/muddata` or, if you deleted this file, the default port of 4000.
8. Login and have fun with your game!

## PyEnv
PyEnv lets you easily switch between versions of Python at the global level or at the project level. In this projects root there is a `.python-version`. It is a simple single line file that specifies to PyEnv which version of Python to use.

The instructions for installation are located at https://github.com/pyenv/pyenv#Installation. Those instructions make it seem a bit more complicated then it needs to be. Here are generalized instructions:

### OSX

Homebrew includes pyenv, makes sure you have homebrew (https://brew.sh/) installed and do the following.

```sh
brew install pyenv
```

Restart your shell

```sh
pyenv install 2.7.18
```

This should work since Brew handles the environment variable placement.

### Linux

Some package managers (like pacman/pamac for arch/manjaro) include pyenv and it is as simple as typing `pamac install pyenv`, but these usually do not set the appropriate environment variables so you need to then go into your profile and set these or explicitly run them before working.

If your package manager does not include it, these are generalized instructions:

1. Clone the Repository

To install the latest version of pyenv and provide a straightforward method for updating it, run the following commands to pull it down from GitHub:

```sh
cd $HOME
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

2. Configure the Environment

Run the following block of commands to set some important environment variables and setup pyenv autocompletion:

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
```

If you are using **zsh** then you can replace .bashrc with .zshrc in the above example. After this, restart your shell and install 2.7.18:

```sh
pyenv install 2.7.18
```

### Windows

The best bet here is to run WSL Ubuntu 20.04 and follow the Linux commands. WSL is Windows Subsystem for Linux, it essentially allows you to run a full linux distribution in your terminal without having to switch operating systems: https://docs.microsoft.com/en-us/windows/wsl/install-win10

I have built it in WSL with no problem, the good thing about doing this is you can host it from WSL or you can easily create an executable and deploy it to your mud host or cloud environment to run.

### Note: SCons is Python Specific
If you do not choose to use PyEnv, realize that SCons is built specifically for Python 2.x or Python 3, you will need to install the Python 2.x dependent version to be able to run this. If you have Scons for Python 2.x and Python 3 installed, it will be up to you to ensure that you set the appropriate environmental options to use the right version. Some systems will alias it to scons2, but a google search on your system will help you move forward.



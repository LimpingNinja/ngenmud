# NGenMUD

This is a mud server written in C with Python (current support 2.x with no plans to upgrade yet). It is a derivative of NakedMud 3.8.1 written by Geoff Hollis. Please see CREDITS and doc/README for details. NakedMud was left in a very workable state with some bugs and some design decisions that needed to be dressed up and this is considered a continuation on that line. The goal is to 
continue the work of removing existing bugs while continuing the common-sense
segregation of some of the core 'world' functionality. I will try to keep a 
full set of backwards compatibility where possible, while providing easy routes of migration where not.

Latest Release:
    (https://github.com/LimpingNinja/ngenmud/releases/latest)
    
# Compiling and Running

The SCons system that was put in place prior to the end of NakedMud releases is still fully functional from a type-and-go point of view, v1.0.0 made a modification to ensure libm was included.

1. Install 'SConstruct' in whatever manner your system requires it.
2. Untar/Unzip the package into your directory and `cd ./ngenmud/src`
3. Run: `scons`.
4. Wait for compilation to finish, if there are errors come back here and open an issue!
5. *Optional* `rm ../lib/muddata` - all the settings in here will be recreated off of the default settings, this can be good unless my tests slip in.  
5. Run `./ngenmud &`: This will start the mud running on the port defined in `../lib/muddata` or, if you deleted this file, the default port of 4000.
6. Login and have fun with your game!

## SCons is Python Specific
SCons is built specifically for Python 2.x or Python 3, you will need to 
install the Python 2.x dependent version to be able to run this. If you 
have Scons for Python 2.x and Python 3 installed, it will be up to you to
ensure that you set the appropriate environmental options to use the right
version. Some systems will alias it to scons2, but a google search on your
system will help you move forward.

### OSX

This assumes you do not have SCons installed.

Newer versions of OSX ship with Python 3 as the default, so to get the SCons
setup for Python2.x you will need to run the following:

```bash
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py  -o get-pip.py
python get-pip.py
```

You will then need to add the bin path for Python2.7 to your $PATH, you can
do this by editing .zshrc in your home directory with:

```bash
export PATH=$HOME/Library/Python/2.7/bin:$PATH
```

After this you can install SCons:

```bash
pip install scons
```


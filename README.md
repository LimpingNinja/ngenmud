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
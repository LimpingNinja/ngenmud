# NgenMUD

This is a mud server written in C with Python (current support 2.x with no plans to upgrade yet). It is a derivative of NakedMud 3.8.1.

# Purpose and Intent

NakedMud was left in a very workable state with some bugs and some design decisions that needed to be dressed up. The initial goal was to clean up the apparent bugs and Python integration. The intent, going forward, and the reason for the fork is to modify the Python integration and lib-side default state to remove as much dependency on the C code for game-related and support-related issues. Additionally there will be breaking changes to exposed functions and objects.

# Naming?

I'm not very creative, a long while back I had developed a pike mud driver and lib "GenMud + GenLib" for "Generic". When thinking of a name for a game engine, it made since to simply prepend N (for NakedMud). I also have always disliked the name NakedMud due to the naming and penchant for disrupting search results. Yes, it is intended to sound like "Engine Mud".

# Contributing

I will address contributions on a case-by-case basis, please create an issue and reference your pull request.

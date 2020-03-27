# NgenMUD
---------------
This is a mud server written in C with Python (current support 2.x with no 
plans to upgrade yet). It is a derivative of NakedMud 3.8.1 written by Geoff 
Hollis. Please see CREDITS and original README included at the bottom of this
file for details.

## Intent
---------------
NakedMud was left in a very workable state with some bugs and some design
decisions that needed to be dressed up. The initial goal was to clean up the
apparent bugs and Python integration. The intent, going forward, and the reason
for the fork is to modify the Python integration and lib-side default state to
remove as much dependency on the C code for game-related and support-related 
issues. Additionally there will be breaking changes to exposed functions and
objects.

## Naming
---------------
I'm not very creative, a long while back I had developed a pike mud driver and
lib "GenMud + GenLib" for "Generic". When thinking of a name for a game engine,
it made since to simply prepend N (for NakedMud). I also have always disliked 
the name NakedMud due to the naming and penchant for disrupting search results.
Yes, it is intended to sound like "Engine Mud".

## Contributing
---------------
I will address contributions on a case-by-case basis, please create an issue
on the GitHub and reference your pull request: 
    https://github.com/LimpingNinja/ngenmud/issues

--------------------------------------------------------------------------------
**NakedMud version 3.8.1 (Geoff Hollis)**

NakedMud is a project I started up to keep myself entertained, and fool around
with a couple ideas I could not work with on the MUD I run. The basic idea
behind NakedMud is to provide users with a solid engine for running a MUD, but
without the content that goes along with it.

I really know little about socket handling, and every time I've looked at the
topic, I cringe in horror. That is the reason NakedMud was built on top of
SocketMud(tm); SocketMud(tm) was essentially a glorified chat client when I got
it, which suited my purposes perfectly, since it had all of the socket work
done, leaving all of the fun stuff for me to fool around with. Many thanks go
out to Brian Graversen for writing and releasing SocketMud(tm) to the public.

The origional SocketMud(tm) README has been appended below.

For instructions on getting the MUD up and running, see startup.txt

Geoff Hollis
hollisgf@email.uc.edu
http://www.uc.edu/~hollisgf/

--------------------------------------------------------------------------------
**SocketMud version 1.9 (Brian Graversen) **

Little mud project, which has a command interpreter and supports
ANSI colors... has a nifty little help file system, and a few
commands (say, quit, who, etc). Also supports MCCP version 1 and 2.

I have used a few snippets of Erwin Andreasen's, so if you use this
codebase for something, remember to keep the credits to him, he
deserves it.

Simply type 'make' in the ../src/ directory, and start the mud
by typing './SocketMud &'. You can now connect by telnetting
to port 9009 on localhost (or whatever machine it runs on).

All parts of the SocketMud code written by me, that is contained
in this distribution, is considered public domain, and may be used
as you see fit - but do remember to give credit for Erwin's codebits,
even though they are considered PD as well.

Code and all that by

Brian Graversen (jobo@daimi.au.dk)
